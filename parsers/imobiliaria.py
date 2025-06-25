from xml.dom.minidom import parse

dom = parse("imobiliaria.xml")
imobiliaria = dom.documentElement
imoveis = imobiliaria.getElementsByTagName("imovel")

print("Imóveis disponíveis:")
for imovel in imoveis:
    id_imovel = imovel.getAttribute("id")
    rua = imovel.getElementsByTagName("rua")[0].firstChild.nodeValue.strip()
    bairro = imovel.getElementsByTagName("bairro")[0].firstChild.nodeValue.strip()
    cidade = imovel.getElementsByTagName("cidade")[0].firstChild.nodeValue.strip()
    print(f"{id_imovel} - {rua}, {bairro}, {cidade}")

escolha = input("Digite o ID do imóvel que deseja: ")

encontrado = False
for imovel in imoveis:
    if imovel.getAttribute("id") == escolha:
        descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue.strip()
        proprietario = imovel.getElementsByTagName("proprietario")[0]
        nome = proprietario.getElementsByTagName("nome")[0].firstChild.nodeValue.strip()
        email_node = proprietario.getElementsByTagName("email")
        email = email_node[0].firstChild.nodeValue.strip() if email_node else "Não informado"
        telefones = proprietario.getElementsByTagName("telefone")

        endereco = imovel.getElementsByTagName("endereco")[0]
        rua = endereco.getElementsByTagName("rua")[0].firstChild.nodeValue.strip()
        bairro = endereco.getElementsByTagName("bairro")[0].firstChild.nodeValue.strip()
        cidade = endereco.getElementsByTagName("cidade")[0].firstChild.nodeValue.strip()
        numero_node = endereco.getElementsByTagName("numero")
        numero = numero_node[0].firstChild.nodeValue.strip() if numero_node and numero_node[0].firstChild else "S/N"

        caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]
        tamanho = caracteristicas.getElementsByTagName("tamanho")[0].firstChild.nodeValue.strip()
        quartos = caracteristicas.getElementsByTagName("numQuartos")[0].firstChild.nodeValue.strip()
        banheiros = caracteristicas.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue.strip()

        valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue.strip()

        print("--- INFORMAÇÕES DO IMÓVEL ---")
        print(f"Descrição: {descricao}")
        print(f"Proprietário: {nome}")
        print(f"Email: {email}")
        print("Telefones:")
        for tel in telefones:
            print(f"  - {tel.firstChild.nodeValue.strip()}")
        print(f"Endereço: {rua}, Nº {numero}, {bairro}, {cidade}")
        print(f"Tamanho: {tamanho} m²")
        print(f"Quartos: {quartos}")
        print(f"Banheiros: {banheiros}")
        print(f"Valor: R${valor}")
        encontrado = True
        break

if not encontrado:
    print("Nenhum imóvel com esse ID foi encontrado!")