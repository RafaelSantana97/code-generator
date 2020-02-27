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



  def generate_variable(self, amount = OptionAmount.RANDOM, with_value = OptionDecision.RANDOM) -> str:
    if amount == OptionAmount.NONE:
      return ''
    
    qtd = '{' + str(amount.value - 1) + '}' if amount.value in range(1,8) else r'{0,6}'
    
    var_attr = ''
    if with_value == OptionDecision.RANDOM:
      var_attr = r'{0,1}'
    elif with_value == OptionDecision.YES:
      var_attr = r'{1}'
    else:
      var_attr = r'{0}'
    
    var = rc.VAR_NAME + rc.VALUE_ATTRIBUTION + var_attr
    nvar = r'(' + var + r')(, ' + var + r')' + qtd

    var_code = rstr.xeger(r'var ' + nvar + r';')

    self.var_list = re.findall(rc.VAR_NAME,var_code)
    self.var_list.pop(0)

    return var_code

  def generate_if(self, amountcomp = OptionAmount.RANDOM) -> str: #amount é a qtd de comparacoes no if, definindo a qtd de variaveis
    
    
    if amountcomp == OptionAmount.RANDOM:
      var_qtdr = r'{0,'+str(len(self.var_list))+r'}'
    else:
      var_qtdr = r'{'+str(amountcomp-1)+r'}'


    qtd_var = str(len(self.var_list) -1)
    str_if = ''
    list_varre =[]

    if_1 = rc.IF_1 + qtd_var +r']'
    if_2 = rc.IF_2 + qtd_var+ r']'
    if_3 = rc.IF_3 + qtd_var+ r']'
    if_4 = rc.IF_4 + qtd_var+ r']'
    if_5 = rc.IF_5 + var_qtdr
    if_6 = rc.IF_6 #poderá ser complementado com instruções

    str_if=rstr.xeger(if_1+if_2+if_3+if_4+if_5+if_6)
    
    list_varre = re.findall(r'variavel\d',str_if)
    
    for item in list_varre:
      indnomevar = int(item.replace("variavel","")) 
      str_if = str_if.replace(item, self.var_list[indnomevar])



    return str_if

  def generate_instruction(self, amountinst = OptionAmount.RANDOM) -> str: #amount é a qtd de instrucoesw                        
    
    regex_inst = ''

    if amountinst == OptionAmount.RANDOM:
       varqtdr = r'0,8}'
    else:
       varqtdr = str(amountinst)+r'}'


    qtd_var = str(len(self.var_list) -1)

    regex_inst = rc.INSTRUCTION_1 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_2 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_3 + qtd_var +r']'
    regex_inst += rc.INSTRUCTION_4 + varqtdr


    str_inst=rstr.xeger(regex_inst)
    
    
    list_varre = re.findall(r'variavel\d',str_inst)
    
    for item in list_varre:
      indnomevar = int(item.replace("variavel","")) 
      str_inst = str_inst.replace(item, self.var_list[indnomevar])

 
    return str_inst


  def generate_code(self) -> str:
    


    code_fim = ''

    code_fim+=self.generate_variable(OptionAmount.RANDOM, OptionDecision.RANDOM)
    code_fim+="\n"+self.generate_if(OptionAmount.RANDOM)

    code_fim = code_fim.replace("instrucoes", self.generate_instruction(OptionAmount.RANDOM))


    return code_fim

CodeGenerator()