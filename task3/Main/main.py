import time
from selenium import webdriver
from Utils.ConfigUtils import Storage
from Utils.Utils import Utils
from DriverUtils.DriverUtils import BrowserFactory
from selenium.webdriver.support.expected_conditions import visibility_of, alert_is_present, number_of_windows_to_be
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Test.test_toolsqa import Testing



St = Storage()
Ut = Utils()
Ut.Generator()
driver, alert = BrowserFactory.getWebdriver(St.ConfigOutput()['browser'])
Te = Testing()

class Alerts():
    def HomePage(self): #TC 1.1
        driver.get(St.ValueOutput()['url']['homepage'])
        Te.test_HomePage(str(driver.current_url))

    def AlertForm(self): #TC 1.2
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Alerts, Frame & Windows"]').click() # Клик на кнопку перехода к предупреждениям и фреймам
        driver.find_element(By.XPATH, '//ul[@class="menu-list"]/li/span[text()="Alerts"]').click() # Клик на предупреждения
        elem = driver.find_element(By.ID, 'javascriptAlertsWrapper') # Поле с выбором алертов
        Te.test_AlertForm(elem)

    def ClickAlert(self): #TC1.3
        driver.find_element(By.ID, 'alertButton').click()
        Te.test_ClickAlert(alert.text)

    def ClickAlertButton(self): #TC1.4
        alert.accept()
        # Проверку можно сделать только через try/except

    def ClickConfirmAlert(self): #TC1.5
        driver.find_element(By.ID, 'confirmButton').click()
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(alert_is_present())
        Te.test_ClickConfirmAlert(alert.text)

    def ClickAlertConfirmButton(self): #TC1.6
        self.ClickAlertButton()
        elem = driver.find_element(By.ID, 'confirmResult').text
        Te.test_ClickAlertConfirmButton(elem)

    def ClickAlertPromptButton(self): #TC1.7
        driver.find_element(By.ID, 'promtButton').click()
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(alert_is_present())
        Te.test_ClickAlertPromptButton(alert.text)

    def RandomText(self): #TC1.8
        alert.send_keys(St.ValueOutput()['rand'])
        alert.accept()
        elem = driver.find_element(By.ID, 'promptResult').text
        Te.test_RandomText(elem)



class Iframe(Alerts):
    def NestedFrames(self): #TC 2.2
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Alerts, Frame & Windows"]').click() # Клик на кнопку перехода к предупреждениям и фреймам
        driver.find_element(By.XPATH, '//ul[@class="menu-list"]/li/span[text()="Nested Frames"]').click()
        elem = driver.find_element(By.ID, 'frame1')
        driver.switch_to.frame(elem)
        St.ValueStorage('framepage_1', 'outerframe', driver.find_element(By.XPATH, '//body').text) # Текст внешнего фрейма
        elem = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(elem)
        St.ValueStorage('framepage_1', 'innerframe', driver.find_element(By.XPATH, '//p').text) # Текст внутреннего фрейма
        driver.switch_to.default_content()
        Te.test_NestedFrames(driver.current_url)

    def Frames(self): #TC 2.3
        driver.find_element(By.XPATH, '//ul[@class="menu-list"]/li/span[text()="Frames"]').click()
        elem = driver.find_element(By.ID, 'frame1')
        driver.switch_to.frame(elem)
        St.ValueStorage('framepage_2', 'topframe', driver.find_element(By.TAG_NAME, 'body').text)
        driver.switch_to.default_content()
        elem = driver.find_element(By.ID, 'frame2')
        driver.switch_to.frame(elem)
        St.ValueStorage('framepage_2', 'bottomframe', driver.find_element(By.TAG_NAME, 'body').text)
        driver.switch_to.default_content()
        Te.test_Frames()

