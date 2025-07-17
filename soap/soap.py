import soap as zeep
from xml.dom import minidom

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=wsdl_url)

# MOEDA DO PAÍS
def get_currency(country_code):
    result = client.service.CountryCurrency(country_code)
    print(f"{result.sName} ({result.sISOCode})")

# BANDEIRA DO PAÍS
def get_flag(country_code):
    result = client.service.CountryFlag(country_code)
    print(result)

# NOME DO PAÍS
def get_country_name(country_code):
    result = client.service.CountryName(country_code)
    print(result)

# MENU DE OPÇÕES
print("Escolha uma opção:")
print("1 - Moeda do país")
print("2 - Bandeira do país")
print("3 - Nome completo do país")

opcao = input("Digite o número da opção: ")
codigo = input("Digite o código do país (ex: BR, US, JP): ").upper()

if opcao == '1':
    get_currency(codigo)
elif opcao == '2':
    get_flag(codigo)
elif opcao == '3':
    get_country_name(codigo)
else:
    print("Opção inválida.")