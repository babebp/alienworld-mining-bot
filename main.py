from modules.mine import AlienWorld
import time

if __name__ == "__main__":
    alien = AlienWorld()

    with open('session_token.txt') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        session_token = lines[i]
        alien.login(session_token.strip())

    time.sleep(5)
    alien.all_in_one()