import pandas 

with open('nato_phonetic_alphabet.csv') as phonetic:
    data = pandas.read_csv(phonetic)
game = True

while game:
    dict_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
    ask_word = input("Enter a word: ").low()
    if ask_word == "exit":
        game = False
    else:
        answer = [dict_phonetic[letter] for letter in ask_word.upper()]
        print(answer)
    