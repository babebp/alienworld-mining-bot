from modules.mine import AlienWorld

if __name__ == "__main__":
    alien = AlienWorld()
    session_token = input('Enter Your Session Token: ')
    alien.login(session_token)