Feature: CoinMart login page authentication


  Scenario: User logs in

     Given I am not logged in

     And CoinMart is set up

      When I log in with "admin" and "default"

      Then I should see the response message "You were logged in"


  Scenario: User logs in with incorrect username

     Given I am not logged in

     And CoinMart is set up

      When I log in with "notright" and "default"

      Then I should see the response message "Invalid username"


  Scenario: User logs in with incorrect password

     Given I am not logged in

     And CoinMart is set up

      When I log in with "admin" and "notright"

      Then I should see the response message "Invalid password"


  Scenario: User logs out successfully

     Given CoinMart is set up

     And I log in with "admin" and "default"

      When I log out

      Then I should see the response message "You were logged out"


  Scenario: User registers with valid credentials

     Given I am not logged in

     And I am at the registration page

      When I register with "testuser" and "Testing123"

      Then I am redirected to the home page

      And I should see the response message "You were successfully registered and have been logged in"


  Scenario: User registers with invalid credentials

     Given I am not logged in

     And I am at the registration page

      When I register with "user" and "baduserpw"

      Then I am redirected to the registration page

      And I should see the response message "Invalid password. Passwords must contain at least 8 characters and at least one capital letter and one number"