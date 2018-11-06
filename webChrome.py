# -*- coding: utf-8 -*-
"""
@author: Matheus A. Santana


Orientações:
1. Chromedriver incluso no Path do Computador.
"""


from selenium import webdriver


class driver:
    def __init__ (self, mimeType='application/vnd.ms-excel'):
     
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        
        self.driver = webdriver.Chrome(chrome_options=options)
