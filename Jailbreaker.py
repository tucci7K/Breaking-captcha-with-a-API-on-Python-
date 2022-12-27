from webdriver_manager.chrome import ChromeDriverManager   #GERENCIADOR
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by  import By    #nos permite encontrar coisas no navegador
import time
from anticaptchaofficial.recaptchav2proxyless import * #importar todas as infos da biblio

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #facilitador de vida, manager útil, identifica o chrome driver


link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
solver.set_verbose  (1) #parametro 0, congela o codigo e não mostra, parametro 1, mostra o codigo e etc
solver.set_key('ed6b3ef0ef38f58084acc9df03fd5895') #chave da API
solver.set_website_url('https://google.com/recaptcha/api2/demo')
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    # preencher o campo do token do captcha
    # g-recaptcha-response
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)








time.sleep(100)




