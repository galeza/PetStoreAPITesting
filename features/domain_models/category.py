'''
Created on Nov 8, 2018
# -----------------------------------------------------------------------------
# CATEGORY DOMAIN-MODEL:
# -----------------------------------------------------------------------------

Category of the pet like: domesticated, protection, or entertainment 
@author: agagaleza
'''
from common.util.random_string_generator import RandomStringGenerator

class Category(object):
    '''
    classdocs
    '''
    category_id = 0
    category_name = ""

    def get_category_id(self):
        return  self.category_id

    def get_category_name(self):
        return self.category_name

    def set_category_name(self, category_name):
        self.category_name = category_name
        
    def __init__(self):
        '''
        Constructor
        '''
        self.category_id = RandomStringGenerator.generate_random_number_with_n_digits(6)