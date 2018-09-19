'''
Created on Sep 15, 2018

@author: agagaleza
'''

import random, string
from random import randint

class RandomStringGenerator(object):
    '''
    Generates random string and numbers
    '''
    
    @staticmethod
    def generate_random_pet_name(length):
        return "pet_" +''.join(random.choice(string.ascii_lowercase) for i in range(length))
    
    @staticmethod
    def generate_random_numbers(start_index, stop_index):
        return ''.join(str(random.randint(0,9)) for i in range(start_index,stop_index))

    @staticmethod
    def generate_random_number_with_N_digits(lenght):
        range_start = 10**(lenght-1)
        range_end = (10**lenght)-1
        return randint(range_start, range_end)
    
    def __init__(self):
        '''
        Constructor
        '''
        