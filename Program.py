#importando a biblioteca para lidar com os números decimais de forma precisa
import decimal

#Função para receber um número como argumento
def obter_mes():
    while True:
        numero_digitado = input("Digite um número de 1 a 12: ")
#para converter a entrada em um objeto decimal para depois em um número inteiro, podemos fazer
        try:
            numero = decimal.Decimal(numero_digitado)
            numero_inteiro = int(numero)

#verificamos se o número é normal
            if numero.is_normal() and numero == numero_inteiro and 1 <= numero <= 12:
                meses = [
                    "Janeiro",
                    "Fevereiro",
                    "Março",
                    "Abril",
                    "Maio",
                    "Junho",
                    "Julho",
                    "Agosto",
                    "Setembro",
                    "Outubro",
                    "Novembro",
                    "Dezembro",
                ]
                nome_mes = meses[numero_inteiro - 1]

#se tudo ocorrer conforme o esperado, então é retornado o nome do mês
                return nome_mes

#E aqui tratamos dos erros de input errados pela parte do usuário
            else:
                print ("O número deve ser um número inteiro entre 1 e 12.")
        except decimal.InvalidOperation:
            return ("O valor inserido não é um número válida")

nome_mes = obter_mes()
print(nome_mes)