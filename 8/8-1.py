def inicio():
	numero = int(input("Informe um numero: "))

	contador = 1
	while(contador <= 10):
		print(f"{numero} x {contador} = {numero * contador}")
		contador +=1

if __name__ == "__main__":
	inicio()