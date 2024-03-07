#########
## Inicialmente o bot irá receber o link do produto através do usario, no qual sera monitorado o preço do mesmo. Caso ocorra alguma alteração de preço negativamente, o bot irá avisar o usuario da
## oportunidade de investimento. <vários/produto/usuario>.

## Para o desenvolvimento, será necessario utilizar as bibliotecas do selenium e BeatifulSoup para extração de dados dos e-commerce e pyrogram e dotenv para ciração do bot.
## Integração será feita por meio do Heroku.
#########
'''from selenium import webdriver
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

data_atual = datetime.today().now().date().strftime("%d.%m.%Y")
#driver = webdriver.Firefox()
loja = ''
def acessar_produto(url: str):
    response = requests.get(url)
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
    
    verificar_preco(loja, response)

    
def verificar_preco(loja: str, response):
    #MERCADO LIVRE
    soup = BeautifulSoup(response.text, 'html.parser')
    if loja == 'mercado livre':
        precos = soup.find_all('span', class_='andes-money-amount__fraction')
        preco_inicial = precos[1].text
        produtos = soup.find_all('h1', class_='ui-pdp-title')
        produto_nome = produtos[0].text
        data_consulta = data_atual
    elif loja == 'amazon':
        span_preco = soup.select_one('span.a-price-whole')
        
        #preco = span_preco[13]
        print(span_preco)
        i = 0
        #for item in span_preco[0]:
            #print(item)
            
    
def comparar_preço(preco_atual, preco_anterior):
    if preco_atual < preco_anterior:
        return ...
    


#__main__
acessar_produto("https://www.amazon.com.br/Apple-iPhone-14-128-GB/dp/B0BZ66ZCZ9?pf_rd_r=Y8J4WBG4129AK2Z9J374&pf_rd_t=PageFrameworkApplication&pf_rd_i=16209062011&pf_rd_p=ae3d3dc9-1e88-4cd1-8974-532941e13f8e&pf_rd_s=merchandised-search-4&ref=dlx_16209_sh_dcl_img_0_d7738cc9_dt_mese4_8e")