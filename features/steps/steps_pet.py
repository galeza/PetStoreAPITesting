
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager
from features.domain_models.pet import Pet
from common.util.random_string_generator import RandomStringGenerator

pet_details ={}

@given(u'Set GET pet request endpoint')
def step_impl(context):
#     context.pet = Pet()
    context.requestConfigManager = RequestConfigManager()
    context.requestConfigManager.set_GET_endpoint("pet/" + str(context.pet.get_pet_id()))

@given(u'Set POST pet api endpoint as "{post_endpoint}"')
def step_impl(context, post_endpoint):
#     context.pet = Pet()
    context.requestConfigManager = RequestConfigManager()
    context.requestConfigManager.set_POST_endpoint(post_endpoint)

@when(u'Set pet details as "{particular}" and "{value}" below') 
def step_impl(context, particular, value):
    photoUrls = []
    for row in context.table:
        print(row['particular'])
        if(row['particular']) == "photoUrls":
            
            photoUrls.append(row['value'])
            
        else:
            pet_details[row['particular']] = row['value']
    if photoUrls.__len__() > 0:
        pet_details["photoUrls"] = photoUrls  
    print("lenght = " + str(photoUrls.__len__()))
    context.pet.set_pet_details(pet_details)
                
@when(u'Set BODY form param using pet details')
def step_impl(context):
    context.requestConfigManager.set_http_request_body_with_pet_details(context.pet)