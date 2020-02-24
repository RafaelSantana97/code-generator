
import rstr

var_name = r'([a-zA-Z]{3,10})'
var_optional_value = r'( = ((\d{1,6})|(\d{2,6} \+ \d{2,6})|(\d{2,3} \* \d{1,3}))){0,1}'
var = var_name + var_optional_value
nvar = r'(' + var + r')(, ' + var + r'){0,4}'

var_declaration = rstr.xeger(r'var ' + nvar + r';')

print(var_declaration)