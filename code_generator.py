import rstr
from regex_code import RegexCode as rc
from options_enum import *
import random
import re
import string

class CodeGenerator:

  var_list = []

  
  def __init__(self):
    print(self.generate_code())


  def generate_variable(self, nesting_level, amount = OptionAmount.RANDOM, with_value = OptionDecision.RANDOM) -> str:
    # Se a quantidade de variáveis é Zero, então retorna Vazio
    if amount == OptionAmount.NONE:
      return ''
        
    # Define se as variáveis geradas terão ou não um valor
    has_var_attr = ''
    if with_value == OptionDecision.RANDOM:
      has_var_attr = r'{0,1}'
    elif with_value == OptionDecision.YES:
      # Todas terão atribuição de valor
      has_var_attr = r'{1}'
    else:
      # Nenhuma terá atribuição de valor
      has_var_attr = r'{0}'
    
    # Declaração de variável e possível atribuição de valor
    complete_var_declaration = rc.VAR_NAME + rc.VALUE_ATTRIBUTION + has_var_attr

    # Define a quantidade de variáveis que serão criadas
    qtd_var = '{' + str(amount.value - 1) + '}' if amount.value in range(1,8) else r'{0,6}'

    # Monta regex para geração de N variáveis, de acordo com parâmetros passados
    nvar = r'(' + complete_var_declaration + r')(, ' + complete_var_declaration + r')' + qtd_var

    # Gera definição de variável com identação referente a posição da variável no código
    var_code = (nesting_level * rc.NESTING_SPACE) + rstr.xeger(r'var ' + nvar + r';')

    self.var_list = re.findall(rc.VAR_NAME,var_code)
    self.var_list.pop(0)

    return var_code

    
  def generate_if(self, nesting_level, amountcomp = OptionAmount.RANDOM) -> str: #amount é a qtd de comparacoes no if, definindo a qtd de variaveis
    if amountcomp == OptionAmount.RANDOM:
      var_qtdr = r'{0,'+str(len(self.var_list))+r'}'
    else:
      var_qtdr = r'{'+str(amountcomp-1)+r'}'

    #Calcula a qtd de variaveis para o regex criar a string variavelx com base no índice da variável
    qtd_var = str(len(self.var_list) -1)
    str_if = ''
    list_varre =[]

    #Forma o Regex parametrizado para geração da string posteriormente
    if_1 = rc.IF_1 + qtd_var +r']'
    if_2 = rc.IF_2 + qtd_var+ r']'
    if_3 = rc.IF_3 + qtd_var+ r']'
    if_4 = rc.IF_4 + qtd_var+ r']'
    if_5 = rc.IF_5 + var_qtdr
    if_6 = rc.IF_6 #poderá ser complementado com instruções

    #ajusta tabulacoes de acordo com o nível
    nesting = nesting_level * rc.NESTING_SPACE
    str_if = nesting + rstr.xeger(if_1+if_2+if_3+if_4+if_5+if_6)

    str_if = str_if.replace('instrucoes', nesting + 'instrucoes')
    str_if = str_if.replace('}', nesting + '}')
    
    list_varre = re.findall(r'variavel\d',str_if)
    
   #com base nas variaveis geradas pelo regex, substituimos pelo nome das variaveis existentes
    for item in list_varre:
      indnomevar = int(item.replace("variavel","")) 
      str_if = str_if.replace(item, self.var_list[indnomevar])

    return str_if


  def generate_instruction(self, nesting_level, amountinst = OptionAmount.RANDOM) -> str: #amount é a qtd de instrucoesw                        
    regex_inst = ''

    #define a qtd de instrucoes a serem geradas
    if amountinst == OptionAmount.RANDOM:
      varqtdr = r'0,8}'
    else:
      varqtdr = str(amountinst)+r'}'
    
    qtd_var = str(len(self.var_list) -1)

    #ajusta tabulacoes e forma regex para geração da instrução
    nesting = nesting_level * rc.NESTING_SPACE
    regex_inst = r'(('+nesting + rc.INSTRUCTION_1 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_2 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_3 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_4 
    regex_inst += r'('+nesting + rc.INSTRUCTION_5 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_6 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_7 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_8 + varqtdr

    str_inst=rstr.xeger(regex_inst)
    
    #agora irá sobrescrever as palavras variaveisx de acordo com as variaveis existentes
    list_varre = re.findall(r'variavel\d',str_inst)
    
    
    for item in list_varre:
      indnomevar = int(item.replace("variavel","")) 
      str_inst = str_inst.replace(item, self.var_list[indnomevar])
 
    return str_inst


  def generate_code(self, nesting_level = 0) -> str:
    # Gera variáveis
    partial_code = self.generate_variable(nesting_level, OptionAmount.RANDOM, OptionDecision.RANDOM)
    # Gera estrutura de decisão
    partial_code += "\n"+self.generate_if(nesting_level, OptionAmount.RANDOM)

    # Enquanto houver 'instrucoes' no código e a sorte ajudar. Gera todo um novo código dentro do escopo que está esperando as 'instrucoes'
    old_expression = (nesting_level * rc.NESTING_SPACE) + 'instrucoes'
    if 'instrucoes' in partial_code and random.randrange(0, 2) == 0:
      partial_code = partial_code.replace(old_expression, self.generate_code(nesting_level+1), 1)
    # Senão, insere lógica
    else:
      partial_code = partial_code.replace(old_expression, self.generate_instruction(nesting_level+1, OptionAmount.RANDOM))
      
    return partial_code

CodeGenerator()