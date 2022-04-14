import random
import time  

from datetime import datetime
from termcolor import cprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.support import expected_conditions as EC




class AlienWorld:
    
    def __init__(self, ):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Projects\main_project\aw_bot_\chromedriver.exe")
        
    def login(self, session):    
        self.driver.get("https://all-access.wax.io/")
        time.sleep(10)
        self.driver.add_cookie({"name": "session_token", "value": f"{session}"})
        self.driver.get("https://play.alienworlds.io/")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div/div[1]/div/div/div")))
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div[1]/div/div/div').click()

    def approve(self):
        try:
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/section/div[2]/div/div[5]/button/div")))
            self.driver.find_element(by=By.XPATH, value='/html/body/div/div/section/div[2]/div/div[5]/button/div').click()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def all_in_one(self):
        while True:
            # Click Mine
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div/div/div/div/span")))
                self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div/div/div/div/span').click()
            except:
                pass

            time.sleep(4)

            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div")))
                self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div').click()
            except:
                pass
            
            try:
                self.approve()
            except:
                pass

            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]")))
                self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div[2]').click()

                cprint(f"({datetime.now().strftime('%H:%M:%S')}) Get => {self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div/div[2]').text}", 'green', attrs=['bold'])
                cprint(f"({datetime.now().strftime('%H:%M:%S')}) CPU : {self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[10]/div[1]/div[1]/p[2]').text}", 'green', attrs=['bold'])

            except:
                pass

            print('----------------------------')
            time.sleep(random.randint(10,60))