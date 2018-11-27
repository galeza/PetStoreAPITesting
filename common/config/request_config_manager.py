'''
Created on Sep 14, 2018

RequestConfigManager is a singleton class that manages HTTP requests - 
contains methods that set endpoint URL, content type, accept typ and get response
from Swagger PetStore server. 



@author: agagaleza
'''
import requests
from common.config.request_constants import RequestConstants
import logging


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
    multipart_data ={}
    logger = logging.getLogger(__name__)    

    def __init__(self):
        '''
        Constructor
        '''
        self.configure_logger()
    
    def set_basic_url(self, basic_url):
        self.basic_config[RequestConstants.JSON_URL] = basic_url
    
    def get_basic_url(self):
        return self.basic_config[RequestConstants.JSON_URL]   
    
    def set_http_content_type(self, header_content_type):
        self.http_request_header[RequestConstants.JSON_CONTENT_TYPE] = header_content_type

    def set_api_key(self):
        self.http_request_header[RequestConstants.JSON_API_KEY] = RequestConstants.API_KEY
            
    def get_http_content_type(self):
        return self.http_request_header[RequestConstants.JSON_CONTENT_TYPE]      
    
    def set_http_accept_type(self, header_accept_type):
        self.http_request_header[RequestConstants.JSON_ACCEPT] = header_accept_type
    
    def get_http_accept_type(self):
        return self.http_request_header[RequestConstants.JSON_ACCEPT]   
    
    def set_endpoint(self, api_endpoint):
        self.basic_config[RequestConstants.JSON_ENDPOINT] = api_endpoint
    
    def get_endpoint(self):
        return self.basic_config[RequestConstants.JSON_ENDPOINT]       
       
    def get_http_request_body(self):
        return self.http_request_body

    def clear_http_request_body(self):
        self.http_request_body.clear()

    def clear_http_request_header(self):
        self.http_request_header.clear()
               
    def set_get_response_full(self, url_temp):
        self.basic_config[RequestConstants.JSON_RESPONSE] = requests.get(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         data=self.http_request_body) 

            
    def set_post_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config[RequestConstants.JSON_RESPONSE] = requests.post(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         json=self.http_request_body) 

    def set_post_uploadimage_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config[RequestConstants.JSON_RESPONSE] = requests.post(url_temp,files=self.multipart_data) 

          
    def set_delete_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config[RequestConstants.JSON_RESPONSE] = requests.delete(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         json=self.http_request_body) 


    def set_put_response_full(self, url_temp):
        self.http_request_url_query_param.clear()
        self.basic_config[RequestConstants.JSON_RESPONSE] = requests.put(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param,
                                                                                         json=self.http_request_body) 

    def set_get_user_login_response_full(self, url_temp):
        self.basic_config[RequestConstants.JSON_RESPONSE] = requests.get(url_temp,
                                                                                         headers=self.http_request_header,
                                                                                         params=self.http_request_url_query_param) 

                                               
    def get_response_full(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE]  

    def get_response_full_json(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE].json()     
    
    def set_expected_response_code(self, expected_response_code):
        self.basic_config[RequestConstants.JSON_RESPONSE_CODE] = expected_response_code
    
    def get_expected_response_code(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE_CODE]  
    
    def set_expected_response_content_type(self, expected_response_content_type):
        self.basic_config[RequestConstants.JSON_RESPONSE_CONTENT_TYPE] = expected_response_content_type
    
    def get_expected_response_content_type(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE_CONTENT_TYPE]  
    
    def get_response_full_status_code(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE].status_code   

    def get_response_full_text(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE].text 
       
    def get_response_full_content_type(self):
        return self.basic_config[RequestConstants.JSON_RESPONSE].headers[RequestConstants.JSON_CONTENT_TYPE]
    
    def set_http_request_body_with_pet_details(self, pet):
        self.http_request_body[RequestConstants.JSON_ID] = pet.pet_id
        self.http_request_body[RequestConstants.JSON_NAME] = pet.name
        self.http_request_body[RequestConstants.JSON_PHOTOURLS] = pet.photourls
        self.http_request_body[RequestConstants.JSON_STATUS] = pet.status
        self.http_request_body[RequestConstants.JSON_CATEGORY] = pet.category.to_dict()
        self.http_request_body[RequestConstants.JSON_TAGS] = pet.tag_list
#         self.logger.info('http_request_body ' + str(self.http_request_body))

    def set_http_request_url_query_param(self,user):
        self.http_request_url_query_param[RequestConstants.PARAMS_USERNAME] = user.username
        self.http_request_url_query_param[RequestConstants.PARAMS_PASSWORD] = user.password
         
    def set_http_request_body_with_pet_photo(self, pet):
        self.clear_http_request_body()

        self.multipart_data = {
            'file': (pet.photo, open('./' + pet.photo, 'rb'), 'image/jpeg'),
           }
    def configure_logger(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

