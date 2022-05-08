import itertools
import random
from urllib3.connectionpool import xrange
from sendMail import send_cards
import json
import copy

with open('config.json', 'r') as f:
    params = json.load(f)

original_config = copy.deepcopy(params)


def play_cluedo(number_of_players: int, players_email: str) -> list:
    answer = [params["suspects"].pop(random.randint(0, 5)), params["weapons"].pop(random.randint(0, 5)),
              params["rooms"].pop(random.randint(0, 8))]
    all_cards = [x for x in itertools.chain(params["suspects"], params["weapons"], params["rooms"])]
    random.shuffle(all_cards)
    division = len(all_cards) / float(number_of_players)
    player_cards = [all_cards[int(round(division * i)): int(round(division * (i + 1)))] for i in
                    xrange(number_of_players)]
    for player_no in range(number_of_players):
        send_cards(players_email[player_no], player_cards[player_no])

    return answer


original_config["answer"] = ",".join(play_cluedo(params["number_of_players"], params["players_email"]))
with open("config.json", "w") as outfile:
    json.dump(original_config, outfile, indent=4)
