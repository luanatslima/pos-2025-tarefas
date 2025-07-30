import requests
from getpass import getpass
from tabulate import tabulate


base_url = "https://suap.ifrn.edu.br/api/"


user = input("Usuário: ")
password = getpass("Senha: ")


# Autenticação
auth_response = requests.post(f"{base_url}/v2/autenticacao/token/", json={"username": user, "password": password})
auth_data = auth_response.json()


if "access" not in auth_data:
    print("Erro ao autenticar:", auth_data)
    exit()


token = auth_data["access"]
headers = {"Authorization": f"Bearer {token}"}


# Parâmetros do boletim
ano_letivo = input("Ano letivo (ex: 2025): ")
periodo_letivo = input("Período letivo (1 ou 2): ")


# Requisição do boletim
boletim_url = f"{base_url}/ensino/meu-boletim/{ano_letivo}/{periodo_letivo}/"


# Requisição do boletim
response = requests.get(boletim_url, headers=headers)


if response.status_code != 200:
    print("Erro ao buscar boletim:", response.text)
    exit()


# Captura os dados corretamente
notas_dict = response.json()
notas = notas_dict.get("results", [])


# Verifica se 'notas' é realmente uma lista de dicionários
if not isinstance(notas, list):
    print("Formato inesperado de boletim:", notas)
    exit()


tabela = []


for disciplina in notas:
    if not isinstance(disciplina, dict):
        print("Ignorado: item não é dicionário →", disciplina)
        continue


    nome_disciplina = disciplina.get("disciplina", {}).get("nome", "Desconhecida")
    linha = [nome_disciplina]


    for i in range(1, 5):
        nota = disciplina.get(f"nota_unidade_{i}", "—")
        linha.append(nota)


    tabela.append(linha)


# Exibir tabela final
cabecalho = ["Disciplina", "U1", "U2", "U3", "U4"]
print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))

