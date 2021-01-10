from multiprocessing import Pool
from datetime import datetime
from math import sqrt, floor
from numba import njit
from copy import deepcopy

'''
@njit
def is_prime(x):
    for i in range(2, floor(sqrt(x))):
        if x % i == 0:
            return 0
    return x

@njit
def main():
    sum_of_primes = 18
    for j in range(10, 10000000):
        sum_of_primes += is_prime(j)
    return sum_of_primes

start_time = datetime.now()
sum_of_primes = main()
print("Sum of primes till 10^6 is", sum_of_primes)
print("It took", datetime.now() - start_time)


#One thread
if __name__ == "__main__":

    start_time = datetime.now()

    sum_of_primes = 18
    for j in range(10, 1000000):
        sum_of_primes += is_prime(j)
    print("Sum of primes till 10^6 is", sum_of_primes)
    print("It took", datetime.now() - start_time)

    # Parallel processing
    
    number_of_pool = 16
    start_time = datetime.now()
    with Pool(number_of_pool) as p:
        sum_of_primes = sum(p.map(is_prime, list(range(10, 1000000)))) + 18

    print(f"\n\nFor number of pool of {number_of_pool}")
    print("Sum of primes till 10^6 is", sum_of_primes)
    print("It took", datetime.now() - start_time)

    # Gpu processing
    '''

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

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
@njit
def index_of_c(text, language):
    global n_y_dict_all
    n_y_dict = n_y_dict_all[language]
    n = len(text)

    for letter in text:
        if letter in alphabet:
            n_y_dict[letter] += 1
    sum_of_n_y = 0
    for letter, count in n_y_dict.items():
        if count > 1:
            sum_of_n_y += count*(count-1)
    return sum_of_n_y/(n*(n-1))

text = input("Write dat shit right here>>")

print(index_of_c(text, "en"))
