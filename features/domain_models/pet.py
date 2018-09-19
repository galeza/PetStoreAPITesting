'''
Created on Sep 15, 2018

@author: agagaleza
'''

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
    photoUrls = []
    status = ""

    def get_pet_id(self):
        return  self.pet_id

    def set_pet_id(self, pet_id):
        self.pet_id = pet_id
            
    def get_pet_name(self):
        return self.name

    def set_pet_name(self, name):
        self.name = name
       
    def get_pet_status(self):
        return self.status
    
    def set_pet_status(self, status):
        self.status = status

    def get_pet_photoUrls(self):
        return self.photoUrls
    
    def set_pet_photoUrls(self, photoUrls):
        self.photoUrls = photoUrls
    
    def set_pet_details(self, pet_details):
        self.set_pet_id(pet_details.get("id"))  
        self.set_pet_name(pet_details.get("name"))
#         for dla pet_URLS
        self.set_pet_photoUrls(pet_details.get("photoUrls"))
        self.set_pet_status(pet_details.get("status"))
        
    def __init__(self):
        '''
        Constructor
        '''

        
        
        