'''
Created on Sep 15, 2018

@author: agagaleza
'''
from common.util.random_string_generator import RandomStringGenerator
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------

class Pet(object):
    '''
    classdocs
    '''
    status_list = ["available", "pending", "sold"]

    def get_pet_id(self):
        return  self.id
    
    def get_pet_name(self):
        return self.name
    
    def get_pet_status(self):
        return self.status
    
    def set_pet_status(self, status_number):
        self.status = self.status_list[status_number]
    
    def __init__(self):
        '''
        Constructor
        '''
        self.id = 2
        self.name = RandomStringGenerator.generate_random_pet_name(3)
        self.photoUrls = "string"
        self.status = self.set_pet_status(0)