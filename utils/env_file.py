from selenium import webdriver
from appium import webdriver


# desired_cap={
#   "platformName": "Android",
#   "platformVersion": "10",
#   "deviceName": "emulator-5554",
#   "appPackage" : "com.android.contacts",
#   "appActivity" : "com.android.contacts.activities.PeopleActivity",
#   "apk" : "/media/muthu/sub1/Pytest-bdd--mobile/build/seller-app-release-v1.32.apk"
# }

caps = {}
caps["platformName"] = "android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "emulator-5554"
caps["app"] = "/home/muthu/Downloads/seller-app-release-v1.32.apk"
caps["appPackage"] = "com.sellerapplication"
caps["appActivity"] = "com.sellerapplication.MainActivity"
caps["ensureWebviewsHavePages"] = True
caps["newCommandTimeout"] = 0


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)











