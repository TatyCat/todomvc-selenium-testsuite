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
        
        #Wait until input box is available in DOM tree.
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
        #todo: text found in the loction.


        #checklist item can be marked complete by toggle:
    def test_mark_complete(self):
            # find toggle, mark toggle, check that it shows as complete 
        input_todo = self.driver.find_element_by_xpath("/html/body/todo-app/section/header/input")
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)

        toggle_check = self.driver.find_element_by_xpath("/html/body/todo-app/section/section/ul/li/div/input")

        #verify not selected
        self.assertTrue(not toggle_check.is_selected())
        
        toggle_check.click()
        
        #verify toggle is selected
        self.assertTrue(toggle_check.is_selected())
    

    def test_completion_style_format(self):
        input_todo = self.driver.find_element_by_xpath("/html/body/todo-app/section/header/input")
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)
        mark_complete = self.driver.find_element_by_xpath("/html/body/todo-app/section/section/ul/li/div/input")
        mark_complete.click()
        #check for item by 'complete' class name
        completed_li = self.driver.find_element_by_class_name("completed")

        
    
# ASSERTequals, one for each li 



# WHY DOES CHROME CLOSE ON ITS OWN EVEN WHEN TEARDOWN ISN'T THERE? 
    # def tearDown(self):
        # self.driver.implicitly_wait(15)	
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()



# Refactor TODO: 
    # switch out xpath for different selector

#REMINDER
# after one (1) hour of troubleshooting, branch, commit & @ Ben 
# """&& @ BEN, I keep receiving this error: 
#   """