peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Cálculo do IMC
imc = peso / (altura * altura)

# Exibição do resultado
print(f"Seu IMC é: {imc}")