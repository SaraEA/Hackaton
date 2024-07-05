from speech import speech
from random import choice, randint
import time

niveles = {
    "1" : ["hello", "boys", "chair", "bottle", "reuse", "hat", "dog", "girl"],
    "2": ["schedule", "headphones", "fork", "sheet", "water", "house", "lights", "magic"],
    "3":["headlight", "accessory", "athlete", "candidate", "clothes", "deteriorate", "garbage", "language"],
    "4": ["acknowledge","architecture","atmosphere","acidification","deforestation","greenhouse effect","awkward","characteristics"]
}

def play_game(nivel):
    word = niveles.get(nivel,[])
    print(word)
    print(nivel)
    random_word = choice(word)
    return random_word

def compara(random_word, respuesta):
    if random_word.lower() == respuesta.lower():
        if respuesta in ["bottle","reuse", "water", "lights", "deteriorate", "garbage", "deforestation", "greenhouse effect"]:
            return 2
        else:
            return 1
    else:
        return 0
    
def get_nivel(nivel):
    word = niveles.get(nivel,[])
    return len(word)

