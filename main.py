from modules.mine import AlienWorld

if __name__ == "__main__":
    alien = AlienWorld()
    session_token = input('Enter Session Token: ')
    alien.login(session_token)