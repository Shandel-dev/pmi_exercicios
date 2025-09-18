print("Cálculo de IMC")

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura(em metros): "))
imc = peso / (altura ** 2)
print("Você pesa {}Kg e possui {}m de altura, logo, seu IMC será de {:.2f}Kg/m²".format(peso, altura, imc))