
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager


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
        if(row['particular']) == "photoUrls":
            
            photoUrls.append(row['value'])
            
        else:
            pet_details[row['particular']] = row['value']
    if photoUrls.__len__() > 0:
        pet_details["photoUrls"] = photoUrls  
    context.pet.set_pet_details(pet_details)
                
@when(u'Add pet "{status}"')
def step_impl(context, status):
    context.pet.set_pet_status(status)
                    
@when(u'Set BODY form param using pet details')
def step_impl(context):
    context.requestConfigManager.set_http_request_body_with_pet_details(context.pet)
    
    
@then(u'Response BODY contains newly added pet details')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert(added_pet_json['status'] == context.pet.get_pet_status())
    assert(added_pet_json['name'] == context.pet.get_pet_name())
    assert(added_pet_json['id'] == context.pet.get_pet_id())
# TODO how to validate photoUrls
    
    
    