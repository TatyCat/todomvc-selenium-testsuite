import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException

from time import sleep

class ToDoMVCTest(unittest.TestCase):

   
    def setUp(self):    
        self.driver = webdriver.Chrome()
        self.driver.get('https://todomvc.com/examples/angular2/')
        
        #Wait until input box is available in DOM tree. This was a previous Error/Break
        # https://selenium-python.readthedocs.io/waits.html#explicit-waits
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/todo-app/section/header/input")))
        except:
            self.driver.quit()
        
        #Add/type text in input box (not disabled) / #can submit added text to create a checklist item
    def test_text_in_input_box(self):
        input_todo = self.driver.find_element_by_xpath("/html/body/todo-app/section/header/input")
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(15)	
        input_todo.send_keys('test text 2')
        input_todo.send_keys(Keys.ENTER)


    #checklist item can be marked complete only by toggle:
    def test_mark_complete(self):
            # find toggle, mark toggle, check that it shows as complete 

        toggle_check = self.driver.find_element_by_xpath("/html/body/todo-app/section/section/ul/li/div/input")
        toggle_check.click()
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "toggle" )))            
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#toggle" )))
           
        
        if toggle_check.is_selected():
            print('test_mark_complete SELECTED')

    
    # ERROR MESSAGE: 
    #     Traceback (most recent call last):
    #     line 40, in test_mark_complete
    #        toggle_check = self.driver.find_element_by_xpath("/html/body/todo-app/section/section/ul/li/div/input")
    #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 394, in find_element_by_xpath
    #         return self.find_element(by=By.XPATH, value=xpath)
    #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 976, in find_element
    #         return self.execute(Command.FIND_ELEMENT, {
    #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    #         self.error_handler.check_response(response)
    #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    #         raise exception_class(message, screen, stacktrace)

    #     selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/todo-app/section/section/ul/li/div/input"}
    #     (Session info: chrome=89.0.4389.82)





    
    # @classmethod
    def tearDown(self):
        # self.driver.implicitly_wait(15)	
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



# Refactor TODO: 
    # switch out xpath for different selector

#REMINDER
# after one (1) hour of troubleshooting, branch, commit & @ Ben 
# """&& @ BEN, I keep receiving this error: 

#   """