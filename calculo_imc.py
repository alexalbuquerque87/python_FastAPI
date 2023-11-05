peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / (altura ** 2)

def classificacao_imc(imc):
    if imc < 18.5:
        return "Você está abaixo do peso normal."
    elif 18.5 <= imc < 25:
        return "Você está no peso ideal. Parabéns!"
    elif 25 <= imc < 30:
        return "Você está levemente acima do peso"
    elif 30 <= imc < 35:
        return "Você está com Obesidade grau I"
    elif 35 <= imc < 40:
        return "Você está com Obesidade grau II (severa)"
    elif imc >= 40:
        return "Você está com Obesidade grau III (Mórbida)"

print(f"Seu IMC é: {imc:.2f}")
print(f"{classificacao_imc(imc)}")



# peso = float(input("Informe seu peso (kg):"))
# altura = float(input("Informe sua altura:"))
# imc = peso / (altura ** 2)
# print(f"Seu IMC é: {imc:.2f}")

# if imc < 18.5:
#     print("Você está abaixo do peso normal")
# elif 18.5 <= imc < 25:
#     print("Você está dentro da faixa normal")
# elif 25 <= imc < 30:
#     print("Você está levemente acima do peso")
# elif 30 <= imc < 35:
#     print("Você está em Obesidade grau I")
# elif 35 <= imc < 40:
#     print("Você está em Obesidade grau II")
# elif imc >= 40:
#     print("Você está em Obesidade grau III (Mórbida)")