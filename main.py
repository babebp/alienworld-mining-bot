from modules.mine import AlienWorld
import random
import time

if __name__ == "__main__":
    alien = AlienWorld()
    session_token = input('Enter Your Session Token: ')
    alien.login(session_token)
    while True:
        time.sleep(240 + random.randint(10,60))