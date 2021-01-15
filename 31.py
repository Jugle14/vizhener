from modules import *
from math import ceil
def encrypt_mod(language, text, key, b, a=1):
    r = len(key)
    output = ''
    alphabet = alphabet_dict[language]
    count_l = count_letter[language]
    i = 0

    doubling = 0
    for letter in text:
        try:
            output += alphabet[(alphabet.index(letter.lower()) + k_i_r_generator(alphabet.index(key[i%r]), a, b, doubling))%count_l]
            i+=1
            if i%r == 0:
                doubling += 1
        except ValueError:
            output += letter

    return output    

def decrypt(raw_text, key, mod=0, b=0):
    text = cleaner_of_rubbish(raw_text)
    n = len(text)
    #finding r

    output_text = ''
    alphabet = alphabet_dict[language]
    index_of_coincidence = index_of_coincidence_lang[language]
    min_delta = 1
    min_ic = 0
    del_array = {}
    min_r = 2
    for r in range(2, 11):  # Natural bounding 
        index_of_coincidence_r = ic_searcher(r, n, text, language, mod, b)

        value_of_delta_ic = abs(index_of_coincidence_r-index_of_coincidence)
        del_array[min_r] = min_ic
        if aim:
            output_text += '\n\n ' + str(min_r) + ' was deleted'
        min_ic = index_of_coincidence_r
        min_delta = value_of_delta_ic
        min_r = r
    if aim:
        output_text += "\n\nminimal index of coincidence by the first method:" + str(min_ic)
        output_text += "\nthe range of minimal delta:" + str(min_r) + '\n'

    # let the next situation be: we've got the right period of key - r

    r = min_r

    res = key_searcher(r, n, text, language, alphabet)

    if aim:
        output_text += "\nThe resulting key is " + res + '\n'
        output_text += '\nNow printing deleted ranges:\n'
    
    for r, min_ic in del_array.items():
        res = key_searcher(r, n, text, language, alphabet)
        if aim:
            output_text += f'For range {r} resulting key is {res}. '
            output_text += f"The value of index of coincidence is {min_ic}.\n"
        elif len(key) == r:
            if key == res:
                data_gather[length_boundary][0] += 1
                break
            else:
                data_gather[length_boundary][1] += 1
                break

    output_array = list(del_array.keys())
    output_array.append(min_r)
    return output_text, output_array

aim = 1

text = ""
while True:
    inp = cleaner_of_rubbish(input("WRITE IT DOWN>>"))
    if inp == "q":
        break
    text += inp

key = input("Write THE KEY DOWN>>")

language = "en"
enc = encrypt_mod(language, text, key, 9)

txt, out = decrypt(text, key, mod=1, b=9)

print(txt, '\n', out)
