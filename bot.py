#########
## Inicialmente o bot irá receber o link do produto através do usario, no qual sera monitorado o preço do mesmo. Caso ocorra alguma alteração de preço negativamente, o bot irá avisar o usuario da
## oportunidade de investimento. <vários/produto/usuario>.

## Para o desenvolvimento, será necessario utilizar as bibliotecas do selenium e BeatifulSoup para extração de dados dos e-commerce e pyrogram e dotenv para ciração do bot.
## Integração será feita por meio do Heroku.
#########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import time
import os
from pyrogram import Client
from dotenv import load_dotenv
from datetime import datetime

data_atual = datetime.today().now().date().strftime("%d.%m.%Y")
driver = webdriver.Firefox()
loja = ''
def acessar_produto(url: str):
    driver.get(url)
    if 'mercadolivre' in url:
        loja = 'mercado livre'
    elif 'amazon' in url:
        loja = 'amazon'
    elif 'shopee' in url:
        loja = 'shopee'
    elif 'aliexpress' in url:
        loja = 'aliexpress'
    elif 'kabum' in url:
        loja = 'kabum'
    elif 'terabyte' in url:
        loja = 'terabyte'
    
    verificar_preco(loja)

    
def verificar_preco(loja: str):
    #MERCADO LIVRE
    if loja == 'mercado livre':
        produto = driver.find_element(By.CLASS_NAME, 'ui-pdp-title')
        preco = driver.find_elements(By.CLASS_NAME, 'andes-money-amount__fraction')
        print(f'Nome do produto: {produto.text}, valor: {preco[1].text}, data: {data_atual}')
        input('a: ')
        driver.quit()
    
def comparar_preço(preco_atual, preco_anterior):
    if preco_atual < preco_anterior:
        return ...
    


#__main__
acessar_produto("https://www.mercadolivre.com.br/notebook-nitro-5-an517-52-77kz-i7-w11-512gb-gtx-1650-173/p/MLB19036817?pdp_filters=category:MLB1652#searchVariation=MLB19036817&position=4&search_layout=grid&type=product&tracking_id=888046c2-5fbf-4741-b78c-4b60eab4dc3c")