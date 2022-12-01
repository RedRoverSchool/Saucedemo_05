[![GitHub Actions saucedemo](https://github.com/ivanovajulika/RedRover/actions/workflows/action.yml/badge.svg)](https://github.com/Elvorob/Saucedemo/actions)
# ***SAUCEDEMO***

[Web-Site]👉
[<img src="https://www.saucedemo.com/static/media/Login_Bot_graphic.20658452.png" width="120" height="120">](https://www.saucedemo.com/)
[OUR]👉
[<img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/trello_logo_icon_168452.png" width="115" height="70">](https://trello.com/b/kW09yTkM/practice-letsdoit-group)

# Table of contents
- [Как работать с репозиторием?](#some-inst)
- [Pytest INFO](#some-pytest)
- [Poetry](#some-poetry)
- [Python html report](#some-html)
- [Allure](#some-allure)
- [Creat Allure single HTML file builder](#some-allure-html-file)
- [Useful links](#some-links)
___

# **Как работать с репозиторием?:** <a name="some-inst"></a>
<img src="https://www.press-store.net/_pu/0/29765718.jpg" width="60" height="60"> 

👉[Ссылка на инструкцию](https://docs.google.com/document/d/1-eqVnOTsdPmREaV7frzYSc0VGnU-3FhHAfutOBCzdCw/edit?usp=sharing)

# Pytest INFO:<a name="some-pytest"></a> [![pytest](https://img.shields.io/badge/pytest-website-brightgreen.svg?style=flat-square)](https://docs.pytest.org/en/7.2.x/)

> ***Do not forget check your tests with black and flake8 befor pushing***

### **pytest flags**
    -s - prints desired output (pytest -s test_file_name)
    
    -v - shows test process' percentage (pytest -v test_file_name)
    
    -m - allows to run tests with specific marks (pytest -m mark_title test_file_name)

### **pytest-xdist**

##### *Запускает несколько тестов одновременно* 

    pytest -n auto OR pytest -n 5( any number)
    
⬆️(back to [Menu](#table-of-contents))
___
# POETRY<a name="some-poetry"></a> 
#### WEB с дополнительной информацией &middot;[![poetry](https://img.shields.io/badge/poetry-website-brightgreen.svg?style=flat-square)](https://python-poetry.org/docs/)
  
### *Running all tests in the project with poetry:*
  
    poetry run pytest 
  
### *Running test by name with poetry:*
  
    poetry run pytest test_name.py 
  
### *Shou setups and PASSED/FAILED^*
  
    poetry run pytest test_name.py --setup-show -sv 
    
⬆️(back to [Menu](#table-of-contents))
___
# PYTHON_HTML_REPORT <a name="some-html"></a>
#### WEB с дополнительной информацией &middot;[![pytest-html](https://img.shields.io/badge/pyhtml-website-brightgreen.svg?style=flat-square)](https://pytest-html.readthedocs.io/en/latest/user_guide.html)
### ***Installation:***
    pip install pytest-html

### *How add python-html reports*:
  
    poetry add pytest -html

### ***Start:***
  
    poetry run pytest <your_test_name.py> --html=report/report.html --self-contained-html
    
##### right click to file > open in browser or in finder  
##### report.html - the name of the file, it can be anything

⬆️<sup>(back to [Menu](#table-of-contents))</sup>
___
# ALLURE <a name="some-allure"></a>
#### WEB с дополнительной информацией &middot;[![WEB-SITE](https://img.shields.io/badge/allure-website-brightgreen.svg?style=flat-square)](https://docs.qameta.io/allure/#_pytest)

### ***Installation:***
    pip install allure-pytest
    pip install allure-combine
  
### ***1. Create allure:***
  
###### Соберёт отчеты по всем тестам:
  
    pytest --alluredir=allure
  
###### Соберёт отчет по  указанному тесту:
  
    pytest имя теста --alluredir=allure
  
### ***2. Generates a report and opens it in a browser::***
     
    allure serve allure
      
### ***3. Report generated for allure-report:***
  
    allure generate <директория где лежит отчет>
  
### ***4. Create single HTML report:***<a name="some-allure-html-file"></a>
-создает файл с отчетом `complete.html`(можно делиться с другими) 
  
    allure-combine ./allure-report
  
-delete  `sinon.js` и `server.js`
  
### ***Open allure report:***
  
    allure open <directory>  

### ***Clean allure report:***
  
    allure report clean 

### ***Change directory:***

    allure generate old directory-o new directory
___
# Useful links <a name="some-links"></a>

👉[Установка Black](https://pypi.org/project/black/)

👉[Установка Flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart)

👉[About SELENIUM](https://selenium-python.readthedocs.io/)

👉[About SELENIUM.2](https://www.selenium.dev/documentation/)

👉[About Python](https://www.python.org/)

👉[Allure-combine](https://pypi.org/project/allure-combine/)


⬆️ <sup>(back to [Menu](#table-of-contents))</sup>