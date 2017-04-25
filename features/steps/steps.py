
from behave import *
import time

@given(u'CoinMart is set up')
def CoinMart_is_set_up(context):
    assert context.home

@given(u'I am not logged in')
def logout(context):
    driver = context.browser
    driver.get(context.home + '/logout')
    time.sleep(1)

@given(u'I log in with "{username}" and "{password}" and redirected to the registration page')
@given(u'I log in with "{username}" and "{password}"')
@when(u'I log in with "{username}" and "{password}"')
def login(context, username, password):
    driver = context.browser
    driver.get(context.home + "/login")
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    login_button = driver.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()
    time.sleep(1)

@when(u'I log out')
def logout(context):
    driver = context.browser
    driver.get(context.home + '/logout')
    time.sleep(1)


@then(u'I should see the response message "{message}"')
def message(context, message):
    driver = context.browser
    driver.get(context.home)
    assert str.encode(message)

@given(u'I am at the registration page')
def visit_registration(context):
    driver = context.browser
    driver.get(context.home + "/register")

@when(u'I register with "{username}" and "{password}"')
def valid_registration(context, username, password):
    driver = context.browser
    driver.get(context.home + "/register")
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    cfm_passwd = driver.find_element_by_name('cfm_password')
    register_button = driver.find_element_by_id('btn_register')
    uname.clear();
    passwd.clear();
    cfm_passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    cfm_passwd.send_keys(password)
    register_button.click()
    time.sleep(1)

@then(u'I am redirected to the home page')
def visit(context):
    driver = context.browser
    driver.get(context.home)

@then(u'I am redirected to the registration page')
def visit_registration(context):
    driver=context.browser
    driver.get(context.home + "/register")

#@then(u'I should see the response message "{message}"')
#def message(context, message):
#    driver = context.browser
#    driver.get(context.home)
#    assert str.encode(message)
