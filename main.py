from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get('https://www.dio.me/sign-in')

email = ''/#Digite seu email
senha = ''/#Digite sua senha

campo_email = navegador.find_element('xpath', '//*[@id="__next"]/main/div/section/form/div[1]/input')
campo_email.send_keys(email)
campo_senha = navegador.find_element('xpath', '//*[@id="__next"]/main/div/section/form/div[2]/input')
campo_senha.send_keys(senha)
botao = navegador.find_element('xpath', '//*[@id="__next"]/main/div/section/form/button')
botao.click()