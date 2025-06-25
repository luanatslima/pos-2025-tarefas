import json

with open("imobiliaria.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

imoveis = dados["imobiliaria"]

print("Opções de Imóveis:")
for i, item in enumerate(imoveis, start=1):
    imovel = item["imovel"][0]
    rua = imovel["endereco"]["rua"]
    bairro = imovel["endereco"]["bairro"]
    cidade = imovel["endereco"]["cidade"]
    print(f"{i} - {rua}, {bairro}, {cidade}")

escolha = input("Digite o ID do imóvel que deseja ver em detalhes: ")

if escolha.isdigit():
    indice = int(escolha) - 1
    if 0 <= indice < len(imoveis):
        imovel = imoveis[indice]["imovel"][0]

        print("--- INFORMAÇÕES DO IMÓVEL ---")
        print(f"Descrição: {imovel['descricao']}")
        print(f"Proprietário: {imovel['proprietario']['nome']}")
        print(f"Email: {imovel['proprietario']['email'][0]['email']}")
        print("Telefones:")
        for tel in imovel["proprietario"]["telefones"]:
            print(f"  - {tel['telefone']}")

        endereco = imovel["endereco"]
        numero = endereco.get("numero", "S/N")
        print(f"Endereço: {endereco['rua']}, Nº {numero}, {endereco['bairro']} - {endereco['cidade']}")

        carac = imovel["caracteristicas"]
        print(f"Tamanho: {carac['tamanho']} m²")
        print(f"Quartos: {carac['numQuartos']}")
        print(f"Banheiros: {carac['numBanheiros']}")
        print(f"Valor: R${imovel['valor']}")
    else:
        print("ID fora do intervalo.")
else:
    print("Entrada inválida.")