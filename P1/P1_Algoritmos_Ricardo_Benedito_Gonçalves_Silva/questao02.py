# Com base no resultado do IMC, o programa deverá classificar
# o aluno de acordo com as seguintes faixas:
# IMC abaixo de 18,5 – abaixo do peso;
# IMC de 18,5 até 24,9 – peso normal;
# IMC de 25,0 até 29,9 – sobrepeso;
# IMC igual ou superior a 30,0 – obesidade.


def calcula_imc(peso, altura):
    return peso / (altura*altura)

peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = calcula_imc(peso, altura)

if imc >= 30:
    status = 'Obesidade'
elif imc >= 25:
    status = 'Sobrepeso'
elif imc >= 18.5:
    status = 'Peso Normal'
else:
    status = 'Abaixo do peso'


print(f'Seu IMC: {imc:.2f}')
print(f'Sua classificação: {status}')