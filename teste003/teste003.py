from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def front(s,t):
    print('=-='*11)
    sleep(t)
    print(f'Step {s}:', end="")
    
def screen(teste,passo):
    driver.save_screenshot(f'{teste}_passo{passo}.png')
    return None

print('=-='*2,'Realizando teste003','=-='*2)

while(True):
    
    t=0
    teste = "teste003"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    ##### Step 1 #####
    
    passo = 1.0
    front(passo,t)
      
    print('''Acessar a url: https://escritorioagil.netlify.app/
        ''')
    driver.get('https://escritorioagil.netlify.app/')
    print('Verificando acesso a url:')

    if driver.current_url == 'https://escritorioagil.netlify.app/':
        print("Acessou a url.\n", end="")
        sleep(t)
    else:
        print('Não acessou a url: https://escritorioagil.netlify.app/\n')
        break
    screen(teste,passo)
    
    ##### Step 2 #####
    
    passo = 2.0
    front(passo,t) 
    print('Clicando em Criar conta')
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Criar conta').click()
    for i in range(1,4):
        print(' * ', end="")
        sleep(t)
    if driver.current_url == 'https://escritorioagil.netlify.app/register':
        print("Clicou!\n", end="")
    else:
        print(f'Não clicou!')
        break
    screen(teste,passo)
    
    ##### Step 3 #####
    
    passo = 3.0
    front(passo,t) 
    print('Completando os campos: Nome, ',end="")
    driver.find_element(by=By.ID, value='name').send_keys('Carlos Lannes')
    sleep(t)
    print(' Email,', end="")
    driver.find_element(by=By.ID, value='email').send_keys('carlos@uff.br')
    sleep(t)
    print(' Senha')
    driver.find_element(by=By.ID, value='password').send_keys('1234567')
    sleep(t)
    print('e Confirme sua senha.')
    driver.find_element(by=By.ID, value='confirmPassword').send_keys('1234567')
    sleep(t)
    screen(teste,passo)
    for i in range(1,4):
        print(' * ',end="")  
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div/form/div[6]/div[1]/img').click()
    sleep(0.5)
    print('\nSelecionando função')
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/form/div[6]/div[2]/div[3]/img').click()
    
    sleep(0.5)
    driver.find_element(by=By.XPATH, value='/html/body/div/div/div/form/div[6]/div[1]/img').click()
    sleep(0.5)
    passo = 3.1
    screen(teste,passo)
    print('Clicando em Cadastre-se')
    driver.find_element(By.XPATH, value='//*[@id="root"]/div/div/form/div[7]/button').click()
    sleep(0.5)
    for i in range(1,4):
        print(' * ',end="")
        sleep(t)
    if driver.current_url == 'https://escritorioagil.netlify.app/signin':
        print("Clicou!\n", end="")
        sleep(t)
    else:
        print('Não clicou!')
        break

    ##### Step 4 #####
    
    passo = 4.0
    front(passo,t) 
    
    print('Completando os campos: Email e ',end="")
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/input').send_keys('carlos@uff.br')
    sleep(t)
    print('Senha.')
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[3]/input').send_keys('1234567')
    sleep(t)
    screen(teste,passo)
    print('Clicando no Botão entrar')
    driver.find_element(by=By.XPATH, value='/html/body/div/div/form/div[4]/button').click()
    sleep(1)
    
    if driver.current_url == 'https://escritorioagil.netlify.app/teams':
        print("Criou o login e logou!\n", end="")
        sleep(t)
    else:
        print('Criou o login e não logou!')
        break
    passo = 4.1
    screen(teste,passo)
    print('=-='*11)
    print('Teste finalizado sem nenhum erro!')
    
    sleep(t*3)
    
    driver.close()
    driver.quit()
    
    break