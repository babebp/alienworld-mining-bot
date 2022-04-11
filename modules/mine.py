import pickle
import time
from selenium import webdriver

class AlienWorld:
    def __init__(self, ):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Projects\main_project\aw_bot\chromedriver.exe")
        
    def login(self, session):    
        self.driver.get("https://all-access.wax.io/")
        time.sleep(10)
        self.driver.add_cookie({"name": "session_token", "value": f"{session}"})
        self.driver.get("https://play.alienworlds.io/")

    def approve(self):
        pass
