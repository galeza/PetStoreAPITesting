'''
Created on Sep 15, 2018

# -----------------------------------------------------------------------------
# PET DOMAIN-MODEL:
# -----------------------------------------------------------------------------

Pet contains: 
id - int , 
name - String
photourls = list
status 
photo String

@author: agagaleza
'''

from common.util.random_string_generator import RandomStringGenerator
import logging
from common.config.request_constants import RequestConstants
from features.domain_models.category import Category


class Pet(object):
    '''
    classdocs
    '''

    @property
    def pet_id(self):
        """pet_id property."""
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value

    @pet_id.deleter
    def pet_id(self):
        del self._pet_id
        
    @property
    def category(self):
        """category property."""
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @category.deleter
    def category(self):
        del self._category

    @property
    def tag_list(self):
        """tag_list property."""
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        self._tag_list = value

    @tag_list.deleter
    def tag_list(self):
        del self._tag_list

    @property
    def name(self):
        """name property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name
        
    @property
    def photourls(self):
        """photourls property."""
        return self._photourls

    @photourls.setter
    def photourls(self, value):
        self._photourls = value

    @photourls.deleter
    def photourls(self):
        del self._photourls        

    @property
    def status(self):
        """status property."""
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @status.deleter
    def status(self):
        del self._status 

    @property
    def photo(self):
        """photo property."""
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value

    @photo.deleter
    def photo(self):
        del self._photo
                       
    def set_pet_details(self, pet_details):
        self.name = pet_details.get(RequestConstants.JSON_NAME)
#         for pet_URLS
        self.photourl = pet_details.get(RequestConstants.JSON_PHOTOURLS)
        self.status  = pet_details.get(RequestConstants.JSON_STATUS)
#         for pet TAGS
        self.tag_list = pet_details.get(RequestConstants.JSON_TAGS)
        self.category = pet_details.get(RequestConstants.JSON_CATEGORY)
        
    def __init__(self):
        '''
        Constructor
        '''
        self._pet_id = RandomStringGenerator.generate_random_number_with_n_digits(6)
        self._category = Category()
#             status_list = [RequestConstants.JSON_STATUS_AVAILABLE, RequestConstants.JSON_STATUS_PENDING, RequestConstants.JSON_STATUS_SOLD]
        self._tag_list = []
        self._name = ""
        self._photourls = []
        self._status = ""
        self._photo =""
#         self._logger = logging.getLogger(__name__)

        
        
        