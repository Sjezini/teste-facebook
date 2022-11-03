# testes facebook
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)

navegador.get("https://pt-br.facebook.com/")


navegador.find_element(
    'xpath', '//*[@id="email"]').send_keys("jezinipsn@gmail.com")

navegador.find_element(
    'xpath', '//*[@id="pass"]').send_keys("teste2134@")

navegador.find_element(
    'xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
