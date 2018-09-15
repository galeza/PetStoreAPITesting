
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager
from features.domain_models.pet import Pet


@given(u'Set GET pet request endpoint')
def step_impl(context):
    context.pet = Pet()
    context.requestConfigManager = RequestConfigManager()
    context.requestConfigManager.set_GET_endpoint("pet/" + str(context.pet.get_pet_id()))
