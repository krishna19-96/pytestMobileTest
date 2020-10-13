Feature: Login the B2C app

  Scenario: Login with valid number
    Given User see B2C Logo
    When User enter 485897 Verify OTP Number
    And User click AGREE and CONTINUE
    And User choose English and click NEXT button
    And User enter Valid mobile number 1231231782
    And User click GET VERIFICATION CODE button
    And Get the OTP
    And Enter OTP 485897 and click VERIFY OTP button
    And User click HOME button
    Then App Navigate to HOME screen
    

