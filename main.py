import pandas



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index,row) in data.iterrows()}
print(nato)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
running = True
while running:
        try:
            user_input = input("Enter a word: ").upper()
            output = [nato[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            if user_input == "EXIT":
                running = False
            print(output)


