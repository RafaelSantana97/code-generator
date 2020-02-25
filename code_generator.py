import rstr
from regex_code import RegexCode as rc
from options_enum import *
import random

class CodeGenerator:

  def __init__(self):
    print(self.generate_variable(OptionAmount.THREE, OptionDecision.NO))
    print(self.generate_variable(OptionAmount.NONE))
    print(self.generate_variable(OptionAmount.RANDOM, OptionDecision.RANDOM))
    print(self.generate_variable(OptionAmount.ONE, OptionDecision.YES))


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

    return rstr.xeger(r'var ' + nvar + r';')

CodeGenerator()