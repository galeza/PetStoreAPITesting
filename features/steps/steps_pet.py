
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager

pet_details = {}


# specific id
@step(u'"{http_request_type}" api pet request endpoint is set as "{endpoint}"')
def step_impl(context, http_request_type, endpoint):
    context.requestConfigManager = RequestConfigManager()
    if 'GET' == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint + "/" + str(context.pet.get_pet_id()))
    elif 'GET FINDBYSTATUS' == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint + "?status=" )
    elif 'POST' == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint)
    elif 'PUT' == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint)
    elif 'DELETE' == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint + "/" + str(context.pet.get_pet_id()))       
        
    print(str(context.pet.get_pet_id))


@when(u'Pet details are set as "{pet_property}" and "{value}"') 
def step_impl(context, pet_property, value):
    photoUrls = []
    for row in context.table:
        if(row['pet_property']) == "photoUrls":
            
            photoUrls.append(row['value'])
            
        else:
            pet_details[row['pet_property']] = row['value']
    if photoUrls.__len__() > 0:
        pet_details["photoUrls"] = photoUrls  
    context.pet.set_pet_details(pet_details)

                
@when(u'Pet "{status}" is specified')
@when(u'Pet status is set as "{status}"')
def step_impl(context, status):
    context.pet.set_pet_status(status)

@when(u'Request BODY form parameters are set using pet details')
def step_impl(context):
    context.requestConfigManager.set_http_request_body_with_pet_details(context.pet)
    
    
@then(u'Response BODY contains newly added pet details')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert(added_pet_json['status'] == context.pet.get_pet_status())
    assert(added_pet_json['name'] == context.pet.get_pet_name())
    assert(added_pet_json['id'] == context.pet.get_pet_id())
# TODO how to validate photoUrls

    
@when(u'Pet details are specified as "{pet_name}" and "{photoUrl}" and "{status}"')
def step_impl(context, pet_name, photoUrl, status):
    print("1 " + context.pet.get_pet_name())
    context.pet.set_pet_name(pet_name)
    print("2 " + context.pet.get_pet_name())
    context.pet.set_pet_status(status)
    photoUrls = []
    photoUrls.append(photoUrl)
    context.pet.set_pet_photoUrls(photoUrls)
    
