
class RegexCode:

  VAR_NAME = r'([a-zA-Z]{3,10})'
  VALUE_ATTRIBUTION = r'( = ((\d{1,6})|(\d{2,6} \+ \d{2,6})|(\d{2,3} \* \d{1,3})))'
  
  IF_1 = r'if variavel[0-'
  IF_2 = r' (==|<>|>|<) variavel[0-'
  IF_3 = r' ((and|or) variavel[0-'
  IF_4 = r' (==|<>|>|<) variavel[0-'
  IF_5 = r' )'
  IF_6 = r'?{(\n)instrucoes (\n)}'

  INSTRUCTION_1 = r'((variavel[0-'
  INSTRUCTION_2 = r'= variavel[0-'
  INSTRUCTION_3 = r'( (\+|\-|\*|\\) variavel[0-'
  INSTRUCTION_4 = r'){0,6})(\n)){'
  
  NESTING_SPACE = '  '
