'''
Created on Sep 15, 2018

@author: agagaleza
'''

from common.util.random_string_generator import RandomStringGenerator
import logging
from common.config.request_constants import RequestConstants

# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------

class Pet(object):
    '''
    classdocs
    '''
    status_list = [RequestConstants.JSON_STATUS_AVAILABLE, RequestConstants.JSON_STATUS_PENDING, RequestConstants.JSON_STATUS_SOLD]
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
        self.set_pet_name(pet_details.get(RequestConstants.JSON_NAME))
#         for pet_URLS
        self.set_pet_photourls(pet_details.get(RequestConstants.JSON_PHOTOURLS))
        self.set_pet_status(pet_details.get(RequestConstants.JSON_STATUS))
        
    def __init__(self):
        '''
        Constructor
        '''
        self.pet_id = RandomStringGenerator.generate_random_number_with_n_digits(6)
        self.logger.info(str(self.pet_id))

        
        
        