if __name__ == "__main__":
    from math import ceil
    from modules import cleaner_of_rubbish, ic_searcher, key_searcher, alphabet_dict, n_y_dict_all, count_letter, diffrence_counting

    index_of_coincidence_lang = {'en': 0.06552, 'ua': 0.05005}

    language = input("Type in the language>")

    while True:
        raw_text = input("Type in your encrypted text>")
        right_key_length = int(input("Type in the length of the right key>>"))
        if raw_text == 'q':
            print("exiting...\n")
            break
        text = cleaner_of_rubbish(raw_text)
        n = len(text)
        alphabet = alphabet_dict[language]
        #finding r

        index_of_coincidence = index_of_coincidence_lang[language]
        r = 2
        min_delta = 1
        min_ic = 0
        del_array = {}
        min_r = r
        while True:
            index_of_coincidence_r = ic_searcher(r, n, text, language)

            value_of_delta_ic = abs(index_of_coincidence_r-index_of_coincidence)
            if value_of_delta_ic < min_delta:
                if min_delta/value_of_delta_ic >= 1.5:
                    del_array[min_r] = min_ic
                    print('\n', min_r, 'was deleted')
                    min_ic = index_of_coincidence_r
                    min_delta = value_of_delta_ic
                    min_r = r

            if right_key_length == r:
                ic_of_right_key = ic_searcher(r, n, text, language)
            
            r += 1
            if r == ceil(n/2):
                break
            

        print("\nminimal index of coincidence by the first method:", min_ic)
        print("the range of minimal delta:", min_r, '\n')

        # let the next situation be: we've got the right period of key - r

        r = min_r

        res = key_searcher(r, n, text, language)

        print("The resulting key is", res, '\n')

        print('Now printing deleted ranges:\n')
        for r, index_of_coincidence_r in del_array.items():
            res = key_searcher(r, n, text, language)
            print('For range {r} resulting key is {res}.'.format(**{'r': r, 'res': res}))
            print("The value of idenx of coincidence is {a}.\n".format(**{'a': index_of_coincidence_r}))
        
        print("For the right range {r} resulting key is {res}.".format(**{'r': right_key_length, 'res': key_searcher(right_key_length, n, text, language)}))
        print("The value of index of coincidence is {a}.\n".format(**{'a': ic_of_right_key}))
