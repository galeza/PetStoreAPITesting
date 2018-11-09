'''
Created on Nov 8, 2018
# -----------------------------------------------------------------------------
# TAG DOMAIN-MODEL:
# -----------------------------------------------------------------------------

from features.domain_models.base import Base

@author: agagaleza
'''
from common.util.random_string_generator import RandomStringGenerator
from features.domain_models.base import Base

class Tag(Base):
    '''
    classdocs
    '''
    id = 0
    name = ''

    def get_tag_id(self):
        return  self.id

    def get_tag_name(self):
        return self.name

    def set_tag_name(self, tag_name):
        self.name = tag_name

                
    def __init__(self):
        '''
        Constructor
        '''
        self.id = RandomStringGenerator.generate_random_number_with_n_digits(6)
        self.name ='tag'