class Tables(Alerts):

    def ElementsClick(self): #TC 3.2
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Elements"]').click()
        driver.find_element(By.ID, 'item-3').click()
        Te.test_ElementsClick(driver.current_url)

    def ButtonClick(self): #TC 3.3
        driver.find_element(By.ID, 'addNewRecordButton').click()
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(visibility_of(driver.find_element(By.ID, 'firstName-wrapper')))
        elem = driver.find_element(By.XPATH, '//div[@aria-modal="true"]/div/div[@class="modal-content"]')
        Te.test_ButtonClick(elem)

    def TableFilling(self): #TC 3.4
        for j in range(1, 3):
            for i in range(1, 7):
                driver.find_element(By.XPATH, '//form[@id="userForm"]/div[@class="mt-2 row"][{}]/div[2]/input'.format(i)).send_keys(St.ValueOutput()['person_{}'.format(j)]['row_{}'.format(i)])
            driver.find_element(By.ID, 'submit').click()
            if j == 1:
                driver.find_element(By.ID, 'addNewRecordButton').click()
        #assert driver.find_element(By.XPATH, 'body[@class=""]') Не за что завязать проверку наличия формы на странице

    def RowDelete(self): #TC 3.5
        elem = driver.find_elements(By.XPATH, '//div[@class="rt-tbody"]/div[@class="rt-tr-group"]/div/div[1]')
        St.ValueStorage('testvalues', 'before', Ut.Kol(elem, driver))
        driver.find_element(By.ID, 'delete-record-4').click()
        St.ValueStorage('testvalues', 'after', Ut.Kol(elem, driver))
        Te.test_RowDelete()

class Handles(Alerts):

    def BrowserWindows(self):
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Alerts, Frame & Windows"]').click()
        driver.find_element(By.XPATH, '//ul[@class="menu-list"]/li/span[text()="Browser Windows"]').click()
        Te.test_BrowserWindows(driver.current_url)

    def NewTab(self):
        driver.find_element(By.ID, 'tabButton').click()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(
            number_of_windows_to_be(2))
        Te.test_NewTab(driver.current_url)

    def CloseTab(self):
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def Links(self):
        driver.find_element(By.XPATH, '//span[@class="group-header"]/div[@class="header-wrapper"]/div').click()
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(visibility_of(driver.find_element(By.ID, 'item-5')))
        driver.find_element(By.ID, 'item-5').click()
        Te.test_Links(driver.current_url)

    def HomeLink(self):
        driver.find_element(By.ID, 'simpleLink').click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        Te.test_HomeLink(driver.current_url)

    def PrevPage(self):
        driver.switch_to.window(driver.window_handles[0])
        Te.test_Links(driver.current_url)

