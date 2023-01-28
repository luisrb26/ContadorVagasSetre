from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
import re
qntVagas = 0

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

pagina = driver.get('http://www.setre.ba.gov.br/modules/conteudo/conteudo.php?conteudo=280')

page_content = driver.page_source

site = BeautifulSoup(page_content, 'html.parser')

textoVagas = re.findall('\d\d VAGA', site.text)

for vaga in textoVagas:

    qntVagas += int(re.sub('VAGA', '', vaga))

print("Quantidade de vagas hoje: " + str(qntVagas))

#print (site(text=re.compile('VAGA')))
