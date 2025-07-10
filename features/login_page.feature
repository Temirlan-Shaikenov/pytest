Feature: Login functionality
  Scenario Outline: Successful login with valid credentials
    Given the user navigates to the login page
    When the user logs in with email "<email>" and password "<password>"
    Then the login should be successful


  Examples:

    | email                     | password |

    | user1@gmail.com           | pass111 |
    | user2@gmail.com           | pass222  |