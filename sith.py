
def pasto (i):
		valor = int(input("ingrese el valor:"))
		switcher = {
			0: 'caso0',
			1: 'caso1'
			}
		return switcher.get(i, "invalido")

