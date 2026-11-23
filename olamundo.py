altura = float(input("Digite sua altura: "))
peso = float(input ("digite seu peso: "))

imc = peso / (altura * altura)

print(imc)

#analise detalhadas dos pesos

if imc < 18.5:
    print("peso abaixo do normal")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print("esta em sobrepeso")
elif imc < 34.9:
    print("obesidade grau 1")
elif imc < 39.9:
   print("obsidade grau 2")
elif imc < 44.9:
   print("obsidade grau 3")
elif imc < 49.9:
   print("obsidade morbida")