from bs4 import BeautifulSoup

with open('almacen2.xml', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")

producto = Bs_data.find_all('producto')
#print(producto)

for atributo in Bs_data.find_all('producto', {'categoria':'monitor'}):
    atributo['precio '] = "599,95"
print(Bs_data.prettify())


