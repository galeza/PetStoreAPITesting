'''
Created on Nov 22, 2018

# -----------------------------------------------------------------------------
# USER DOMAIN-MODEL:
# -----------------------------------------------------------------------------

User contains: 
id    integer($int64)
username    string
firstName    string
lastName    string
email    string
password    string
phone    string
userStatus    integer($int32)


@author: agagaleza
'''

from common.util.random_string_generator import RandomStringGenerator
import logging
from common.config.request_constants import RequestConstants

class User(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._user_id  = 0
        self._username =''
        self._first_name =''
        self._last_name  =''
        self._email =''
        self._password =''
        self._phone =''
        self._user_status =0
    
    @property
    def user_id(self):
        """user_id property."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @user_id.deleter
    def user_id(self):
        del self._user_id
                
    @property
    def username(self):
        """username property."""
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @username.deleter
    def username(self):
        del self._username
                
    @property
    def first_name(self):
        """first_name property."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        del self._first_name
                
    @property
    def last_name(self):
        """last_name property."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @last_name.deleter
    def last_name(self):
        del self._last_name
                
    @property
    def email(self):
        """email property."""
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email
                
    @property
    def password(self):
        """password property."""
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password
                
    @property
    def phone(self):
        """phone property."""
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @phone.deleter
    def phone(self):
        del self._phone
                
    @property
    def user_status(self):
        """user_status property."""
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
        
    @user_status.deleter
    def user_status(self):
        del self._user_status