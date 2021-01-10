from json import load
from copy import deepcopy
alphabet_dict = {
    'en': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'ua': ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
}
alphabet = alphabet_dict['en']
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

count_letter = {'en': 26, 'ua': 33}


def index_of_c(text, language):
    global n_y_dict_all
    n_y_dict = deepcopy(n_y_dict_all[language])
    n = len(text)

    for letter in text:
        if letter in alphabet:
            n_y_dict[letter] += 1
    sum_of_n_y = 0
    for letter, count in n_y_dict.items():
        if count > 1:
            sum_of_n_y += count*(count-1)
    return sum_of_n_y/(n*(n-1))

def index_of_c_mod_1(text, language, b):
    global n_y_dict_all
    n_y_dict = deepcopy(n_y_dict_all[language])
    n = len(text)
    for letter in text:
        if letter in alphabet:
            n_y_dict[letter] += 1
    sum_of_n_y = 0
    c_lang = count_letter[language]
    values = list(n_y_dict.values())
    for i in range(0, c_lang):
        sum_of_n_y += values[i]*values[(i+b)%c_lang]
    return sum_of_n_y/(n*(n-1))

def size_normalizer(data_dict):
    new_dict = {'en': {}, 'ua': {}}
    for k in new_dict.keys():
        for key, value in data_dict[k].items():
            new_dict[k][key.lower()] = value
    return new_dict

def m_func(g, text_dict, frequency_dict, number_of_letters):
    m_sum = 0
    for t in range(0, number_of_letters):
        p = frequency_dict[alphabet[t]]
        m_sum += p*text_dict[alphabet[(t+g)%number_of_letters]]
    return m_sum

def cleaner_of_rubbish(text):
    res = ''
    for i in text:
        if i.lower() in alphabet_dict['en']+alphabet_dict['ua']:    # ATTENTION
            res += i.lower()
    return res

def ic_searcher(r, n, text, language, mod, b=0):
    text_arr = []
    index_of_coincidence_r = 0
    for _ in range(0, r):
        text_arr.append('')
    
    c = -1
    for i in range(0, n):
        letter = text[i]
        if letter in alphabet:
            c += 1
            text_arr[c%r] += letter
    
    if mod == 0:
        for i in range(0, r):
            index_of_coincidence_r += index_of_c(text_arr[i], language)
    elif mod == 1:
        for i in range(0, r):
            index_of_coincidence_r += index_of_c_mod_1(text_arr[i], language, b)
    
    index_of_coincidence_r /= r

    return index_of_coincidence_r

def key_searcher(r, n, text, language, b=0):
    text_arr = []
    for _ in range(0, r):
        text_arr.append('')
    c = -1
    doubling = -1
    for i in range(0, n):
        letter = text[i]
        c += 1
        if c%r == 0:
            doubling += 1
        text_arr[c%r] += alphabet[(alphabet.index(letter)-doubling*b)%count_letter[language]]
    min_text_arr = text_arr

    with open("data.json") as r:
        frequency_dict = size_normalizer(load(r))[language]

    res = ''
    number_of_letters = count_letter[language]
    for y_i in min_text_arr:
        m_const = 0
        y_i_dict = deepcopy(n_y_dict_all[language])
        for key in y_i_dict:
            y_i_dict[key] = y_i.count(key)
        for g in range(0, number_of_letters):
            m_now = m_func(g, y_i_dict, frequency_dict, number_of_letters)
            if m_now > m_const:
                m_const = m_now
                g_const = g
        
        res += alphabet[g_const]
    
    return res

def diffrence_counting(text1, text2):
    points = 0
    length_1 = len(text1)
    length_2 = len(text2)

    for i in range(0, length_2):
        if text1[i%length_1] == text2[i]:
            points += 1
    
    return points/length_2

def d_r(r_boundary, text, language, right_r=2, b=0):
    alphabet = alphabet_dict[language]
    text_numbers = []
    c_lang = count_letter[language]
    r_dict = {}
    n = len(text)

    for letter in text:
        text_numbers.append(alphabet.index(letter))
    
    d_r_best = 0
    r_best = -1
    
    for r in range(2, r_boundary+1):
        # here is calculating d_r
        d_r_now = 0
        for i in range(n-r):
            if (text_numbers[i] + b)%c_lang == (text_numbers[i+r]):
                d_r_now += 1

        # here is deciding best r:
        if d_r_now >= int(d_r_best*1.2) or r == right_r:
            if r_best != -1:
                r_dict[r_best] = d_r_best
            d_r_best = d_r_now
            r_best = r
    
    r_dict[r_best] = d_r_best

    return r_dict
