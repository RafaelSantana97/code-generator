import rstr
from regex_code import RegexCode as rc
from options_enum import *
import random

class CodeGenerator:

  def __init__(self):
    print(self.generate_variable(OptionAmount.SEVEN))


  def generate_variable(self, amount = OptionAmount.RANDOM, with_value = OptionDecision.RANDOM) -> str:
    qtd = amount - 1 if amount in [range(1,7)] else random.randint(0, 6) if amount == OptionAmount.RANDOM else random.randint(-1, 6)

    if qtd < 0:
      return ''
    
    var_attr = ''
    if with_value == OptionDecision.RANDOM:
      var_attr = r'{0,1}'
    elif with_value == OptionDecision.YES:
      var_attr = r'{1}'
    else:
      var_attr = r'{0}'
    
    var = rc.VAR_NAME + rc.VALUE_ATTRIBUTION + var_attr
    nvar = r'(' + var + r')(, ' + var + r'){0,' + str(qtd) + '}'

    return rstr.xeger(r'var ' + nvar + r';')

CodeGenerator()