from msilib.schema import Class
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def front(s,t):
    print('=-='*11)
    sleep(t)
    print(f'Step {s}:')
    return None

def screen(teste,passo):
    driver.save_screenshot(f'{teste}_passo{passo}.png')
    return None        

print('=-='*2,'Realizando teste001','=-='*2)

while(True):
    t=0
    teste = "teste001"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    ##### Step 1 #####
    passo = 1.0
    front(passo,t)  
    print('''        Acessar a url: https://escritorioagil.netlify.app/
        ''')
    driver.get('https://escritorioagil.netlify.app/')
    print('Verificando acesso a url:') 
    if driver.current_url == 'https://escritorioagil.netlify.app/':
        print("Acessou a url: https://escritorioagil.netlify.app/\n")
        sleep(t)
        screen(teste,passo)    
    else:
        print('Não acessou a url: https://escritorioagil.netlify.app/\n')
        break
    
    ##### Step 2 #####
    passo = 2.0
    front(passo,t) 
    print('''        Clicando em acessar conta''')
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Log in').click()
    for i in range(1,4):
        print(' * ',end="")
        sleep(t)
    if driver.current_url == 'https://escritorioagil.netlify.app/signin':
        print("Clicou!\n")
        sleep(t)
    else:
        print(f'Não clicou!')
        break

    print('''        Completando os campos: 
        Email e ''',end="")
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('teste@gmail.com')
    sleep(t)
    print('Senha.')
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
    sleep(t)
    screen(teste,passo)
    print('Clicando no Botão entrar') 
    for i in range(1,4):
        print(' * ',end="")      
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
    sleep(1)
    
    ##### Step 3 #####
    passo = 3.0
    sleep(1)
    if driver.current_url == 'https://escritorioagil.netlify.app/teams':
        print("Entrou!\n")
        screen(teste,passo)
        sleep(t)
    else:
        print('Não acessou!')
        break
    sleep(0.5)
    passo = 4
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/a[2]').click()
    passo = 3.1
    sleep(0.5)
    screen(teste,passo)
    print('=-='*11)
    print('Teste finalizado sem nenhum erro!')
    sleep(t)
    
    driver.close()
    driver.quit()    
    break