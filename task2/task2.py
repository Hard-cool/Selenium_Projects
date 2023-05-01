from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.expected_conditions import visibility_of
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import json

class Storage(): # Класс для вызова / записи значений из файла
    def FileOutput(self): # Функция для вывода значений из файла
        with open('test.json') as f:
            slov = json.load(f)
        return slov

    def ValueStorage(self, a, key, keyvalue): # Функция для записи переменных в файл
        with open('test.json') as f:
            l = json.load(f)
        l['{}'.format(key)]['{}'.format(keyvalue)] = a

        with open('test.json', 'w') as f:
            f.write(json.dumps(l))
st = Storage()
chromeOptions = Options()
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, chrome_options=chromeOptions)
driver.set_window_size(st.FileOutput()['window_size']['width'], st.FileOutput()['window_size']['height']) ### +

class HomePage(): # Класс для перехода на домашнюю страницу
    def Home(self):
        driver.get(st.FileOutput()['url']['HomePage'])  ### +
        assert st.FileOutput()['url']['HomePage'] in str(driver.current_url)  ### +
        return driver

class About():

    def OpenPage(self):  #Открытие страницы About
        driver.find_element(By.LINK_TEXT, "ABOUT").click()
        assert st.FileOutput()['url']['AboutPage'] in str(driver.current_url)  ### +

    def ch(self, spis): # Логика для вычленения чисел из списка с людьми онлайн и играющими людьми
        for i in range(10):
            try:
                a = int(spis[i])
            except:
                pass
        return a

    def Compare(self): # Сравнение числа игроков онлайн и в игре
        online = driver.find_element(By.XPATH, '//*[@id="about_greeting"]/div[3]/div[1]').text
        play = driver.find_element(By.XPATH, '//*[@id="about_greeting"]/div[3]/div[2]').text
        spis_onl = online.replace(',', '').split()
        spis_pl = play.replace(',', '').split()
        online = self.ch(spis_onl)
        play = self.ch(spis_pl)
        assert online > play

    def Fast(self): # Быстрый вызов методов класса
        self.OpenPage()
        self.Compare()

class TopSellers():
    def Transition(self): # Переход на страницу топа продаж
        elem = driver.find_element(By.XPATH, '//*[@id="noteworthy_tab"]/span/a[1]')
        webdriver.ActionChains(driver).move_to_element(elem).perform()
        WebDriverWait(driver, timeout=5).until(visibility_of(driver.find_element(By.XPATH, '//*[@id="noteworthy_flyout"]/div/a[1]')))
        driver.find_element(By.XPATH, '//*[@id="noteworthy_flyout"]/div/a[1]').click()  # Клик на топ продаж
        assert st.FileOutput()['url']['TopSellersPage'] in str(driver.current_url)  ### +

    def Linux(self): # Клик на чекбокс линукс
        driver.find_element(By.XPATH,'//*[@id="additional_search_options"]/div[7]/div[2]/div[3]/span/span/span[2]').click()
        elem = driver.find_element(By.XPATH, '//*[@id="os"]')
        atr = elem.get_attribute(st.FileOutput()['attributes']['Linux'])  ### +
        assert atr == st.FileOutput()['attributes']['LinuxAttribute'] ### +

    def NumberOfPlayers(self):
        driver.find_element(By.XPATH, '//*[@id="additional_search_options"]/div[4]/div[1]').click()  # Клик на категорию с выбором числа игроков
        driver.find_element(By.XPATH, '//*[@id="additional_search_options"]/div[4]/div[2]')  # Наведение на раскрывающийся при нажатии div
        # WebDriverWait(driver, timeout = 2).until(visibility_of(elem))
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="additional_search_options"]/div[4]/div[2]/div[9]/span/span/span[1]').click()  # Клик на чекбокс кооператива
        elem = driver.find_element(By.XPATH, '//*[@id="additional_search_options"]/div[4]/div[2]/div[9]')
        atr = elem.get_attribute(st.FileOutput()['attributes']['NumberOfPlayers']).split()  ### +
        assert atr[1] == st.FileOutput()['attributes']['NumberOfPlayersAttribute']  ### +
        time.sleep(2)

    def Tags(self):
        driver.find_element(By.XPATH, '//*[@id="TagSuggest"]').send_keys("Action")  # Ввод в поисковое поле
        elem = driver.find_element(By.XPATH, '//*[@id="TagFilter_Container"]/div[8]/span[1]/span/span[2]')  # Выбор Action
        chislo_1 = int(driver.find_element(By.XPATH, '//*[@id="TagFilter_Container"]/div[8]/span[1]/span/span[3]').text)
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//*[@id="search_results"]/div[1]').text.split()
        chislo_2 = int(elem[0])
        assert chislo_1 == chislo_2

    def GameData(self): # Взятие данных о первой игре в списке
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[1]/span').text, 'listforcompare', 'GameName') ### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[2]').text, 'listforcompare', 'GameDate') ### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[4]/div[2]').text, 'listforcompare', 'GamePrice') ### +
    def CompareGameData(self): # Сравнение данных из списка с фактическими на странице игры

        driver.find_element(By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[1]').click()
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="appHubAppName"]').text, 'listforcomparefrompage', 'GameNamePage') ### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[1]/div/div[3]/div[2]/div[2]').text, 'listforcomparefrompage', 'GameDatePage') ### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="game_area_purchase_section_add_to_cart_388899"]/div[2]/div/div[1]').text.split(), 'listforcomparefrompage', 'GamePricePage') ### +
        assert st.FileOutput()['listforcomparefrompage']['GameNamePage'] == st.FileOutput()['listforcompare']['GameName'] and st.FileOutput()['listforcomparefrompage']['GameDatePage'] == st.FileOutput()['listforcompare']['GameDate'] and st.FileOutput()['listforcomparefrompage']['GamePricePage'][0] == st.FileOutput()['listforcompare']['GamePrice']

    def Fast(self): # Быстрый вызов методов класса
        self.Transition()
        self.Linux()
        self.NumberOfPlayers()
        self.Tags()
        self.GameData()
        self.CompareGameData()

