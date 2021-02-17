import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

class ToDoMVCTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):    
        self.driver = webdriver.Chrome()
        self.driver.get('https://todomvc.com/examples/angular2/')
        #Wait until input box is available in DOM tree. This was a previous Error/Break
        # https://selenium-python.readthedocs.io/waits.html#explicit-waits
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/todo-app/section/header/input")))
        except:
            self.driver.quit()
        
    #Add/type text in input box (not disabled)
    def test_text_in_input_box(self):
        input_todo = self.driver.find_element_by_xpath("/html/body/todo-app/section/header/input")
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)




    #can submit added text to create a checklist item
    # def test_submit_text():

    #checklist item can be marked complete only by toggle: body > todo-app > section > section > ul > li > div > input
    # def test_mark_complete():

    #item marked complete has strikethrough on text && is greyed out
    # def test_item_shows_complete():

    #refreshng the page should still leave the same incomplete items displayng prior to refresh
    # def test_save_state_on_refresh():
        # driver.navigate().refresh()

    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print ("We did it Joe...")

if __name__ == '__main__':
    unittest.main()



# Refactor: 


#TODO
# after one () hour of troubleshooting, commit & branch & Ben 