'''
Created on Sep 15, 2018

@author: agagaleza
'''

from common.util.random_string_generator import RandomStringGenerator
import logging

# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------

class Pet(object):
    '''
    classdocs
    '''
    status_list = ["available", "pending", "sold"]
    pet_id = 0
    name = ""
    photourls = []
    status = ""
    photo =""
    logger = logging.getLogger(__name__)

    def get_pet_id(self):
        return  self.pet_id

    def get_pet_name(self):
        return self.name

    def set_pet_name(self, name):
        self.name = name
       
    def get_pet_status(self):
        return self.status
    
    def set_pet_status(self, status):
        self.status = status

    def get_pet_photourls(self):
        return self.photourls
    
    def set_pet_photourls(self, photourls):
        self.photourls = photourls

    def get_pet_photo(self):
        return self.photo
    
    def set_pet_photo(self, photo):
        self.photo = photo
            
    def set_pet_details(self, pet_details):
        self.set_pet_name(pet_details.get("name"))
#         for pet_URLS
        self.set_pet_photourls(pet_details.get("photoUrls"))
        self.set_pet_status(pet_details.get("status"))
        
    def __init__(self):
        '''
        Constructor
        '''
        self.pet_id = RandomStringGenerator.generate_random_number_with_n_digits(6)
        self.logger.info(str(self.pet_id))

        
        
        