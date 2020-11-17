from pyfiglet import Figlet
custom_fig = Figlet(font='big')
print(custom_fig.renderText('GoMini'))

print('https://github.com/theRedpch')

print('Para cabiar la busqueda: metete en el codigo y cambia "term" ')
print('-----------------------------------------------------------------------------------------')
from googlesearch import search

term = '?id=56' 

for i in search(term, num_results=50, lang='es'):
	print(i)