class ComunityMarket():

    def LogicForCompare(self):
        schetch = 0
        for i in range(5):  # Логика проверки слов Golden в названии
            a = 0
            spis = (driver.find_element(By.XPATH, '//*[@id="result_{}_name"]'.format(i)).text).split()
            for j in range(len(spis)):
                if spis[j] == st.FileOutput()['itemforcompare']:  ### +
                    a = 1
                    break
                else:
                    a = 0
            if a == 1: schetch += 1
        assert schetch == 5

    def Transition(self): # Перход на страницу комъюнити маркета
        elem = driver.find_element(By.XPATH, '//*[@id="global_header"]/div/div[2]/a[2]')
        webdriver.ActionChains(driver).move_to_element(elem).perform()
        WebDriverWait(driver, timeout=2).until(visibility_of(driver.find_element(By.XPATH, '//*[@id="global_header"]/div/div[2]/div[2]/div/a[4]')))
        driver.find_element(By.XPATH, '//*[@id="global_header"]/div/div[2]/div[2]/div/a[4]').click() # Клик на подкатегорию "магазин"
        assert 'https://steamcommunity.com/market/' == str(driver.current_url) ### +
    def Advanced(self):
        driver.find_element(By.XPATH, '//*[@id="market_search_advanced_show"]/div').click()
        assert driver.find_element(By.XPATH, '/html/body/div[3]')
    def Choose(self):
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//*[@id="app_option_0_selected"]')
        webdriver.ActionChains(driver).move_to_element(elem).click().perform() # Наведение на форму с выбором игры
        elem = driver.find_element(By.XPATH, '//*[@id="app_option_570"]')
        driver.execute_script("arguments[0].scrollIntoView();", elem) # Выбор доты из списка
        elem.click() # Клик на доту
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="market_advancedsearch_filters"]/div[1]/select').click() # Клик на список для выбора героя
        elem = driver.find_element(By.XPATH, '//*[@id="market_advancedsearch_filters"]/div[1]/select/option[48]')
        driver.execute_script("arguments[0].scrollIntoView();", elem) # Скролл до лайфстилера
        elem.click()
        driver.find_element(By.XPATH, '//*[@id="market_advancedsearch_filters"]/div[5]/div[6]/label/span').click() # Клик на иммортал
        elem = driver.find_element(By.XPATH, '//*[@id="advancedSearchBox"]') # Поле для поиска
        elem.click()
        elem.send_keys('golden') ###
    def Search(self): # Функция поиска по заданным параметрам
        driver.find_element(By.XPATH, '//*[@id="advancedSearchSubmit"]').click()
        time.sleep(2)
        #elem = driver.find_elements(By.CSS_SELECTOR, 'a.market_searchedForTerm')
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[1]').text.replace(' ', ''), 'listofvalues', 'GameName')### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[2]').text, 'listofvalues', 'HeroName') ### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[3]').text, 'listofvalues', 'Rarity') ### +
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[4]').text.replace('"', ''), 'listofvalues', 'WordInName') ### +
        assert st.FileOutput()['listofvalues']['GameName'] == st.FileOutput()['testvalues']['GameName'] and st.FileOutput()['listofvalues']['HeroName'] == st.FileOutput()['testvalues']['HeroName'] and st.FileOutput()['listofvalues']['Rarity'] == st.FileOutput()['testvalues']['Rarity'] and st.FileOutput()['listofvalues']['WordInName'] == st.FileOutput()['testvalues']['WordInName'] ###
        self.LogicForCompare()


    def Delete(self):
        driver.find_element(By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[4]/span').click()  # Клик на удаление голден
        #driver.find_element(By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[1]/span').click() # Клик на удаление доты (у стима другая логика, не работает)
        assert st.FileOutput()['listofvalues']['GameName'] == st.FileOutput()['testvalues']['GameName'] and st.FileOutput()['listofvalues']['HeroName'] == st.FileOutput()['testvalues']['HeroName'] and st.FileOutput()['listofvalues']['Rarity'] == st.FileOutput()['testvalues']['Rarity']

    def ItemPage(self):
        driver.find_element(By.XPATH, '//*[@id="result_0"]').click()
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="largeiteminfo_game_name"]').text.replace(' ', ''), 'gamepagevalues', 'GameName')
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="largeiteminfo_item_descriptors"]/div[1]').text.split(), 'gamepagevalues', 'HeroName') # 2
        st.ValueStorage(driver.find_element(By.XPATH, '//*[@id="largeiteminfo_item_type"]').text.split(), 'gamepagevalues', 'Rarity') # 0
        assert st.FileOutput()['gamepagevalues']['GameName'] == st.FileOutput()['testvalues']['GameName'] and st.FileOutput()['gamepagevalues']['HeroName'][2] == st.FileOutput()['testvalues']['HeroName'] and st.FileOutput()['gamepagevalues']['Rarity'][0] == st.FileOutput()['testvalues']['Rarity']

    def Fast(self): # Быстрый вызов методов класса
        self.Transition()
        self.Advanced()
        self.Choose()
        self.Search()
        self.Delete()
        self.ItemPage()


HP = HomePage()
HP.Home()
Ab = About()
Ab.Fast() # Тест кейс 1
HP.Home()
TS = TopSellers()
TS.Fast() # Тест кейс 2
HP.Home()
CM = ComunityMarket()
CM.Fast() # Тест кейс 3
driver.close()



