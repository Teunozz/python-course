from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(direction, text, shift):
    if direction == "decode":
        shift *= -1

    result = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter) + shift
            if index > len(alphabet) - 1:
                index = index % len(alphabet)

            if index < len(alphabet) * -1:
                index = index % (len(alphabet) * -1)

            result += alphabet[index]
        else:
            result += letter

    print(result)


print(logo)


def run_ceasar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(direction, text, shift)


run_ceasar()
while input("Type 'yes' if you want to go again. Otherwise type 'no'.") == "yes":
    run_ceasar()
