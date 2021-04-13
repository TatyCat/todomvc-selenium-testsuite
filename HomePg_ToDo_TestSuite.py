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
        input_todo = self.driver.find_element_by_class_name("new-todo")
        input_todo.send_keys('test completion text')
        input_todo.send_keys(Keys.ENTER)
        mark_complete = self.driver.find_element_by_xpath("/html/body/todo-app/section/section/ul/li/div/input")
        mark_complete.click()
        #check for item by 'complete' class name
        completed_li = self.driver.find_element_by_class_name("completed")
        self.assertTrue(completed_li)
        

    def state_refresh(self):
        input_todo = self.driver.find_element_by_class_name("new-todo")
        for x in range(1, 6):
            input_todo.send_keys('test text ' + str(x))
            input_todo.send_keys(Keys.ENTER)
            
        # check whats there
        before_refresh = len(self.driver.find_elements(By.CLASS_NAME, 'toggle'))
        # refresh page
        self.driver.refresh()
        # verify that the number remains the same.
        post_refresh = len(self.driver.find_elements(By.CLASS_NAME, 'toggle'))
        self.assertEqual(before_refresh, post_refresh)

          # 'X item(s) left' section updates 
    def items_left_counter(self):
        input_todo = self.driver.find_element_by_class_name("new-todo")
        for x in range(1, 4):
            input_todo.send_keys('test text ' + str(x))
            input_todo.send_keys(Keys.ENTER)
            # I LEFT OFF: trying to locate the text of 'items left' to verify the number based on toggles
        counter = self.driver.find_element(By.CLASS_NAME,'todo-count//*[text()=" items left"]')
        print(counter)

        # 'X item(s) left' section updates upon completed or incomplete amount of items
        


# WHY DOES CHROME CLOSE ON ITS OWN EVEN WHEN TEARDOWN ISN'T THERE? 
    def tearDown(self):
        sleep(15)
        # self.driver.implicitly_wait(15)	
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



# Refactor TODO: 
    # switch out xpath for different selector
