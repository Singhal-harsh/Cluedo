import yagmail
import datetime


def send_cards(receiver, player_cards_list):
    player_cards = ",".join(player_cards_list)
    now = datetime.datetime.now()
    subject = "Lets play Cluedo, Game starting at " + str(now.hour) + ":" + str(now.minute)
    body = "Your cards are: " + player_cards + "\nLink for markup and detective analysis to solve the crime: " \
                                               "\nhttps://public-library.safetyculture.io/products/my-cluedo"

    yag = yagmail.SMTP("cluedobymail@gmail.com", "Cluedo@1234")
    yag.send(to=receiver, subject=subject, contents=body)

