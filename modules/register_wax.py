from re import I
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.support import expected_conditions as EC

import time

class Register:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Projects\main_project\aw_bot_\chromedriver.exe")
        self.google_icon = "/html/body/div[1]/div/div/div/div[4]/div[1]/div[2]/button/div/img"
        self.use_other_email = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[3]/div"
        self.next_1 = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"
        self.email_input = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
        self.next_2 = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]"
        self.password_input = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
        self.term_1 = "/html/body/div[1]/div/section/div[2]/section/form/label[1]/span[2]/span"
        self.term_2 = "/html/body/div[1]/div/section/div[2]/section/form/label[2]/span[2]/span"
        self.accept_continue = "/html/body/div[1]/div/section/div[2]/section/form/div/button/div"
        self.copy_address_wax = "/html/body/div/div/section/div[2]/div[2]/div[4]/div[5]/div[2]/div[1]/div/div/button/div"
        self.copy_memo_wax = "/html/body/div/div/section/div[2]/div[2]/div[4]/div[5]/div[2]/div[2]/div/div/button/div"

