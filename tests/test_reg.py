from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from appium import webdriver
from utils.env_file import driver
from time import sleep
# import object

scenarios('../features/login.feature')


@given("User see B2C Logo")
def app_logo():
    print('User see B2C Logo')
    pass

@when(parsers.cfparse("User enter {num:Number} Verify OTP Number", extra_types=dict(Number=int))) 
def verify_pass(num):
    verify_pass = driver.find_element_by_accessibility_id("Input verification code")
    verify_pass.send_keys(num)
    
@when("User click AGREE and CONTINUE")
def agree_continue():
    agree_and_continue = driver.find_element_by_accessibility_id("Agree and continue")
    agree_and_continue.click()

@when("User choose English and click NEXT button")
def choose_english():
    choose_eng = driver.find_element_by_accessibility_id("englishLangBtn")
    choose_eng.click()
    sleep(10)
    choose_nxt = driver.find_element_by_accessibility_id("nextBtn")
    choose_nxt.click()
    

# @when(parsers.cfparse('User enter Valid mobile number {mobile:Number}', extra_types=dict(Number=int)))
@when(parsers.parse("User enter Valid mobile number {mobile:d}"))
def mobile_no(mobile):
    print('mobile number: ', mobile)
    mobile_number = driver.find_element_by_accessibility_id("mobileInput")
    mobile_number.send_keys(mobile)

@when("User click GET VERIFICATION CODE button")
def get_verify_code():
    get_verification_code = driver.find_element_by_accessibility_id("getVerificationCode")
    get_verification_code.click()

@when("Get the OTP")
def get_otp():
    pass

@when(parsers.cfparse("Enter OTP {otp:Number} and click VERIFY OTP button", extra_types=dict(Number=int)))
def otp_value(otp):
    otp_value = driver.find_element_by_xpath("//android.widget.EditText[@text='-']")
    otp_value.send_keys(otp)
    sleep(10)
    verify_otp = driver.find_element_by_accessibility_id("verifyOtpBtn")
    verify_otp.click()


@when("User click HOME button")
def home_btn():
    home_button = driver.find_element_by_accessibility_id("nextBtn")
    home_button.click()

@then("App Navigate to HOME screen")
def home_screen():
    pass