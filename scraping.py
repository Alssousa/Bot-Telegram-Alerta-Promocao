#########
## Inicialmente o bot irá receber o link do produto através do usario, no qual sera monitorado o preço do mesmo. Caso ocorra alguma alteração de preço negativamente, o bot irá avisar o usuario da
## oportunidade de investimento. <vários/produto/usuario>.

## Para o desenvolvimento, será necessario utilizar as bibliotecas do selenium e BeatifulSoup para extração de dados dos e-commerce e pyrogram e dotenv para ciração do bot.
## Integração será feita por meio do Heroku.
#########
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC '''
import requests
from bs4 import BeautifulSoup
import time
import os
from pyrogram import Client
from dotenv import load_dotenv
from datetime import datetime
from models import Produto, Pessoa

data_atual = datetime.today().now().date().strftime("%d.%m.%Y")
loja = ''
url = ''
driver = ''
options = Options()
options.add_argument('--headless')
print("nao e pra estar aquiiii")

def acessar_produto(link: str):
    driver = webdriver.Firefox()
    url = link
    e = False
    try:
        driver.get(url)
    except TimeoutException:
        print("Erro ao abrir o link: TIME OUT EXCEPTION.")
        driver.quit()
        e = True
    except Exception as ex:
        print("Erro nao registrado ao abrir o link: ", ex)
        driver.quit()
        e = True
           
    if not e:    
        if 'mercadolivre' in url:
            loja = 'mercado livre'
        elif 'amazon' in url or 'a.co' in url:
            loja = 'amazon'
        elif 'aliexpress' in url:
            loja = 'aliexpress'
        elif 'kabum' in url:
            loja = 'kabum'
        elif 'terabyte' in url:
            loja = 'terabyte'
        
        print(loja)
        return verificar_preco(loja, driver)

def verificar_preco(loja: str, driver: webdriver):
    #MERCADO LIVRE
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data_consulta = data_atual
    preco_inicial = None
    produto_nome = None
    if loja == 'mercado livre':
        precos = soup.find_all('span', class_='andes-money-amount__fraction')
        preco_inicial = precos[1].text
        produtos = soup.find_all('h1', class_='ui-pdp-title')
        produto_nome = produtos[0].text        
    elif loja == 'amazon':
        precos = soup.find_all("span", class_="a-price")
        preco_inicial = precos[0].text
        produto = soup.find('span', id="productTitle").text
        print(produto)
    driver.quit()
    return produto

def definir_produto(prod_name, prod_preco, usuario, data_verificacao):
    if prod_name and prod_preco and usuario:
        produto = Produto(nome=prod_name, preco_inicial=prod_preco, data_verificacao=data_verificacao, url=url, nome_loja=loja)
        produto.pessoa_id = ''
    
    
def comparar_preço(preco_atual, preco_anterior):
    if preco_atual < preco_anterior:
        return ...
    


#__main__
#acessar_produto("https://a.co/d/6YBwZxH")