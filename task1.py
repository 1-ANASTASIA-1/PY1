# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

translate_number = [{'dec': i, 'bin': bin(i), 'oct': oct(i), 'hex': hex(i)} for i in range(16)]
pprint(translate_number)
