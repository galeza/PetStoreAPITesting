
'''
Created on Sep 10, 2018

@author: agagaleza
'''
import requests
from behave import given, when, then, step

basic_url = ""
http_request_header = {}
http_request_body = {}


@given(u'Set web application url as "{basic_url}"')
def step_impl(context, basic_url):
    basic_url['basic_url'] = basic_url
    
@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type


@given(u'Set GET pet app endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint