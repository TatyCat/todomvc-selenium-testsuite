# To Do MVC Selenium Test Suite
## Purpose: 
This Python script is a regression test on a MVC to-do app (https://todomvc.com/examples/angular2)

## Set Up: 
<ul>
<li>Python 3 Installed (https://docs.brew.sh/Homebrew-and-Python) or (https://docs.python-guide.org/starting/install3/osx/)</li>
<li>Homebrew Installed (https://formulae.brew.sh)</li>
<li>Selenium Installed through Homebrew (https://formulae.brew.sh/formula/selenium-server-standalone)</li>
<li>Virtual Environment (https://docs.python-guide.org/dev/virtualenvs/#direnv)</li>
<li>Python Alias in the .bash file ("alias python='python3')</li>
<li>Selenium Drivers Installed for Chrome (https://selenium-python.readthedocs.io/installation.html) (https://sites.google.com/a/chromium.org/chromedriver/downloads) </li>
</ul>

## Run It
- Create a project folder 
- Open up Terminal. 
- Create a virtual enviroment inside the project folder you created (https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/) 
- Clone Project or download code file (https://github.com/TatyCat/todomvc-selenium-testsuite) and save it inside your project folder.
- While in the project folder, use terminal to activate the virtual enviroment you created (ex: "Source venv_name\Scripts> activate" per https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/)
- To run a specific test in the test suite, type in the terminal using the following template:  python HomePg_ToDo_TestSuite.py ToDoMVCTest.<replace with test/method name>
- To run the entire test suite, type in the terminal using the following template: python HomePg_ToDo_TestSuite.py 


***	
### Personal Notes for Tatyanna: 
To ACTIVATE PYTHON ENV:
    cd '/Documents/Code.Eat.Sleep/QA_Scripts/todoApp_Test'
    source todo-env/bin/activate  

Error: "This version of ChromeDriver only supports Chrome version 87"
Solution: Update/Install Selenium - Webdriver
    brew upgrade chromedriver
    python -m pip install pip

Pro Bash tip: <!-- *history* shows last used commands-->

To run independent methods/test: python [fileName] [className.testName]
    Examples: 
    - python HomePg_ToDo_TestSuite.py ToDoMVCTest.test_mark_complete 
    - python test_todomvc.py TestToDoMVC.test_put__text_in_input_box 

