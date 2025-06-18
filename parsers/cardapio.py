from xml.dom.minidom import parse

dom = parse("cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')

print("Menu:")
for prato in pratos:
    id_prato = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue.strip()
    print(f"{id_prato} - {nome}")

escolha = input("Digite o ID do prato que deseja: ")

encontrado = False
for prato in pratos:
    if prato.getAttribute('id') == escolha:
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue.strip()
        descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue.strip()
        ingredientes = prato.getElementsByTagName('ingrediente')
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue.strip()
        tempo = prato.getElementsByTagName('tempo')[0].firstChild.nodeValue.strip()
        preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue.strip()

        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        print("Ingredientes:")
        for i in ingredientes:
            print("  -", i.firstChild.nodeValue.strip())
        print(f"Calorias: {calorias}")
        print(f"Tempo de preparo: {tempo}")
        print(f"Preço: R${preco}")
        encontrado = True
        break

if not encontrado:
    print("Nenhum prato com esse ID foi encontrado!")