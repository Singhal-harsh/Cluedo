import yagmail
import datetime
import json

with open('config.json', 'r') as f:
    params = json.load(f)


def send_answer(receiver, answer):
    now = datetime.datetime.now()
    subject = "Cluedo Game finished at " + str(now.hour) + ":" + str(now.minute)
    body = "Envelope cards are: \n" + answer + "\n\nI hope you enjoyed the game :D"

    yag = yagmail.SMTP("cluedobymail@gmail.com", "Cluedo@1234")
    yag.send(to=receiver, subject=subject, contents=body)


for player in params["players_email"]:
    send_answer(player, params["answer"])
