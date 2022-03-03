from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def screen(teste,passo):
    driver.save_screenshot(f'teste004\{teste}_passo_{passo}.png')
    return None        

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

#Teste004 Excluir uma conta

t=0
teste = "teste004_exclui_cadastro_"

##### Step 1 #####
passo = 1.0 
#Acessar a url: https://escritorioagil.netlify.app/
driver.get('https://escritorioagil.netlify.app/')
screen(teste,passo)

##### Step 2 #####
passo = 2.0
#Clicando em acessar conta''')
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Log in').click()
#Completando os campos: Email e Senha.
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('carlos@uff.br')
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
screen(teste,passo)
#Clicando no Botão entrar 
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
sleep(1)
sleep(1)
passo = 2.1
screen(teste,passo)

##### Step 3 #####
passo = 3.0
#Clicando em Minha conta
driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/a[2]').click()
sleep(t)
screen(teste,passo)
#Clicando em Excluir conta 
driver.find_element(by=By.XPATH, value='/html/body/div/div/section[5]/div/button[1]').click()
sleep(1)
passo = 3.1
screen(teste,passo)
#Confirmando exclusão da conta 
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[6]/button[1]').click()
sleep(1)
passo = 3.2
screen(teste,passo)
#Clicando em ok 
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[6]/button[1]').click()
passo = 3.3
screen(teste,passo)
driver.close()
driver.quit()