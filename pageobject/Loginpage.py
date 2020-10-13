from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobject.CommonMethods import CommonMethods
from testdata.test_data import TestData


class LoginPage(CommonMethods):
    
    """ Login Locator """
    Pass_code = (By.ID, "Input verification code")
    Agree_and_Continue = (By.ID, "Agree and continue")
    Choose_English = (By.ID, "englishLangBtn")
    Next_Btn = (By.ID, "nextBtn")
    Mobile_No_Field = (By.ID, "mobileInput")
    Get_verification_code = (By.ID, "getVerificationCode")
    OTP_Field = (By.XPATH, "//android.widget.EditText[@text='-']")
    Verify_OTP = (By.ID, "verifyOtpBtn")
    Home_Btn = (By.ID, "nextBtn")


    def __init__(self, driver):
        super().__init__(driver)


    def login(self, passcode, mobileno):
        self.send_keys(self.Pass_code, passcode)
        self.clicks(self.Agree_and_Continue)
        self.clicks(self.Choose_English)
        self.clicks(self.Next_Btn)
        self.send_keys(self.Mobile_No_Field, mobileno)
        self.get_element_text(self.Get_verification_code, otp)
        self.send_keys(self.OTP_Field, )
        self.clicks(self.Verify_OTP)
        self.clicks(self.Home_Btn)
