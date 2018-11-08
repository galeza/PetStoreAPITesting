'''
Created on Nov 8, 2018
# -----------------------------------------------------------------------------
# TAG DOMAIN-MODEL:
# -----------------------------------------------------------------------------


@author: agagaleza
'''
from common.util.random_string_generator import RandomStringGenerator

class Tag(object):
    '''
    classdocs
    '''
    tag_id = 0
    tag_name = ""

    def get_tag_id(self):
        return  self.tag_id

    def get_tag_name(self):
        return self.tag_name

    def set_tag_name(self, tag_name):
        self.tag_name = tag_name
        
    def __init__(self):
        '''
        Constructor
        '''
        self.tag_id = RandomStringGenerator.generate_random_number_with_n_digits(6)