# Selenium Python - Exemplos de uso


## No ubuntu 18.04

### Passo 1 - Instalando Python, Jupyter Notebook, Selenium

[Python 3.6.6](https://www.python.org/) <br>

Abra o terminal e digite

`pip3 install --upgrade pip` <br>
`pip install jupyter` <br>
`pip install selenium` <br>

### Passo 2 - Instalando o WebDriver

Download o webdriver a seu critério:

[Geckodriver - Navegador Firefox](https://github.com/mozilla/geckodriver/releases) <br>
[Chromedriver - Navegador Chrome](http://chromedriver.chromium.org/downloads)

Abra o terminal no diretório Download e digite

`sudo mv <nome do driver> /usr/bin/<nome do driver>` <br>
`sudo chown root:root /usr/bin/<nome do driver>` <br>
`sudo chmod +x /usr/bin/<nome do driver>`

### Passo 3 - Testando funcionamento

No terminal digite `jupyter notebook`, quando abrir, clique em `New` ➤ `Python3`
![Screen](https://uploaddeimagens.com.br/images/001/731/853/full/Deepin_Screenshot_selecionar_%C3%A1rea_20181117120030.png?1542466846)

Digite o código

`from selenium import webdriver`<br>
`driver = webdriver.Chrome()` <br>
`driver.get('https://www.google.com/')` <br>
`driver.find_element_by_name('q').send_keys('Alô Mundo')` <br>
`driver.find_element_by_name('btnK').click()`

![Screen](https://uploaddeimagens.com.br/images/001/731/844/full/Deepin_Screenshot_selecionar_%C3%A1rea_20181117115636.png?1542466662)

