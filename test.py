from modules import n_y_dict_all, index_of_c, alphabet_dict

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
language = "en"
def k_i_r_generator(k_i, a, b, doubling):
    if a == 1:
        return k_i + b*doubling
    else:
        res = 0
        for n in range(doubling):
            res += a**n
        res *= b
        res += (a**doubling)*k_i
        return res

a, b = 130, 1
c_lang = 26
excepted = []
'''
for n in range(10):
    n_dict = {}
    repeating = 0
    for letter in alphabet:
        result_of_generating = k_i_r_generator(alphabet.index(letter), a, b, n)%c_lang
        if result_of_generating in n_dict.values():
            repeating += 1
        n_dict[letter] = result_of_generating

    if repeating > 0:
        excepted.append(n)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(n_dict, "\n", repeating, "\n")
print(excepted)
'''

def encrypt_mod(text, key, b, a=1):
    r = len(key)
    output = ''
    count_l = 26
    i = 0
    doubling = 0
    mod_array = []
    for letter in text:
        try:
            adder = k_i_r_generator(alphabet.index(key[i%r]), a, b, doubling)%count_l
            mod_array.append(adder)
            output += alphabet[(alphabet.index(letter.lower()) + adder)%count_l]
            i+=1
            if i%r == 0:
                doubling += 1
        except ValueError:
            output += letter
    return output, mod_array[::6]

def cleaner_of_rubbish(text):
    res = ''
    for i in text:
        if i.lower() in alphabet_dict['en']+alphabet_dict['ua']:    # ATTENTION
            res += i.lower()
    return res

text = ""
while True:
    inp = cleaner_of_rubbish(input("WRITE IT DOWN>>"))
    if inp == "q":
        break
    text += inp

key = input("Write THE KEY DOWN>>")

enc, mod_array = encrypt_mod(text, key, b, a)

print(enc)
print("\n", index_of_c(enc, language))

# pretend here is a method to find the right length of the key
right_r = len(key)
y_text = []
r_dict = {}
ic_lang = 0.06552
for i in range(right_r):
    y_text.append(enc[i::right_r])



for j in range(right_r):
    block_of_text = y_text[j]
    r_dict[j] = {}
    min_delta = 1    
    for letter_number in range(c_lang):
        modified = letter_number
        deciphered_text = alphabet[(alphabet.index(block_of_text[0])-modified)%c_lang]
        modified_array = [modified]
        for i in range(1, len(block_of_text)):
            modified = k_i_r_generator(modified, a, b, 1)%c_lang
            modified_array.append(modified)
            deciphered_text += alphabet[(alphabet.index(block_of_text[i]) - modified)%c_lang]

        ic_now = index_of_c(deciphered_text, language)
        delta_now = abs(ic_now-ic_lang)
        if delta_now < 0.005:
            r_dict[j][alphabet[letter_number]] = ic_now

print(r_dict)

