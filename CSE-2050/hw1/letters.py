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

if __name__ == "__main__":
    the_file = input()
    letcount = letter_count(the_file)
    letfreq = letter_frequency(letter_count(the_file))
    assert (letcount['a']) == 13 # tests if my code counts 13 as
    assert letfreq['a'] == 0.06190476190476191 # test if my a frequency count matches the one in the PDF