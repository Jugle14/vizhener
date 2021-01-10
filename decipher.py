from math import ceil
from modules import cleaner_of_rubbish, ic_searcher, key_searcher, alphabet_dict, n_y_dict_all, count_letter, index_of_c_mod_1, d_r
from json import load
from random import randint
from os import listdir
from sys import exit
from datetime import datetime 

frequency_dict = {'en': ['e', 't', 'a', 'o', 'n', 'i', 'r', 's', 'h'], 'ua': ['о', 'а', 'н', 'і', 'и', 'в', 'р', 'т', 'е', 'с', 'к', 'л']}
alphabet_dict = {
    'en': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'ua': ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
}
count_letter = {'en': 26, 'ua': 33}
start_message = "~~~  STARTING A PROGRAMME  ~~~\n"
index_of_coincidence_lang = {'en': 0.06552, 'ua': 0.05004}
length_boundary = 3000

def encrypt(language, text, key):
    r = len(key)
    output = ''
    alphabet = alphabet_dict[language]
    count_l = count_letter[language]
    i = 0

    for letter in text:
        try:
            output += alphabet[(alphabet.index(letter.lower()) + alphabet.index(key[i%r]))%count_l]
            i+=1
        except ValueError:
            output += letter

    return output

def encrypt_mod_1(language, text, key, b):
    r = len(key)
    output = ''
    alphabet = alphabet_dict[language]
    count_l = count_letter[language]
    i = 0

    doubling = 0
    for letter in text:
        try:
            output += alphabet[(alphabet.index(letter.lower()) + alphabet.index(key[i%r]) + b*doubling)%count_l]
            i+=1
            if i%r == 0:
                doubling += 1
        except ValueError:
            output += letter

    return output    

def decrypt(raw_text, mod=0, b=0):
    text = cleaner_of_rubbish(raw_text)
    n = len(text)
    #finding r

    output_text = ''
    index_of_coincidence = index_of_coincidence_lang[language]
    min_delta = 1
    min_ic = 0
    del_array = {}
    min_r = 2
    for r in range(2, ceil(n/3)-1):  # Natural bounding 
        index_of_coincidence_r = ic_searcher(r, n, text, language, mod, b)

        value_of_delta_ic = abs(index_of_coincidence_r-index_of_coincidence)
        if value_of_delta_ic < min_delta:
            if min_delta/value_of_delta_ic >= 1.5:
                del_array[min_r] = min_ic
                output_text += '\n\n ' + str(min_r) + ' was deleted'
                min_ic = index_of_coincidence_r
                min_delta = value_of_delta_ic
                min_r = r

    output_text += "\n\nminimal index of coincidence by the first method:" + str(min_ic)
    output_text += "\nthe range of minimal delta:" + str(min_r) + '\n'

    # let the next situation be: we've got the right period of key - r

    r = min_r

    res = key_searcher(r, n, text, language)

    output_text += "\nThe resulting key is " + res + '\n'

    output_text += '\nNow printing deleted ranges:\n'
    for r, min_ic in del_array.items():
        res = key_searcher(r, n, text, language)
        output_text += 'For range {r} resulting key is {res}. '.format(**{'r': r, 'res': res})
        output_text += "The value of index of coincidence is {a}.\n".format(**{'a': min_ic})
    
    output_array = list(del_array.keys())
    output_array.append(min_r)
    return output_text, output_array

def decrypt_d_r(raw_text, b=0):
    text = cleaner_of_rubbish(raw_text)
    output_text = ""
    natural_boundary = ceil(len(text)/33)-1

    r_dict = d_r(natural_boundary, text, language, b=b)

    for r, d_r_unit in r_dict.items():
        res = key_searcher(r, len(text), text, language, b=b)
        output_text += f"\nFor range {r} resulting key is {res}. "
        output_text += f"The D_r is {d_r_unit}.\n"
    
    output_array = list(r_dict.keys())
    return output_text, output_array

#
# ~~~ Starting the programme ~~~
#

print(start_message)

language = input("Enter the language: 'en' or 'ua'>>")
if language != "en" and language != "ua":
    print("\nError: write correctly")
    exit()

modification = int(input("Enter number of modification>>"))

start_time = datetime.now()
# Importind list of text files and list of keys
print("\nImporting list of data\n")


list_of_data = listdir('txt_files/'+language)

with open("txt_files/keys/"+language+".txt", 'r', encoding="utf-8") as r:
    list_of_keys = r.read().split()
length_of_list_of_keys = len(list_of_keys)

# Working with every file
for text_file in list_of_data:
    print("Working with "+text_file, "\n")
    start_time_sub = datetime.now()
    with open('txt_files/'+language+'/'+text_file, 'r', encoding="utf-8") as r:
        text_data = r.read()
    
    # Naming logs file
    log_file = 'logs_' + str(modification) + "_" + text_file.replace('.txt', '')
    log_file = 'logs/' + log_file + '.logs'

    number_of_example = 1
    failed_examples = []
    start_point = 0
    end_point = start_point
    continue_point = True
    while continue_point:
        # Registering start time of example's processing
        start_time_exmpl = datetime.now()
        
        # Now making a unit of text , which contains more than 1000 symbols
        start_point = end_point+1

        while (end_point - start_point) < length_boundary:
        
            end_point = text_data.find('.', end_point+1)
        
            if end_point == -1:
                end_point = len(text_data)
                continue_point = False
                break

        unit = text_data[start_point:end_point+1]
        start_point = end_point + 1
        key = list_of_keys[randint(0, length_of_list_of_keys-1)]
        b = randint(1, count_letter[language]-1)

        # encrypting
        if modification == 0:
            encrypted_text = encrypt(language, unit, key)
        elif modification == 1 or modification == 2:
            encrypted_text = encrypt_mod_1(language, unit, key, b)
        
        # length of the text should be at least 2, cuz' of the principal of index's of coincidence formula
        if len(encrypted_text) <= 1:
            pass
        # decrypting
        if modification == 0:
            result_txt, list_of_ranges = decrypt(encrypted_text)
        elif modification == 1:
            result_txt, list_of_ranges = decrypt(encrypted_text, mod=1, b=b)
        elif modification == 2:
            result_txt, list_of_ranges = decrypt_d_r(encrypted_text, b=b)

        # listing failed deciphering
        if not (len(key) in list_of_ranges):
            failed_examples.append(number_of_example)
        
        # Adding some information to output text
        result_txt = "\n\n~~~ " +str(number_of_example) + " ~~~\n" + result_txt
        result_txt += f"\nThe right range of key is {str(len(key))}. The right key is {key}.\n"
        if modification >= 1:
            result_txt += f"The value of b is {str(b)}.\n"
        # Creating log file
        
        with open(log_file, 'a') as w:
            w.write(result_txt+'\n')
        
        # Reporting about time used for each of an example
        print("\nProcessing example №"+str(number_of_example)+" took "+str(datetime.now()-start_time_exmpl))

        number_of_example += 1
    
    # Reporting of failed examples
    if failed_examples != []:
        report = "\n\nFailed Examples are "
        for i in failed_examples:
            report += str(i) + ' '
        with open(log_file, 'a') as w:
            w.write(report)
    
    print("\nProcessing at text file " + text_file + " has cost you " + str(datetime.now()-start_time_sub))
    print("Processing time for now: " + str(datetime.now()-start_time))

# Finishing programme
print("\n\n~~~  FINISHING A PROGRAMME  ~~~")
print("\nThe resulting time is " + str(datetime.now()-start_time))