class Sl_Prbar(Alerts):

    def Widgets(self):
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Widgets"]').click()
        driver.execute_script("window.scrollTo(0, 200)")
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(
            visibility_of(driver.find_element(By.XPATH, '//ul[@class="menu-list"]/li[4]/span[text()="Slider"]')))
        driver.find_element(By.XPATH, '//*[@id="item-3"]/span[text()="Slider"]').click()
        driver.execute_script("window.scrollTo(0, -200)")
        Te.test_Widgets_1(driver.current_url)

    def Move(self):
        WebDriverWait(driver, timeout=St.ConfigOutput()['wait']).until(
            visibility_of(driver.find_element(By.XPATH, '//div[@class="col-9"]/span/input[@value="25"]')))
        elem = driver.find_element(By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/input')
        ch = Ut.GeneratorChisel()
        if ch > 0:
            webdriver.ActionChains(driver).move_to_element(elem).move_by_offset(elem.size['width'] / 100 * ch + ch * (-0.2), 0).click().perform()
        else:
            webdriver.ActionChains(driver).move_to_element(elem).move_by_offset(elem.size['width'] / 100 * ch - ch * 0.2, 0).click().perform()
        Te.test_Move(driver.find_element(By.ID, 'sliderValue').get_attribute('value'), ch)

    def PrBar(self):
        driver.execute_script("window.scrollTo(0, 300)")
        driver.find_element(By.XPATH, '//*[@id="item-4"]/span[text()="Progress Bar"]').click()
        driver.execute_script("window.scrollTo(0, -300)")
        Te.test_PrBar(driver.current_url)

    def Start(self):
        return driver.find_element(By.ID, 'startStopButton').click()

    def Stop(self): #Utils
        elem = driver.find_element(By.XPATH, '//div[@id="progressBar"]/div')
        while True:
            if int(elem.get_attribute('aria-valuenow')) == St.ValueOutput()['age']:
                self.Start()
                break
        Te.test_Stop(elem.get_attribute('aria-valuenow'))

class DatePicker(Alerts):

    def Widgets(self):
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Widgets"]').click()
        driver.find_element(By.XPATH, '//*[@id="item-2"]/span[text()="Date Picker"]').click()
        elem_1 = driver.find_element(By.ID, 'datePickerMonthYearInput')
        elem_2 = driver.find_element(By.ID, 'dateAndTimePickerInput')
        St.ValueStorage('date', 'date', elem_1.get_attribute('value'))
        St.ValueStorage('date', 'datetime', elem_2.get_attribute('value'))
        Te.test_Widgets_2(driver.current_url)

    def DateChoose(self):
        driver.find_element(By.ID, 'datePickerMonthYearInput').click()
        elem = driver.find_element(By.XPATH, '//select[@class="react-datepicker__month-select"]')
        elem.click()
        elem.send_keys("Feb")
        elem.click()
        elem = driver.find_element(By.XPATH, '//select[@class="react-datepicker__year-select"]')
        elem.click()
        elem.send_keys("2024")
        elem.click()
        driver.find_element(By.XPATH, '//div[@aria-label="Choose Thursday, February 29th, 2024"]').click()
        Te.test_DateChoose(driver.find_element(By.ID, 'datePickerMonthYearInput').get_attribute('value'))

class Files(Alerts):

    def Elements(self):
        driver.find_element(By.XPATH, '//div[@class="card-body"]/h5[text()="Elements"]').click()
        driver.execute_script("window.scrollTo(0, 300)")
        driver.find_element(By.ID, 'item-7').click()
        driver.execute_script("window.scrollTo(0, -300)")
        Te.test_UplDown(driver.current_url)

    def Download(self):
        elem = driver.find_element(By.ID, 'downloadButton')
        elem.click()
        Te.test_Download(elem.get_attribute('download'))
        time.sleep(2)

    def Upload(self):
        elem = driver.find_element(By.ID, 'uploadFile')
        elem.send_keys(St.ValueOutput()['path'] + '/' + driver.find_element(By.ID, 'downloadButton').get_attribute('download'))
        elem = driver.find_element(By.ID, 'uploadedFilePath')
        Te.test_Upload(driver.find_element(By.ID, 'downloadButton').get_attribute('download'), elem.text.split('\\'))

Al = Alerts()
If = Iframe()
Ta = Tables()
Ha = Handles()
Sl_Prb = Sl_Prbar()
DP = DatePicker()
Fi = Files()
Al.HomePage()
Al.AlertForm()
Al.ClickAlert()
Al.ClickAlertButton()
Al.ClickConfirmAlert()
Al.ClickAlertConfirmButton()
Al.ClickAlertPromptButton()
Al.RandomText()
If.HomePage()
If.NestedFrames()
If.Frames()
Ta.HomePage()
Ta.ElementsClick()
Ta.ButtonClick()
Ta.TableFilling()
Ta.RowDelete()
Ha.HomePage()
Ha.BrowserWindows()
Ha.NewTab()
Ha.CloseTab()
Ha.Links()
Ha.HomeLink()
Ha.PrevPage()
Sl_Prb.HomePage()
Sl_Prb.Widgets()
Sl_Prb.Move()
Sl_Prb.PrBar()
Sl_Prb.Start()
Sl_Prb.Stop()
DP.HomePage()
DP.Widgets()
DP.DateChoose()
Fi.HomePage()
Fi.Elements()
Fi.Download()
Fi.Upload()
driver.quit()



