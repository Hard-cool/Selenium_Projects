from Utils.ConfigUtils import Storage
from selenium.webdriver.common.by import By
from DriverUtils.DriverUtils import BrowserFactory
import random

St = Storage()
class Utils():
    def Generator(self):
        alph, stroka, spis = 'abcdefghigklmnopqrstuvwxyz', '', []
        for i in range(random.randint(1, 10)):
            spis.append(random.choice(alph))
        stroka = ''.join(spis)
        St.ValueStorage('rand', keyvalue = stroka)

    def Kol(self, elem, driver):
        schetch = 0
        elem = driver.find_elements(By.XPATH, '//div[@class="rt-tbody"]/div[@class="rt-tr-group"]/div/div[1]')
        for i in elem:
            if i.text != ' ': schetch += 1
        return schetch

    def GeneratorChisel(self):
        ch = random.randint(-50, 50)
        return ch