*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Register
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  valle
    Set Password  1
    Set Password Confirmation  1
    Submit Register
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  valle
    Set Password  valle123
    Set Password Confirmation  ville123
    Submit Register
    Register Should Fail With Message  Passwords do not match

Login After Failed Registration
    Set Username  valle
    Set Password  valle123
    Set Password Confirmation  ville123
    Submit Register
    Register Should Fail With Message  Passwords do not match
    Go To Login Page
    Set Username  valle123
    Set Password  valle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login After Successful Registration
    Set Username  valle
    Set Password  valle123
    Set Password Confirmation  valle123
    Submit Register
    Go To Login Page
    Set Username  valle
    Set Password  valle123
    Submit Credentials
    Login Should Succeed


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}