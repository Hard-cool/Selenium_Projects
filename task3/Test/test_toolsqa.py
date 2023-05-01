from Utils.ConfigUtils import Storage
import pytest
from datetime import datetime
import os
St = Storage()
class Testing():

    def test_HomePage(self, url):
        assert St.ValueOutput()['url']['homepage'] == url

    def test_AlertForm(self, elem):
        assert elem.is_displayed()

    def test_ClickAlert(self, text):
        assert text == St.ValueOutput()['assertation']['alerttext_1']

    def test_ClickConfirmAlert(self, text):
        assert text == St.ValueOutput()['assertation']['alerttext_2']

    def test_ClickAlertConfirmButton(self, text):
        assert text == St.ValueOutput()['assertation']['alerttext_3']

    def test_ClickAlertPromptButton(self, text):
        assert text == St.ValueOutput()['assertation']['alerttext_4']

    def test_RandomText(self, text):
        assert text == St.ValueOutput()['assertation']['alerttext_5'] + St.ValueOutput()['rand']

    def test_NestedFrames(self, url):
        assert url == St.ValueOutput()['url']['nfpage']
        assert St.ValueOutput()['framepage_1']['outerframe'] == St.ValueOutput()['testvalues']['outerframe'] and \
               St.ValueOutput()['framepage_1']['innerframe'] == St.ValueOutput()['testvalues']['innerframe']

    def test_Frames(self):
        assert St.ValueOutput()['framepage_2']['topframe'] == St.ValueOutput()['framepage_2']['bottomframe']

    def test_ElementsClick(self, url):
        assert url == St.ValueOutput()['url']['wtpage']

    def test_ButtonClick(self, elem):
        assert elem

    def test_RowDelete(self):
        assert St.ValueOutput()['testvalues']['before'] > St.ValueOutput()['testvalues']['after']

    def test_BrowserWindows(self, url):
        assert url == St.ValueOutput()['url']['bwpage']

    def test_NewTab(self, url):
        assert url == St.ValueOutput()['url']['newpage']

    def test_CloseTab(self):
        pass # Не знаю как написать без try/except

    def test_Links(self, url):
        assert url == St.ValueOutput()['url']['lpage']

    def test_HomeLink(self, url):
        assert St.ValueOutput()['url']['homepage'] == url

    def test_Widgets_1(self, url):
        assert St.ValueOutput()['url']['sliderpage'] == url

    def test_Move(self, text, ch):
        assert int(text) == 50 + ch

    def test_PrBar(self, url):
        assert St.ValueOutput()['url']['prbpage'] == url

    def test_Stop(self, age):
        assert int(age) - 2 <= St.ValueOutput()['age'] <= int(age) + 2

    def test_Widgets_2(self, url):
        assert St.ValueOutput()['url']['datepage'] == url
        a = str(datetime.strptime(St.ValueOutput()['date']['date'], '%d/%m/%Y'))
        b = str(datetime.strptime(St.ValueOutput()['date']['datetime'], '%B %m, %Y %I:%M %p'))
        c = str(datetime.strftime(datetime.now(), '%Y-%d-%m %H:%M')) + ':00'
        d = str(datetime.strftime(datetime.now(), '%Y-%d-%m')) + ' 00:00:00'
        assert a == d and b == c

    def test_DateChoose(self, date):
        a = str(datetime.strptime(date, '%m/%d/%Y'))
        assert (St.ValueOutput()['date']['year'] + '-' + St.ValueOutput()['date']['month'] + '-' + St.ValueOutput()['date']['day'] + ' 00:00:00') == a

    def test_UplDown(self, url):
        assert St.ValueOutput()['url']['uploadpage'] == url

    def test_Download(self, name):
        a = 0
        for i in os.listdir(St.ValueOutput()['path']):
            a += 1
            if i == name:
                assert True
                break

    def test_Upload(self, file, text):
        assert file == text[2]
