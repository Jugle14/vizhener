frequency_dict = {'en': ['e', 't', 'a', 'o', 'n', 'i', 'r', 's', 'h'], 'ua': ['о', 'а', 'н', 'і', 'и', 'в', 'р', 'т', 'е', 'с', 'к', 'л']}
alphabet_dict = {
    'en': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'ua': ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
}
count_letter = {'en': 26, 'ua': 33}
n_y_dict_all = {
    'en':{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
        'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
        'w': 0, 'x': 0, 'y': 0, 'z': 0
        },
    'ua':{'а': 0, 'б': 0, 'в': 0, 'г': 0, 'ґ': 0, 'д': 0, 'е': 0, 'є': 0, 'ж': 0, 'з': 0, 'и': 0,
        'і': 0, 'ї': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0,
        'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ь': 0, 'ю': 0, 'я': 0
        }
}

def index_of_c(n_y_dict, n, text):
    for letter in text:
        if letter in alphabet:
            n_y_dict[letter] += 1
    sum_of_n_y = 0
    for letter, count in n_y_dict.items():
        if count > 1:
            sum_of_n_y += count*(count-1)
    return sum_of_n_y/(n*(n-1))


language = input("Type in the language>")
text = input("Type in your encrypted text>")

n = len(text)
alphabet = alphabet_dict[language]
#finding r

index_of_coincidence = index_of_c(n_y_dict_all[language].copy(), n, text)
r = 2

while True:
    index_of_coincidence_arr = []
    text_arr = []
    for _ in range(0, r):
        text_arr.append('')
        index_of_coincidence_arr.append(0)
    
    c = -1
    for i in range(0, n):
        letter = text[i]
        if letter in alphabet:
            c += 1
            text_arr[c%r] += letter
    
    if r <= 5:
        for i in range(0, r):
            y_i = text_arr[i]
            index_of_coincidence_arr[i] = index_of_c(n_y_dict_all[language].copy(), n, y_i)
        
        index_of_coincidence_r = sum(index_of_coincidence_arr)
        print(index_of_coincidence, index_of_coincidence_r, '\n')

    #searching of delta
    if r >= 6:
        delta_r = 0
        for i in range(0, r-1):
            text_1, text_2 = text_arr[i], text_arr[i]
            for j in range(0, len(text_2)):
                if text_1[j] == text_2[j]:
                    delta_r += 1
        print(delta_r)
    r += 1
    if r == 11:
        break
