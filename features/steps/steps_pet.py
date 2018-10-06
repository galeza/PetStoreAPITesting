
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager
from hamcrest import assert_that, equal_to, contains_string

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
    elif 'POST UPLOADIMAGE' == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint+ "/" + str(context.pet.get_pet_id()) + "/" + "uploadImage")
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

@when(u'Request BODY form parameters are set using pet photo details')
def step_impl(context):
    context.requestConfigManager.set_http_request_body_with_pet_photo(context.pet)
        
@when(u'Photo is selected as "{photo}"')
def step_impl(context, photo):
    context.pet.set_pet_photo(photo)
        
@then(u'Response BODY contains newly added pet details')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))
    assert_that(added_pet_json['name'], equal_to(context.pet.get_pet_name()))
    assert_that(added_pet_json['id'], equal_to(context.pet.get_pet_id()))
    assert_that(added_pet_json['photoUrls'], equal_to(context.pet.get_pet_photoUrls()))

@then(u'Response BODY pet status is equal to pet status')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))
    
    
@when(u'Pet details are specified as "{pet_name}" and "{photoUrl}" and "{status}"')
def step_impl(context, pet_name, photoUrl, status):
    print("1 " + context.pet.get_pet_name())
    context.pet.set_pet_name(pet_name)
    print("2 " + context.pet.get_pet_name())
    context.pet.set_pet_status(status)
    photoUrls = []
    photoUrls.append(photoUrl)
    context.pet.set_pet_photoUrls(photoUrls)

@when(u'Pet details are specified as "{pet_name}" and "{status}"')
def step_impl(context, pet_name, status):
    #TODO one step
    context.pet.set_pet_name(pet_name)
    context.pet.set_pet_status(status)

@step(u'Response BODY contains uploaded file name')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert_that(added_pet_json['message'], contains_string(context.pet.get_pet_photo()))
      
