import requests
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado
codigo = 100
while not codigo == "0":
    codigo = print("Digite um número:")
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
                <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                    <soap:Body>
                        <CapitalCity xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                            <sCountryISOCode>BR</sCountryISOCode>
                        </CapitalCity>
                    </soap:Body>
                </soap:Envelope>"""
    # headers
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    # request POST
    response = requests.request("POST", url, headers=headers, data=payload)

    # imprime a resposta
    print(response.text)
    print(response)