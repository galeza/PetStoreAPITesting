'''
Created on 14 september 2018

Constants that are used in report generation.

@author: Agnieszka Galeza
'''

class ReportConstants(object):
    '''
    Manages shared constants for tests
    '''
    #report constants
    PASSED = 'passed'
    FAILED = 'failed'
    SKIPPED = 'skipped'
    ERROR = 'error'
    BROKEN = 'broken'
    REPORT_STATUSES ={
        PASSED : PASSED,
        FAILED : FAILED,
        SKIPPED : SKIPPED,
        ERROR : ERROR,
        BROKEN : FAILED
        }
    
    #report json columns
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
        