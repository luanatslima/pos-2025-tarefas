from xml.dom.minidom import parse

dom = parse("cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue.strip()
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue.strip()
    ingredientes = prato.getElementsByTagName('ingrediente')
    lista_ingredientes = [i.firstChild.nodeValue.strip() for i in ingredientes]
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue.strip()
    tempo = prato.getElementsByTagName('tempo')[0].firstChild.nodeValue.strip()
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue.strip()

    print("Nome:", nome)
    print("Descrição:", descricao)
    print("Ingredientes:", lista_ingredientes)
    print("Calorias:", calorias)
    print("Tempo:", tempo)
    print("Preço:", preco)
    print("-" * 40)