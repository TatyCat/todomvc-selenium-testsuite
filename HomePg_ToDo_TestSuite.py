import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

class ToDoMVCTest(unittest.TestCase):

    def setUp(self):    
        self.driver = webdriver.Chrome()
        self.driver.get('https://todomvc.com/examples/angular2/')
        
        #Wait until input box is available in DOM tree.
            # https://selenium-python.readthedocs.io/waits.html#explicit-waits
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/todo-app/section/header/input')))
        except:
            self.driver.quit()
        
        #Add/type text in input box (not disabled) / #can submit added text to create a checklist item
    def test_text_in_input_box(self):
        input_todo = self.driver.find_element_by_xpath('/html/body/todo-app/section/header/input')
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(15)	
        input_todo.send_keys('test text 2')
        input_todo.send_keys(Keys.ENTER)
        #todo: text found in the loction.


        #checklist item can be marked complete by toggle:
    def test_mark_complete(self):
            # find toggle, mark toggle, check that it shows as complete 
        input_todo = self.driver.find_element_by_xpath('/html/body/todo-app/section/header/input')
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)

        toggle_check = self.driver.find_element_by_xpath('/html/body/todo-app/section/section/ul/li/div/input')

        #verify not selected
        self.assertTrue(not toggle_check.is_selected())
        
        toggle_check.click()
        
        #verify toggle is selected
        self.assertTrue(toggle_check.is_selected())
    
    def test_completion_style_format(self):
        input_todo = self.driver.find_element_by_class_name("new-todo")
        input_todo.send_keys('test completion text')
        input_todo.send_keys(Keys.ENTER)
        mark_complete = self.driver.find_element_by_xpath('/html/body/todo-app/section/section/ul/li/div/input')
        mark_complete.click()
        #check for item by 'complete' class name
        completed_li = self.driver.find_element_by_class_name('completed')
        self.assertTrue(completed_li)
        

    def test_state_refresh(self):
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

          
        # 'X item(s) left' section updates upon completed or incomplete amount of items. Accurate number of 'item(s) left' is displayed.
    def test_items_left_counter(self):
        input_todo = self.driver.find_element_by_class_name("new-todo")
        for x in range(1, 4):
            input_todo.send_keys('test text ' + str(x))
            input_todo.send_keys(Keys.ENTER)
        counter = self.driver.find_element(By.CLASS_NAME,'todo-count')
        self.assertEqual(counter.text, "3 items left")

        #change counter and verify counter updates. 
        mark_complete = self.driver.find_element_by_xpath('/html/body/todo-app/section/section/ul/li/div/input')
        mark_complete.click()
        self.assertEqual(counter.text, "2 items left")
        
        #click input to mark incomplete and verify counter updates. 
        mark_complete.click()
        self.assertEqual(counter.text, "3 items left")

    def test_clear_button(self):
        input_todo = self.driver.find_element_by_class_name('new-todo')
        for x in range(1, 5):
            input_todo.send_keys('test text ' + str(x))
            input_todo.send_keys(Keys.ENTER)

        toggle_complete1 = self.driver.find_element_by_xpath('/html/body/todo-app/section/section/ul/li[1]/div/input')
        toggle_complete2 = self.driver.find_element_by_xpath('/html/body/todo-app/section/section/ul/li[2]/div/input')
        toggle_complete1.click()
        toggle_complete2.click()

        clear_completed = self.driver.find_element_by_class_name('clear-completed')
        clear_completed.click()
        #Verify that two items remain
        counter = self.driver.find_element(By.CLASS_NAME,'todo-count')
        self.assertEqual(counter.text, "2 items left")

    def test_hover_to_remove(self):
        input_todo = self.driver.find_element_by_class_name('new-todo')
        for x in range(0, 3):
            input_todo.send_keys('test item ' + str(x))
            input_todo.send_keys(Keys.ENTER)
            
        li_to_hover = self.driver.find_element_by_xpath('/html/body/todo-app/section/section/ul/li[1]/div/input')

        hover_action = ActionChains(self.driver).move_to_element(li_to_hover)

        x_destroy_element = self.driver.find_element_by_class_name('destroy')

        hover_action.perform()
        x_destroy_element.click()

        counter = self.driver.find_element(By.CLASS_NAME,'todo-count')
        self.assertEqual(counter.text, "2 items left")
           


    def tearDown(self):
        sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()