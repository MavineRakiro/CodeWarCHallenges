

"""
In this kata you will create a function that takes a list of non-negative
integers and strings and returns a new list with the strings filtered out.
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
"""
def filter_list(l):
    int_list = []
    for i in l:
        if type(i)==int:
            int_list.append(i)
    return int_list

def filter_list(l):
    return [i for i in l if isinstance(i, int)]
    # return [i for i in l if type(i)==int]

"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    vowels = "aeiou"
    num_vowels = 0
    for letter in input_str:
        if letter in vowels:
            num_vowels += 1
    return num_vowels
    # return len([i for i in input_str if i in vowels])

"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""
def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = [int(i) for i in numbers]
    return f"{str(max(numbers))} {str(min(numbers))}"

"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
"""

def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[-1]]
    while len(signature) < n:
        last_three = signature[-1:-4:-1]
        signature.append(sum(last_three))
    return signature

"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6):
        try:
            a = [int(i) for i in pin]
            return True
        except:
            return False
    else:
        return False

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

validate_pin = lambda pin : len(pin) and pin.isdigit()

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)
"""
def solution(number):
    new_a = []
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            new_a.append(i)
    return sum(new_a)

"""
Complete the solution so that it splits the string into pairs of two characters.
 If the string contains an odd number of characters then it should replace the
  missing second character of the final pair with an underscore ('_').
"""


def solution(s):
 split_strings = []
 n = 2
 if len(s) % 2 == 0:
  for i in range(0, len(s), n):
   split_strings.append(s[i: i + n])
 else:
  s += '_'
  for i in range(0, len(s), n):
   split_strings.append(s[i: i + n])

 print(split_strings)
 pass

"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""


def count_bits(n):
 return len(bin(n).replace("0b", "").replace("0", ""))

"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""

from itertools import groupby

def unique_in_order(iterable):
    lst = [i[0] for i in groupby(iterable)]
    return lst
    pass

"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""


# def tower_builder(n_floors):
#   return [("*" * (i*2-1)).center(n_floors*2-1) for i in range(1, n_floors+1)]

def tower_builder(n_floors):
    tower = []
    floor = ''

    for f in range(n_floors):
        stars = '*' * (f * 2 + 1)
        spaces = ' ' * (n_floors - f - 1)
        floor = spaces + stars + spaces
        tower.append(floor)

    return tower

"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

import string

def is_pangram(s):
    s = s.lower()
    alphabets = string.ascii_lowercase
    s = "".join(sorted(set(i for i in s if i not in string.punctuation and i != " ")))
    return alphabets in s 

"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.
"""
import re
def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    MORSE_CODE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    MORSE_CODE = {v:k for k,v in MORSE_CODE.items()}
    n = re.split(r'\s{2,}', morse_code)
    modified = " ".join("".join(MORSE_CODE[j] for j in i.split()) for  i in n)
    return modified
   #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

