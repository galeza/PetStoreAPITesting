'''
Created on Nov 9, 2018

@author: agagaleza
'''
from common.config.request_constants import RequestConstants

class Base(object):
    '''
    classdocs
    '''

    def to_dict(self):
        dictionary ={}
        dictionary[RequestConstants.JSON_ID] = self.id
        dictionary[RequestConstants.JSON_NAME] = self.name
        return dictionary

    def __init__(self):
        '''
        Constructor
        '''
        