from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

###################################

### ID: 4
### Funcionalidade: Cadastro e acesso
#                   de um usuario
### TEST CASE NAME: Criar cadastro  

###################################

def screen(teste,passo):
    driver.save_screenshot(f'teste002\{teste}_passo_{passo}.png')
    return None
   
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window() 

#teste003_Fazer um cadastro e logo após realizar um login

t=0
teste = "teste002_realizar_cadastro_e_login_"

##### Step 1 #####
passo = 1.0
  
#Acessando a url: https://escritorioagil.netlify.app/
driver.get('https://escritorioagil.netlify.app/')
#Verificando acesso a url:')
screen(teste,passo)

##### Step 2 #####
passo = 2.0 
#Clicando em Criar conta
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Criar conta').click()
screen(teste,passo)

##### Step 3 #####
passo = 3.0 
#Completando os campos: Nome, Email, Senha e Confirme sua senha.
driver.find_element(by=By.ID, value='name').send_keys('Carlos Lannes')
driver.find_element(by=By.ID, value='email').send_keys('carlos@uff.br')
driver.find_element(by=By.ID, value='password').send_keys('1234567')
driver.find_element(by=By.ID, value='confirmPassword').send_keys('1234567')
screen(teste,passo)  
driver.find_element(by=By.XPATH, value='/html/body/div/div/div/form/div[6]/div[1]/img').click()
sleep(1)
#Selecionando função
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/form/div[6]/div[2]/div[3]/img').click()
sleep(1)
driver.find_element(by=By.XPATH, value='/html/body/div/div/div/form/div[6]/div[1]/img').click()
sleep(1)
passo = 3.1
screen(teste,passo)
#Clicando em Cadastre-se
driver.find_element(By.XPATH, value='//*[@id="root"]/div/div/form/div[7]/button').click()
sleep(1)

##### Step 4 #####
passo = 4.0 
#Completando os campos: Email e Senha.
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('carlos@uff.br')
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
screen(teste,passo)
#Clicando no Botão entrar
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
sleep(1)
passo = 4.1
screen(teste,passo)

driver.close()
driver.quit()