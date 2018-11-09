
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager
from hamcrest import assert_that, equal_to, contains_string
from common.config.request_constants import RequestConstants
import logging
from features.domain_models.tag import Tag

pet_details = {}
logger = logging.getLogger(__name__)

# specific id
@step(u'"{http_request_type}" api pet request endpoint is set as "{endpoint}"')
def step_impl(context, http_request_type, endpoint):
    context.requestConfigManager = RequestConfigManager()
    if (RequestConstants.JSON_GET == http_request_type) or (RequestConstants.JSON_DELETE == http_request_type):
        context.requestConfigManager.set_endpoint(endpoint + "/" + str(context.pet.get_pet_id()))
    elif RequestConstants.JSON_FINDBYSTATUS == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint + RequestConstants.JSON_REQUEST_STATUS)
    elif (RequestConstants.JSON_POST == http_request_type) or (RequestConstants.JSON_PUT == http_request_type):
        context.requestConfigManager.set_endpoint(endpoint)
    elif RequestConstants.JSON_UPLOAD == http_request_type:
        context.requestConfigManager.set_endpoint(endpoint+ "/" + str(context.pet.get_pet_id()) + "/" + RequestConstants.JSON_UPLOAD_IMAGE)


@when(u'Pet details are set as "{pet_property}" and "{value}"') 
def step_impl(context, pet_property, value):
    photourls = []
    tags = []
    for row in context.table:
        if(row['pet_property']) == RequestConstants.JSON_PHOTOURLS:
            
            photourls.append(row['value'])
        elif(row['pet_property']) == RequestConstants.JSON_TAG:
            tag = Tag()
            tag.set_tag_name(row['value'])
            tags.append(tag.to_dict())  
        else:
            pet_details[row['pet_property']] = row['value']
    if photourls.__len__() > 0:
        pet_details[RequestConstants.JSON_PHOTOURLS] = photourls  
    if tags.__len__() > 0:
        pet_details[RequestConstants.JSON_TAGS] = tags  
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
#     print('added_pet_json ' + str(added_pet_json))
#     logger.info('added_pet_json ' + str(added_pet_json))
#     print('added_pet_json[RequestConstants.JSON_STATUS] ' + added_pet_json[RequestConstants.JSON_STATUS])
#     print('context.pet.get_pet_status() ' + context.pet.get_pet_status())
    assert_that(added_pet_json[RequestConstants.JSON_STATUS], equal_to(context.pet.get_pet_status()))
    assert_that(added_pet_json[RequestConstants.JSON_NAME], equal_to(context.pet.get_pet_name()))
    assert_that(added_pet_json[RequestConstants.JSON_ID], equal_to(context.pet.get_pet_id()))
    assert_that(added_pet_json[RequestConstants.JSON_PHOTOURLS], equal_to(context.pet.get_pet_photourls()))

@then(u'Response BODY pet status is equal to pet status')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert_that(added_pet_json[0][RequestConstants.JSON_STATUS], equal_to(context.pet.get_pet_status()))
    
    
@when(u'Pet details are specified as "{pet_name}" and "{photourl}" and "{status}"')
def step_impl(context, pet_name, photourl, status):
    context.pet.set_pet_name(pet_name)
    context.pet.set_pet_status(status)
    photourls = []
    photourls.append(photourl)
    context.pet.set_pet_photourls(photourls)

@when(u'Pet details are specified as "{pet_name}" and "{status}"')
def step_impl(context, pet_name, status):
    #TODO one step
    context.pet.set_pet_name(pet_name)
    context.pet.set_pet_status(status)

@step(u'Response BODY contains uploaded file name')
def step_impl(context):
    added_pet_json = context.requestConfigManager.get_response_full_json()
    assert_that(added_pet_json[RequestConstants.JSON_MESSAGE], contains_string(context.pet.get_pet_photo()))
      
