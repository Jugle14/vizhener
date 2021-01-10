frequency_dict = {'en': ['e', 't', 'a', 'o', 'n', 'i', 'r', 's', 'h'], 'ua': ['о', 'а', 'н', 'і', 'и', 'в', 'р', 'т', 'е', 'с', 'к', 'л']}
alphabet_dict = {
    'en': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'ua': ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
}
count_letter = {'en': 26, 'ua': 33}

language = input("Type in the language>")
text = input("Type in text>")
key = input("Type in key>").lower()

r = len(key)
output = ''
alphabet = alphabet_dict[language]
count_l = count_letter[language]
i = 0
b = 1
count_of_cycles = 0
for letter in text:
    try:
        output += alphabet[(alphabet.index(letter.lower()) + alphabet.index(key[i%r])+count_of_cycles*b)%count_l]
        i+=1
        if i%r == 0:
            count_of_cycles+=1
    except ValueError:
        output += letter

print(output)
