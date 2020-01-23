'''
Created on Jan 21, 2020

@author: agagaleza
'''
from common.util.random_string_generator import RandomStringGenerator
import datetime

class Order(object):
    '''
    classdocs
    '''

    @property
    def order_id(self):
        """order_id property."""
        return self._order_id

    @property
    def pet_id(self):
        """pet_id property."""
        return self._pet_id

    @property
    def quantity(self):
        """quantity property."""
        return self._quantity

    @property
    def ship_date(self):
        """ship_date property."""
        return self._ship_date

    @property
    def status(self):
        """status property."""
        return self._status
    
    @property
    def complete(self):
        """complete property."""
        return self._complete
               
    def __init__(self, pet):
        '''
        Constructor
        '''
        self._order_id = RandomStringGenerator.generate_random_number_with_n_digits(1)
        self._pet_id = pet.pet_id()
        self._quantity = 1
        self._ship_date = datetime.datetime.now()
        self._status = ""
        self._complete = False
        