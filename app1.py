def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    try:
        peso = float(input("Informe seu peso em kg: "))
        altura = float(input("Informe sua altura em metros: "))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
