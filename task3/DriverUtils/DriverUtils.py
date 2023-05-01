from Utils.ConfigUtils import Storage
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
St = Storage()
class BrowserFactory:
    @staticmethod
    def getWebdriver(browserName):
        if (browserName == 'firefox'):
            option = FirefoxOptions()
            option.add_argument("--width={}".format(St.ConfigOutput()['window_size']['width']))
            option.add_argument("--height={}".format(St.ConfigOutput()['window_size']['height']))
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
            alert = Alert(driver)
            return driver, alert
        elif (browserName == 'chrome'):
            options = webdriver.ChromeOptions()
            options.add_argument('window-size={},{}'.format(St.ConfigOutput()['window_size']['width'],
                                                            St.ConfigOutput()['window_size']['height']))
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
            alert = Alert(driver)
            return driver, alert