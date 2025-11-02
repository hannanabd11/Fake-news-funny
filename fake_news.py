import random
subjects = [
    "Atlantis ka mayor",
    "moonwalk karte hue raccoons ka tola",
    "Mars ka president",
    "time-travel karta hua librarian",
    "shakli taur pe gym gaya hua kabootar",
    "Einstein ki billi ka bhoot",
    "psychic frogs ki council",
    "Bubble Wrap Inc. ka CEO",
    "Tokyo ka ninja sloth",
    "Candyland ka shahi jellybean"
]

actions = [
    "par pabandi laga di",
    "galti se godh le liya",
    "karaoke muqablay ka chalang diya",
    "raaz dance moves leak kar diye",
    "ek nayi mazhab ki buniyad rakhi",
    "Wi-Fi router samajh liya",
    "orbit mein launch kar diya",
    "TED Talk de di",
    "fashion line shuru kar di",
    "anghoon ka jung kar liya"
]

objects = [
    "radioactive kela",
    "Detroit ka aakhri unicorn",
    "sentient lava lamp",
    "confused GPS system",
    "glitter-powered submarine",
    "haunted vending machine",
    "Paris ka robotic llama",
    "teleport hota hua marshmallow",
    "disco-themed virus",
    "filsoofi aloo"
]

while True:
    subject = random.choice(subjects)
    act = random.choice(actions)
    obj = random.choice(objects)
    print(f'Breaking news: {subject} {act} {obj}')

    choice=input('Do u want another or quit: ').lower()
    if choice=='no':
        print('Thanks for using it')
        break
