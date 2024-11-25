import random

words_list = ['Dog', 'Cow', 'Cat', 'Horse', 'Donkey', 'Tiger', 'Lion', 'Panther', 'Leopard', 'Cheetah', 'Bear',
            'Elephant', 'Polar', 'bear', 'Turtle', 'Tortoise', 'Crocodile', 'Rabbit', 'Porcupine', 'Hare', 'Hen',
            'Pigeon', 'Albatross', 'Crow', 'Fish', 'Dolphin', 'Frog', 'Whale', 'Alligator', 'Eagle', 'Flying',
            'squirrel', 'Ostrich', 'Fox', 'Goat', 'Jackal', 'Emu', 'Armadillo', 'Eel', 'Goose', 'Arctic', 'fox', 'Wolf',
            'Beagle', 'Gorilla', 'Chimpanzee', 'Monkey', 'Beaver', 'Orangutan', 'Antelope', 'Bat', 'Badger', 'Giraffe',
            'Hermit', 'Crab', 'Giant', 'Panda', 'Hamster', 'Cobra', 'Hammerhead', 'shark', 'Camel', 'Hawk', 'Deer',
            'Chameleon', 'Hippopotamus', 'Jaguar', 'Chihuahua', 'King', 'Cobra', 'Ibex', 'Lizard', 'Koala', 'Kangaroo',
            'Iguana', 'Llama', 'Chinchillas', 'Dodo', 'Jellyfish', 'Rhinoceros', 'Hedgehog', 'Zebra', 'Possum',
            'Wombat', 'Bison', 'Bull', 'Buffalo', 'Sheep', 'Meerkat', 'Mouse', 'Otter', 'Sloth', 'Owl', 'Vulture',
            'Flamingo', 'Racoon', 'Mole', 'Duck', 'Swan', 'Lynx', 'Monitor', 'lizard', 'Elk', 'Boar', 'Lemur', 'Mule',
            'Baboon', 'Mammoth', 'Blue', 'whale', 'Rat', 'Snake', 'Peacock']
answer = random.choice(words_list)

word_filled_blank = ""
for _ in range(len(answer)):
    word_filled_blank += "_"

print(answer)
print(word_filled_blank)
word_list = list(word_filled_blank)
player_life = len(answer)
character_positions = []
while word_filled_blank != answer and player_life > 0:
    guess_letter = input("Guess a letter: ")
    if guess_letter in answer:
        for i in range(len(answer)):
            if answer[i] == guess_letter:
                word_list[i] = guess_letter  # Update the blank at each position
        word_filled_blank = "".join(word_list)  # Update the filled blank word
        print("Current word:", word_filled_blank)
    else:
        player_life -= 1
        print(f"Lives remaining: {player_life}")
if word_filled_blank == answer:
    print("You win")
else:
    print("You lose")