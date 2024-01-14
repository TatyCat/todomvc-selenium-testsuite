import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import tracemalloc

# class TestToDoMVC():
class TestToDoMVC(unittest.TestCase):

    def setUp(self):    
        self.browser = webdriver.Firefox()
        self.browser.get("https://todomvc.com/examples/angular2/")
        
        #Wait until input box is available in DOM tree.
            # https://selenium-python.readthedocs.io/waits.html#explicit-waits
        try:
            wait = WebDriverWait(self.browser, timeout=10)
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/todo-app/section/header/input")))
        except TimeoutException as error:
            isrunning = 0
            print("Exception has been thrown. " + str(error))
            self.browser.quit()

        tracemalloc.start()    
        
        #Add/type text in input box (not disabled) / #Can submit added text to create a checklist item
    def test_put__text_in_input_box(self):
        input_todo = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/header/input")
        input_todo.send_keys("test text")
        input_todo.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(15)	
        input_todo.send_keys("test text 2")
        input_todo.send_keys(Keys.ENTER)

        #checklist item can be marked complete by toggle:
    def test_mark_complete(self):
        # find toggle, mark toggle, check that it shows as complete 
        input_todo = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/header/input")
        input_todo.send_keys("test text")
        input_todo.send_keys(Keys.ENTER)

        toggle_check = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li/div/input")

        #verify not selected
        self.assertTrue(not toggle_check.is_selected())
        
        toggle_check.click()
        
        #verify toggle is selected
        self.assertTrue(toggle_check.is_selected())
    
    def test_completion_style_format(self):
        input_todo = self.browser.find_element(By.CLASS_NAME, "new-todo")
        input_todo.send_keys("test completion text")
        input_todo.send_keys(Keys.ENTER)
        mark_complete = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li/div/input")
        mark_complete.click()
        completed_li = self.browser.find_element(By.CLASS_NAME, "completed")
        self.assertTrue(completed_li)
        

    def test_state_refresh(self):
        input_todo = self.browser.find_element(By.CLASS_NAME, "new-todo")
        for x in range(1, 6):
            input_todo.send_keys("test text " + str(x))
            input_todo.send_keys(Keys.ENTER)
            
        # check what data is there (five items)
            # refresh page & wait for page load
        self.browser.refresh()
        pageLoadWait = WebDriverWait(self.browser, timeout=10)
        pageLoadWait.until(EC.presence_of_element_located((By.CLASS_NAME, "toggle")))

        # verify that the number remains the same.
        print(self.browser.find_element(By.CLASS_NAME, "todo-count").text)
        confirmtext = self.browser.find_element(By.CLASS_NAME, "todo-count").text
        print(confirmtext)
        self.assertEqual(confirmtext, "5 items left")
          
        # "X item(s) left" section updates upon completed or incomplete amount of items. Accurate number of "item(s) left" is displayed.
    def test_items_left_counter(self):
        input_todo = self.browser.find_element(By.CLASS_NAME, "new-todo")
        for x in range(1, 4):
            input_todo.send_keys("test text " + str(x))
            input_todo.send_keys(Keys.ENTER)
        counter = self.browser.find_element(By.CLASS_NAME, "todo-count")
        self.assertEqual(counter.text, "3 items left")

        #change counter and verify counter updates. 
        mark_complete = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li/div/input")
        mark_complete.click()
        self.assertEqual(counter.text, "2 items left")
        
        #click input to mark incomplete and verify counter updates. 
        mark_complete.click()
        self.assertEqual(counter.text, "3 items left")

    def test_clear_button(self):
        input_todo = self.browser.find_element(By.CLASS_NAME, "new-todo")
        for x in range(1, 5):
            input_todo.send_keys("test text " + str(x))
            input_todo.send_keys(Keys.ENTER)

        toggle_complete1 = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li[1]/div/input")
        toggle_complete2 = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li[2]/div/input")
        toggle_complete1.click()
        toggle_complete2.click()

        clear_completed = self.browser.find_element(By.CLASS_NAME, "clear-completed")
        clear_completed.click()
        #Verify that two items remain
        counter = self.browser.find_element(By.CLASS_NAME, "todo-count")
        self.assertEqual(counter.text, "2 items left")

    def test_hover_to_remove(self):
        input_todo = self.browser.find_element(By.CLASS_NAME, "new-todo")
        for x in range(0, 3):
            input_todo.send_keys("test item " + str(x))
            input_todo.send_keys(Keys.ENTER)
            
        li_to_hover = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li[1]/div/input")
        ActionChains(self.browser).move_to_element(li_to_hover).perform()
        x_destroy_element = self.browser.find_element(By.CLASS_NAME, "destroy")
        x_destroy_element.click()
        #verify test removed the li 
        counter = self.browser.find_element(By.CLASS_NAME, "todo-count")
        self.assertEqual(counter.text, "2 items left")
           
    def test_double_click_to_edit(self):
        input_todo = self.browser.find_element(By.CLASS_NAME, "new-todo")
        for x in range(0, 3):
            input_todo.send_keys("test item ")
            input_todo.send_keys(Keys.ENTER)

        todo_item = self.browser.find_element(By.CLASS_NAME, "view")
        ActionChains(self.browser).double_click(todo_item).perform()
        edit_item = self.browser.find_element(By.CLASS_NAME, "edit")
        edit_item.clear()

        ActionChains(self.browser).double_click(todo_item).perform()
        edit_item = self.browser.find_element(By.CLASS_NAME, "edit") 

        edit_item.send_keys("Edited List Item")
        edit_item.send_keys(Keys.ENTER)

        #verify that edit occured
        edited_li_text = self.browser.find_element(By.XPATH, "/html/body/todo-app/section/section/ul/li[1]/div/label").get_attribute('innerHTML')
        self.assertEqual(edited_li_text, "Edited List Item", "Double Click to Edit test Failed")
        

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)