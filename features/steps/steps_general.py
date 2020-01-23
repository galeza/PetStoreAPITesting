
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from common.config.request_config_manager import RequestConfigManager
from behave import given, when, then, step
from features.domain_models.pet import Pet
from features.domain_models.user import User
from hamcrest import assert_that, equal_to, matches_regexp
from common.config.request_constants import RequestConstants
import logging

logger = logging.getLogger(__name__)

@given(u'Swagger PetStore web application url is set as "{basic_url}"')
def step_impl(context, basic_url):
    """
    BACKGROUND step is called at begin of each scenario before other steps.
    """
    # -- SETUP
    context.pet = Pet()
    context.user = User()
    context.requestConfigManager = RequestConfigManager()
    context.requestConfigManager.set_basic_url(basic_url)
    
@when(u'HEADER param request content type is set as "{header_content_type}"')
def step_impl(context, header_content_type):
    context.requestConfigManager.set_http_content_type(header_content_type)


@when(u'HEADER param response accept type is set as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    context.requestConfigManager.set_http_accept_type(header_accept_type)

@step(u'HEADER param api_key is set')
def step_impl(context):
    context.requestConfigManager.set_api_key()
    
@when(u'"{http_request_type}" HTTP request is raised')
def step_impl(context, http_request_type):
    url_temp = context.requestConfigManager.get_basic_url() 
    if RequestConstants.JSON_GET == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_get_response_full(url_temp)
    elif RequestConstants.JSON_FINDBYSTATUS == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint() + context.pet.status
        context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_get_response_full(url_temp)
    elif RequestConstants.JSON_POST == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
#         context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_post_response_full(url_temp)
    elif RequestConstants.JSON_UPLOAD == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
#         context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_post_uploadimage_response_full(url_temp)        
    elif RequestConstants.JSON_PUT == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.set_put_response_full(url_temp)
    elif RequestConstants.JSON_DELETE == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.set_delete_response_full(url_temp)
    elif RequestConstants.JSON_USER_GET_LOGIN == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.set_get_user_login_response_full(url_temp)

@step(u'Valid HTTP response is received')
def step_impl(context):
    if None in context.requestConfigManager.get_response_full():
        assert_that('Null response received')
        
@step(u'Response http code is {expected_response_code:d}')
def step_impl(context, expected_response_code):
    context.requestConfigManager.set_expected_response_code(expected_response_code)
    actual_response_code = context.requestConfigManager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_response_code):
        assert_that('***ERROR: Following unexpected error response code received: ' + str(actual_response_code))

@step(u'Response http text is "{expected_response_text}"')
def step_impl(context, expected_response_text):
    actual_response_text = context.requestConfigManager.get_response_full_text()
    if actual_response_text not in expected_response_text:
        assert_that('***ERROR: Following unexpected error response text received: ' + actual_response_text)

@step(u'Response http text contains session number')
def step_impl(context):
    response_text = context.requestConfigManager.get_response_full_text()
    try:
        response = tuple(response_text.split(':'))
        session_number = response[1]
        logger.info('session number : ' + session_number)
        assert_that(session_number, matches_regexp('^[0-9]+$'))
    except:
        logger.info('User is not logged')

        
@then(u'Response HEADER content type is "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    context.requestConfigManager.set_expected_response_content_type(expected_response_content_type)
    actual_response_content_type = context.requestConfigManager.get_response_full_content_type()
    if expected_response_content_type not in actual_response_content_type:
        assert_that('***ERROR: Following unexpected error response content type received: ' + actual_response_content_type)


@then(u'Response BODY is not null or empty')
def step_impl(context):
    if None in context.requestConfigManager.get_response_full():
        assert_that('***ERROR:  Null or none response body received')
        
@when(u'HEADER params for request and response are specified')
def step_impl(context):
    context.requestConfigManager.clear_http_request_header()
    context.execute_steps(u''' when HEADER param request content type is set as "application/json"
    and HEADER param response accept type is set as "application/json" ''')
        
        
        
        
        