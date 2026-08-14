import urllib.request    # Download

url = "ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/NOV/DOCS/Legislacao_PDF.pdf"
nome = url.split('/')[-1]
urllib.request.urlretrieve(url, nome)

