"""Module which return the messages of Grandpy Bot
"""
import random

ADRESS_MGS = [
    "Ah mais bien sûr voilà l'adresse :",
    "De mémoire ça se trouve là :",
    "Ca remonte mais je crois me rappeler que c'était ici :",
]

SUMMARY_MGS = [
    "J'ai une histoire qui me vient en tête... ",
    "Je crois me rappeler que... ",
    "Assis-toi un instant, je vais te raconter une petite histoire... ",
]

FAILURE_MGS = [
    "Je ne comprends rien à ton language de jeune, écris moi correctement français !",
    "Je ne connais rien sur ça, est-ce que tu es sûr de ce que tu as écrit ?"
]


def return_failure():
    message = random.choice(FAILURE_MGS)
    return message


def return_address(address):
    random_msg = random.choice(ADRESS_MGS)
    message = "{} -{}".format(random_msg, address)
    return message


def return_story(summary):
    random_msg = random.choice(SUMMARY_MGS)
    message = "{} {}...".format(random_msg, summary)
    return message
