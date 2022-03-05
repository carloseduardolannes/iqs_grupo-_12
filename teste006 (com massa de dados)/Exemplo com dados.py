from turtle import clear
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

arquivo_login = open(".\Teste006 (com massa de dados)\login.txt", "r")
arquivo_senha = open(".\Teste006 (com massa de dados)\senha.txt", "r")

lista_login = arquivo_login.readlines()
lista_senha = arquivo_senha.readlines()

print(f'Número de logins {len(lista_login)}')
print(f'Número de senhas {len(lista_senha)}')

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
            combinacao = []
            combinacao.append("Login:")
            combinacao.append(lista_login[i])
            time.sleep(0.5)
            combinacao.append(" Senha: ")
            combinacao.append(lista_senha[j])
            arq = open("Teste006 (com massa de dados)\combinacao valida.txt","a")
            arq.writelines('')
            arq.writelines(combinacao)
            arq.close()
            driver.close()
            driver = webdriver.Chrome(options=options)
            driver.get('https://escritorioagil.netlify.app/')
           
        except: 
            print("Login inválido\n")
            time.sleep(2)
            driver.find_element(by=By.XPATH , value='/html/body/div[2]/div/div[6]/button[1]').click()
            
driver.close()
driver.quit()
arq.close()
arquivo_login.close()
arquivo_senha.close()
SystemExit