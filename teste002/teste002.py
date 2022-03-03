from tracemalloc import stop
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def screen(teste,passo):
    driver.save_screenshot(f'teste002\{teste}_passo_{passo}.png')
    return None        

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window() 

t=0
teste = "teste002_cria_novo_time_"

##### Step 1 #####
passo = 1.0 
#Acessar a url: https://escritorioagil.netlify.app/
driver.get('https://escritorioagil.netlify.app/')
print('Verificando acesso a url:')
screen(teste,passo)

##### Step 2 #####
passo = 2.0 
#Clicando em acessar conta
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Log in').click()
#Completando os campos: Email e Senha.
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('teste@gmail.com')
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
screen(teste,passo)
sleep(0.5)
#Clicando no Botão entrar      
driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
sleep(2)
        
##### Step 3 #####
passo = 3.0
#Clicando em Adicionar
driver.find_element(by=By.XPATH, value='/html/body/div/div/div[4]/div[1]/button').click()
screen(teste,passo)
sleep(1)
  
##### Step 4 #####
passo = 4.0
#Cadastrando um novo time
driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input').send_keys('Time dos Sonhos')
driver.find_element_by_xpath("//div[@class='actions']/a").click()
screen(teste,passo)
sleep(0.5)
    
driver.close()
driver.quit()