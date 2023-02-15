from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5)/20)


driver = iniciar_driver()
# ir até o facebook
driver.get('https://www.facebook.com/')
sleep(5)

# Encontrando campo email
campo_email = driver.find_element(By.ID, 'email')
sleep(2)
campo_email.click()
seu_email = 'testando_testando@gmail.com'
digitar_naturalmente(seu_email, campo_email)
sleep(5)

# Encontrando campo senha
campo_senha = driver.find_element(By.ID, 'pass')
sleep(1)
campo_senha.click()
sleep(3)
sua_senha = 'senha_teste'
digitar_naturalmente(sua_senha, campo_senha)
sleep(2)

# Clicar em login
btn_entrar = driver.find_element(By.XPATH, "//button[@name='login']")
sleep(2)
btn_entrar.click()
sleep(3)

# encontrar e clicar no campo de postagem
campo_status = driver.find_element(By.XPATH,"//div[@class='m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b']")
sleep(2)
campo_status.click()
sleep(5)

# Clicar dentro do campo de status
dentro_campo_status = driver.find_element(By.XPATH,"//p[@class='i1ao9s8h hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5']")
sleep(1)
dentro_campo_status.click()
sleep(1)

# Digitar algo
mensagem = '!!!!ATENÇÃO!!!!, hoje tem promoção na loja XXX'
digitar_naturalmente(mensagem, dentro_campo_status)
sleep(2)

# Clicar em publicar
btn_publicar = driver.find_element(By.XPATH,"//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq s1i5eluu tv7at329']")
sleep(2)
btn_publicar.click()

# Rolar página para visualizar publicações
for x in range(25):
    driver.execute_script('window.scrollTo(0, 500);')
    sleep(2)

driver.close()
