import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ToDoMVCTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):    
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(15)
        self.driver.get('https://todomvc.com/examples/angular2/')
        print('----setupclass done!')
        
    #Add/type text in input box (not disabled)
    def test_text_in_input_box(self):
        input_todo = self.driver 
        
        input_todo.find_element_by_css_selector('input.new-todo')
        input_todo.sendKeys('test text')
        input_todo.submit()
            # assert True

        print('----test_text_in_input_box done!')





    #can submit added text to create a checklist item
    # def test_submit_text():

    #checklist item can be marked complete only by toggle: body > todo-app > section > section > ul > li > div > input
    # def test_mark_complete():

    #item marked complete has strikethrough on text && is greyed out
    # def test_item_shows_complete():

    #refreshng the page should still leave the same incomplete items displayng prior to refresh
    # def test_save_state_on_refresh():
        # driver.navigate().refresh()

    
    # @classmethod
    # def tearDownClass(cls):
    #     # cls.driver.quit()
    #     print ("yea")

if __name__ == '__main__':
    unittest.main()

