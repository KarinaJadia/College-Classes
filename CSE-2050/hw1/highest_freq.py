import string
from string import ascii_lowercase

def letter_count(fil):
    """
    takes a file and returns the count of each letter in a dictionary
    fails if there is an error
    """
    try:
        fl = open(fil)
        everyting = fl.read().lower() # put the file contents in string called everyting
        fl.close()
        dict = {}
        alphabet = string.ascii_lowercase # string variable that holds the alphabet
        
        for char in alphabet:
            dict.update({char:0}) # creates a dictionary of each letter in the alphabet
        
        for char in everyting: # loops through file
            if char in dict: # checks if character is in the dictionary, or basically is a letter
                dict[char] += 1 # if it is a letter, updates frequency counter in the correct key
        
        return dict
    except:
        return('Error: file not found')

def letter_frequency(dict_letters):
    """
    takes dictionary and calculates the frequency of each letter and returns a new dictionary
    does so by totalling up characters and dividing each dictionary value by total
    """
    total = 0
    new_dict = dict_letters # new dictionary so I don't modify the original
    
    for key in dict_letters:
        total += dict_letters[key] # adds up the total number of letters and stores in variable
    
    for key in dict_letters:
        new_dict[key] = dict_letters.get(key, 0) / total # divides each letter's frequency by total
    
    return new_dict

def highest_freq(file):
    """
    finds the letter with the highest frequency and returns that as a tuple
    """
    dic = letter_frequency(letter_count(the_file))
    max = 0 # this variable will store the highest frequency value
    ltr = '' # this variable will store the highest frequency value's letter
    
    for key in dic: # this loop basically takes the highest frequency value and updates max and ltr
        if dic.get(key, 0) > max:
            max = dic.get(key, 0)
            ltr = key
    
    tup = (ltr, max)
    return tup

if __name__ == "__main__":
    the_file = input()
    correct = ('e', 0.10952380952380952) # value taken from PDF
    assert (highest_freq(the_file)) == correct # tests if my frequency is correct