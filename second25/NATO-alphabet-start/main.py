import pandas 

with open('nato_phonetic_alphabet.csv') as phonetic:
    data = pandas.read_csv(phonetic)

dict_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    ask_word = input("Enter a word: ").lower()
    if ask_word == "exit":
        return 
    try:
        answer = [dict_phonetic[letter] for letter in ask_word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(answer)
generate_phonetic()
    