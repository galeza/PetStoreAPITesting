'''
Created on 14 september 2018

@author: Agnieszka Galeza
'''

class Constant(object):
    '''
    Manages shared constants for tests
    '''

    PASSED = 'passed'
    FAILED = 'failed'
    SKIPPED = 'skipped'
    ERROR = 'error'
    
    #json columns
    SCENARIO = 'Scenario_'
    START = 'start'
    STOP = 'stop'
    STATUS = 'status'
    STEPS = 'steps'
    NAME = 'name'
    STATUS_DETAILS = 'statusDetails'
    MESSAGE = 'message'
    TRACE = 'trace'
    
    


      
    def __init__(self, params):
        '''
        Constructor
        '''
        