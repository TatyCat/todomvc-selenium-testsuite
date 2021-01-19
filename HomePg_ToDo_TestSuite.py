from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unittest

class ToDoMVCTest(unittest.TestCase):
    @classmethod
    def setUP(self):    
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window
        self.driver.get('https://todomvc.com/examples/angular2/')
        
    #Add/type text in input box (not disabled)
    def test_text_in_input_box(self):

    #can submit added text to create a checklist item
    def test_submit_text():

    #checklist item can be marked complete only by toggle: body > todo-app > section > section > ul > li > div > input
    def test_mark_complete():

    #item marked complete has strikethrough on text && is greyed out
    def test_item_shows_complete():

    #refreshng the page should still leave the same incomplete items displayng prior to refresh
    def test_save_state_on_refresh():
    
    @classmethod
    def tEARDOWN(cls):
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()

