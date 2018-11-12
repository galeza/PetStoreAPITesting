'''
Created on Nov 8, 2018
# -----------------------------------------------------------------------------
# CATEGORY DOMAIN-MODEL:
# -----------------------------------------------------------------------------


@author: agagaleza
'''
from common.util.random_string_generator import RandomStringGenerator
from features.domain_models.base import Base

class Category(Base):
    '''
    classdocs
    '''
    id = 0
    name = ""

    def get_category_id(self):
        return  self.id

    def get_category_name(self):
        return self.name

    def set_category_name(self, category_name):
        self.name = category_name
 

               
    def __init__(self):
        '''
        Constructor
        '''
        self.id = RandomStringGenerator.generate_random_number_with_n_digits(6)
