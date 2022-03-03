from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

###################################
#
### ID: 
### Funcionalidade: aplica uma massa 
#                   de teste
### TEST CASE NAME: não efetuar login 
#                   com dados invalidos  
#
###################################

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#firefox = webdriver.Firefox()
#firefox = webdriver.Chrome()

arquivo_login = open("login.txt", "r")
arquivo_senha = open("senha.txt", "r")
arq = open("combinacao.txt","w")

lista_login = arquivo_login.readlines()
lista_senha = arquivo_senha.readlines()

print(len(lista_login))
print(len(lista_senha))

cont = 0
for i in range (0, len(lista_login)):
    for j in range (0, len(lista_senha)):
        driver.get('https://escritorioagil.netlify.app/')
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Log in').click()
        login = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
        password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        cont = cont + 1
        print(cont, "- Login:", lista_login[i], " senha: ", lista_senha[j])
        login.send_keys(lista_login[i])
        password.send_keys(lista_senha[j])
        submit = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/form/div[4]/button')
        submit.click()
        time.sleep(2)

        try:
            driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/a[2]')
            print("Login válido")
            arq = open("combinacao.txt","w")
            combinacao = []
            combinacao.append("Login:")
            combinacao.append(lista_login[i])
            combinacao.append(" Senha: ")
            combinacao.append(lista_senha[j])
            arq.writelines(combinacao)
            driver.close()
            driver = webdriver.Chrome(options=options)
            driver.get('https://escritorioagil.netlify.app/')
           
        except: 
            print("Login inválido")
            time.sleep(2)
            driver.find_element(by=By.XPATH , value='/html/body/div[2]/div/div[6]/button[1]').click()
            
driver.close()
arq.close()
arquivo_login.close()
arquivo_senha.close()