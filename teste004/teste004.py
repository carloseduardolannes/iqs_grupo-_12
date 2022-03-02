from tracemalloc import take_snapshot
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def front(s,t):
    print('=-='*11)
    sleep(t)
    print(f'Step {s}:')

print('=-='*2,'Realizando teste001','=-='*2)

while(True):
    
    t=0
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    ##### Step 1 #####
    passo = 1
    front(passo,t)  
    print('''        Acessar a url: https://escritorioagil.netlify.app/
        ''')
    driver.get('https://escritorioagil.netlify.app/')
    print('Verificando acesso a url:')
    driver.save_screenshot(f'passo{passo}.png') 
    if driver.current_url == 'https://escritorioagil.netlify.app/':
        print("Acessou a url: https://escritorioagil.netlify.app/\n")
        sleep(t)
    else:
        print('Não acessou a url: https://escritorioagil.netlify.app/\n')
        break
    
    ##### Step 2 #####
    front(2,t) 
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
    
    ##### Step 3 #####
    front(3,t) 
    print('''        Completando os campos: 
        Email e ''',end="")
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('carlos@uff.br')
    sleep(t)
    print('Senha.')
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
    sleep(t)
    print('Clicando no Botão entrar') 
    for i in range(1,4):
        print(' * ',end="")      
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
    sleep(1)
    if driver.current_url == 'https://escritorioagil.netlify.app/signin':
        print("Entrou!\n")
        sleep(t)
    else:
        print('Não acessou!')
        break
    
    sleep(1)
    ##### Step 4 #####
    front(4,t) 
    print('''        Clicando em Minha conta
          ''',end="")
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/a[2]').click()
    sleep(t)
    print('''        Clicando em Excluir conta 
          ''',end="")
    driver.find_element(by=By.XPATH, value='/html/body/div/div/section[5]/div/button[1]').click()
    sleep(1)
    
    print('''        Confirmando exclusão da conta 
          ''',end="")
    
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[6]/button[1]').click()
    sleep(1)
    
    print('''        Clicando em ok 
          ''',end="")
    
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[6]/button[1]').click()
    sleep(t)
    
    if driver.current_url == 'https://escritorioagil.netlify.app/':
        print("Entrou!\n")
        sleep(t)
    else:
        print('Não acessou!')
        break
    
    print('=-='*11)
    print('Teste finalizado sem nenhum erro!')
    
    driver.close()
    driver.quit()    
    break