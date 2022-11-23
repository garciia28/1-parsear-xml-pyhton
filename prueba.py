from bs4 import BeautifulSoup

with open('Clientes.xml', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml") #Parsear el archivo
#print(Bs_data)

telefonos = Bs_data.find_all('telefono')
#print(telefonos)

cliente = Bs_data.find('cliente', {'ID':'C001'}) #Filtra la info del cliente cuyo igual = 001
#print(cliente)

#Escribir etiqueta, atributo en archivo
for precio in Bs_data.find_all('cliente', {'ID':'C001'}):
    precio['oferta'] = "PROMOCION 2x1"
print(Bs_data.prettify())
