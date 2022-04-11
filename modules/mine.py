import pickle
import time
from datetime import datetime
from termcolor import cprint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AlienWorld:
    def __init__(self, ):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Projects\main_project\aw_bot\chromedriver.exe")
        
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
            cprint(f'({datetime.now().strftime("%H:%M:%S")}) Approve Success', 'green')
            self.driver.switch_to.window(self.driver.window_handles[0])

        except:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            cprint(f'({datetime.now().strftime("%H:%M:%S")}) Cant Approve', 'red')

    def click_mine(self):

        # Click Mine
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[4]/div[3]/div[2]/div[2]/div/div/div/div/div/div/span")))
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[4]/div[3]/div[2]/div[2]/div/div/div/div/div/div/span').click()

        # Click Claim Mine
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[4]/div[3]/div[2]/div[2]/div/div/div/div/div/span")))
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[4]/div[3]/div[2]/div[2]/div/div/div/div/div/span').click()