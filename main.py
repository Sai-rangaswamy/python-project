import logging
import sys
from logging import exception

import game_data
import random
import art


# Create a logger object
log = logging.getLogger()
log.setLevel(logging.ERROR)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


log.info(game_data.data)
try:
    def main(list):
        name_ = list["name"]
        description_ = list["description"]
        country = list["country"]
        return f"{name_} is {description_} from {country}"
except Exception as e:
    log.error(f"Error occured in Main list exception is {e}")

def winning(user,a_score,b_score):
    log.debug(a_score)
    log.debug(b_score)
    log.debug(user)
    log.debug(user=="a")
    log.debug(user=="b")

    if a_score > b_score:
        return user == "a"
    else:
        return user == "b"

userScore = 0
print(art.logo)
gameContinue = True
bList = random.choice(game_data.data)

while gameContinue:
    aList = bList
    bList = random.choice(game_data.data)

    if aList == bList:
        bList = random.choice(game_data.data)

    print("Compare A",main(aList))
    print(art.vs)
    print("Against B",main(bList))
    userValue = input("Enter who has more followers A or B:- ").lower()

    aScore = aList["follower_count"]
    bScore = bList["follower_count"]

    log.debug(f"A value {aScore}")
    log.debug(bScore)
    if winning(userValue,aScore,bScore):
        userScore += 1
        print(f"you're correct!!,your score is{userScore}")

    else:
        print(f"You lost your score is {userScore}")
        gameContinue = False

