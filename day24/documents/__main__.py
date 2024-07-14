with open("input/names/invited_names.txt") as names_file:
    names = [line.strip() for line in names_file.readlines()]

with open("input/letters/starting_letter.txt") as letter_file:
    content = letter_file.read()

for name in names:
    personal_letter = content.replace("[name]", name)
    with open(f"output/ready_to_send/letter_{name.lower().replace(' ', '_')}.txt", mode="w") as personal_file:
        personal_file.write(personal_letter)
