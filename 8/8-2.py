def inicio():
	numero = 1		
	
	while(numero <= 10):
		contador = 1
		while(contador <= 10):
			print(f"{numero} x {contador} = {numero * contador}")
			contador += 1
		print("")
		numero += 1

if __name__ == "__main__":
	inicio()