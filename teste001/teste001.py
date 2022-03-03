from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def screen(teste,passo):
    driver.save_screenshot(f'teste001\{teste}_passo_{passo}.png')
    return None

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window() 
   
t=0
teste = "teste001_acesso_url_"   
    
##### Step 1 #####
passo = 1.0  
#Acessando a url: https://escritorioagil.netlify.app/
driver.get('https://escritorioagil.netlify.app/')
screen(teste,passo)
    
##### Step 2 #####
passo = 2.0 
#Clicando em acessar conta
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Log in').click()
#Completando os campos: Email e senha.
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('teste@gmail.com')
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
screen(teste,passo)
#Clicando no Botão entrar    
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
sleep(1)
    
##### Step 3 #####
passo = 3.0
sleep(1)
screen(teste,passo)
sleep(0.5)
passo = 4
driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/a[2]').click()
passo = 3.1
sleep(0.5)
screen(teste,passo)
#Teste finalizado sem nenhum erro!
driver.close()
driver.quit()