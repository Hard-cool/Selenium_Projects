import json
slov = {
'url':  {'homepage': 'https://demoqa.com/', 'nfpage': 'https://demoqa.com/nestedframes', 'wtpage': 'https://demoqa.com/webtables', 'bwpage': 'https://demoqa.com/browser-windows', 'newpage': 'https://demoqa.com/sample', 'lpage': 'https://demoqa.com/links', 'prbpage': 'https://demoqa.com/progress-bar', 'sliderpage': 'https://demoqa.com/slider', 'datepage': 'https://demoqa.com/date-picker', 'uploadpage': 'https://demoqa.com/upload-download'},
'assertation': {'alerttext_1': 'You clicked a button', 'alerttext_2': 'Do you confirm action?', 'alerttext_3': 'You selected Ok', 'alerttext_4': 'Please enter your name', 'alerttext_5': 'You entered '},
'rand': '',
'framepage_1': {'outerframe': '', 'innerframe': ''},
'framepage_2': {'topframe': '', 'bottomframe': ''},
'tablestructure': {'row_0': 'firstName', 'row_1': 'lastname', 'row_2': 'userEmail', 'row_3': 'age', 'row_4': 'salary', 'row_5': 'department'},
'person_1': {'row_1': 'Jon', 'row_2': 'Snow', 'row_3': 'knownothing@gmail.com', 'row_4': '30', 'row_5': '3000', 'row_6': 'alpha'},
'person_2': {'row_1': 'Buttercup', 'row_2': 'Cumbersnatch', 'row_3': 'BudapestCandygram@mail.ru', 'row_4': '41', 'row_5': '2000', 'row_6': 'beta'},
'testvalues': {'outerframe': 'Parent frame', 'innerframe': 'Child Iframe', 'before': '', 'after': ''},
'age': 22,
'date': {'date': '', 'datetime': '', 'month': '02', 'year': '2024', 'day': '29'},
'path': '/home/artem/Downloads',
}

slov_1 = {
'window_size':  {'width': 1400, 'height': 1080},
'browser': 'chrome',
'wait': 3,

}
with open('Utils/config.json', 'w') as f:
    f.write(json.dumps(slov_1))

with open('Utils/config.json') as f:
    l = json.load(f)

with open('Utils/test_data.json', 'w') as f:
    f.write(json.dumps(slov))

with open('Utils/test_data.json') as f:
    l = json.load(f)







