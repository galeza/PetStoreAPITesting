'''
Created on Sep 14, 2018

@author: agagaleza
'''
import requests

class Singleton(object):
    _instances = {}
    def __new__(class_, *args, **kwargs):  # @NoSelf
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]
    
class RequestConfigManager(object):
    __metaclass__ = Singleton
    '''
    classdocs
    '''
    basic_config = {}
    http_request_header = {}
    http_request_body = {}
    http_request_url_query_param = {}

    def __init__(self):
        '''
        Constructor
        '''
    
    def set_basic_url(self, basic_url):
        self.basic_config['basic_url'] = basic_url
    
    def get_basic_url(self):
        return self.basic_config['basic_url']   
    
    def set_http_content_type(self, header_content_type):
        self.http_request_header['content-type'] = header_content_type
    
    def get_http_content_type(self):
        return self.http_request_header['content-type']      
    
    def set_http_accept_type(self, header_accept_type):
        self.http_request_header['Accept'] = header_accept_type
    
    def get_http_accept_type(self):
        return self.http_request_header['Accept']   
    
    def set_GET_endpoint(self, get_api_endpoint):
        self.basic_config['GET_api_endpoint'] = get_api_endpoint
    
    def get_GET_endpoint(self):
        return self.basic_config['GET_api_endpoint']       
    
    def get_http_request_body(self):
        return self.http_request_body

    def clear_http_request_body(self):
        self.http_request_body.clear()
        
    def set_response_full(self, url_temp):
        self.basic_config['response_full'] = requests.get(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         data=self.http_request_body) 
    
    def get_response_full(self):
        return self.basic_config['response_full']  
    
    
    def set_expected_response_code(self, expected_response_code):
        self.basic_config['expected_response_code'] = expected_response_code
    
    def get_expected_response_code(self):
        return self.basic_config['expected_response_code']  
    
    def set_expected_response_content_type(self, expected_response_content_type):
        self.basic_config['expected_response_content_type'] = expected_response_content_type
    
    def get_expected_response_content_type(self):
        return self.basic_config['expected_response_content_type']  
    
    def get_response_full_status_code(self):
        return self.basic_config['response_full'].status_code   
    
    def get_response_full_content_type(self):
        print (self.basic_config['response_full'].headers['Content-Type'])
        
        return self.basic_config['response_full'].headers['Content-Type']
    
    