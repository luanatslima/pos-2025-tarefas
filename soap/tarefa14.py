from zeep import Client

# URL do WSDL
wsdl_url = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'

# Cria cliente Zeep
client = Client(wsdl=wsdl_url)

# Solicita número do usuário
numero = int(input("Digite um número inteiro: "))

# Chamada ao método da API
resultado = client.service.NumberToWords(ubiNum=numero)

# Exibe o resultado
print(f"{numero} por extenso em inglês é: {resultado}")