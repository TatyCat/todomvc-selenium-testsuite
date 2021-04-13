# To Do MVC Selenium Test Suite
##Purpose: 
This Python script is a regression test on the to-do app (https://todomvc.com/examples/angular2)

##Requirements: 
Python 3 
Install Homebrew
Install Selenium through Homebrew

##How to Run: 
Save project folder.
Open up Terminal. 
Change Directory to the project folder location. Example: cd '/Documents/Code_Files/QA_Scripts/todoApp_Test'
Install Python Enviroment.
 Activate the python enviroment  source todo-env/bin/activate  









Personal Notes: 
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

