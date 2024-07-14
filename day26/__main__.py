import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

name = input("What is your name? ").upper()
result = [nato_dict[letter] for letter in name if letter in nato_dict.keys()]

print(result)
