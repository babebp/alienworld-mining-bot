from modules.mine import AlienWorld
import time

if __name__ == "__main__":
    alien = AlienWorld()
    session_token = input('Enter Your Session Token: ')
    alien.login(session_token)

    time.sleep(5)
    alien.all_in_one()