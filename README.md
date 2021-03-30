To ACTIVATE PYTHON ENV:
    cd '/Documents/Code.Eat.Sleep/QA_Scripts/todoApp_Test'
    source todo-env/bin/activate  

Error: "This version of ChromeDriver only supports Chrome version 87"
Solution: Update/Install Selenium - Webdriver
    brew upgrade chromedriver
    python -m pip install pip

Pro tip: <!-- *history* shows last used commands-->

To run independent methods/test:
    python HomePg_ToDo_TestSuite.py ToDoMVCTest.test_mark_complete 

