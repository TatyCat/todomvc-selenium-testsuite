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
        
        #Add/type text in input box (not disabled) / #can submit added text to create a checklist item
    def test_text_in_input_box(self):
        input_todo = self.driver.find_element_by_xpath("/html/body/todo-app/section/header/input")
        input_todo.send_keys('test text')
        input_todo.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(15)	
        input_todo.send_keys('test text 2')
        input_todo.send_keys(Keys.ENTER)

        # if test test is present: print success! 
        # @BEN Should I print out status of each method/test? && having an error

        # if self.driver.find_element_by_link_text("test text"):
        #     print ("Condition SUCCESS: Add/type text in input box (not disabled)")
        # else:
        #     print("FAILURE: test_text_in_input_box")
            # '''
            # Traceback (most recent call last):
            #     File "/Users/luckytaty/Documents/Code.Eat.Sleep/QA_Scripts/todoApp_Test/HomePg_ToDo_TestSuite.py", line 37, in test_text_in_input_box
            #         if self.driver.find_element_by_link_text("test text"):
            #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 428, in find_element_by_link_text
            #         return self.find_element(by=By.LINK_TEXT, value=link_text)
            #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 976, in find_element
            #         return self.execute(Command.FIND_ELEMENT, {
            #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
            #         self.error_handler.check_response(response)
            #     File "/usr/local/lib/python3.9/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
            #         raise exception_class(message, screen, stacktrace)
            #     selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"link text","selector":"test text"}
            #     (Session info: chrome=88.0.4324.150)
            # '''



    #checklist item can be marked complete only by toggle:
    def test_mark_complete(self):
            # find toggle, mark toggle, check that it shows as complete 
        timeout = 15
        self.driver.implicitly_wait(15)	

        try:
            # attemtps to locate:
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li#toggle" )))
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "toggle" )))
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "toggle" )))            
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#toggle" )))
            # toggle_check = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#toggle" )))
            # toggle_check = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.toggle")))
            # toggle_check = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input:contains('test text')")))
            toggle_check2 = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/todo-app/section/section/ul/li/div/input")))


            # todo-app > section > section > ul > li > div > input / css=tag#id
            # css=tag:contains("inner text")


            # toggle_check.click()
        except TimeoutException:
            print("Failed to locate toggle checkbox")

        # toggle_check.click()
        # if toggle_check.is_selected():
            # print('test_mark_complete SELECTED')
                # driver.find_element_by_id("firefox").get_attribute("checked")




    #item marked complete has strikethrough on text && is greyed out
    # def test_item_shows_complete():

    #refreshng the page should still leave the same incomplete items displayng prior to refresh
    # def test_save_state_on_refresh():
        # driver.navigate().refresh()

    
    @classmethod
    def tearDownClass(self):
        self.driver.implicitly_wait(15)	
        # print (" We did it Joe...")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



# Refactor TODO: 
    # switch out xpath for different selector

#REMINDER
# after one (1) hour of troubleshooting, branch, commit & @ Ben 
# """@BEN, I keep receiving this error: 

#   """