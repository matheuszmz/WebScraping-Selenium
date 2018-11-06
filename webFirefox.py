# -*- coding: utf-8 -*-
"""
@author: Matheus A. Santana

Orientações:
1. Geckodriver incluso no Path do Computador.
2. Lista Completa de MimeTypes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types

"""


from selenium import webdriver


class driver:

    def __init__ (self, path, mimeType='application/vnd.ms-excel'):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.download.dir", path)
        self.profile.set_preference("browser.download.folderList", 2)
        self.profile.set_preference("browser.download.manager.showWhenStarting", False)
        self.profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mimeType) #MimeType
        self.profile.set_preference("browser.download.manager.focusWhenStarting",False)
        self.profile.set_preference("browser.download.manager.useWindow", False)
        self.profile.set_preference("browser.download.manager.showAlertOnComplete", False)

        self.capabilities = webdriver.DesiredCapabilities().FIREFOX
        self.capabilities['proxy'] = {'proxyType': 'autodetect'}
        self.capabilities['acceptInsecureCerts'] = True
        self.capabilities['marionette'] = True

        self.driver = webdriver.Firefox(capabilities=self.capabilities,
                                        firefox_profile=self.profile)
