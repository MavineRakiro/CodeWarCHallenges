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