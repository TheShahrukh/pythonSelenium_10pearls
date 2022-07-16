== NOTE: Please switch to main branch for the code ====

== Project Info =======

Tool : Selenium
Language : Python
IDE used : Pycharm
Design Pattern : Page Object Model
Requirement.txt: Generated using pipreqs

=== Project Structure ====

Directories: pages => contains page file (locators and methods acting upon them) test => Contains test cases (script) (positive and negative) to verifi login.

=== Pages : LoginPage ====

Pretty self explainotory :: Its class containing login page locators and methods.

=== Tests : test_login.py ===

First Case :

Opens URL -> Asserts URL is opened (Through Title)
Logins with correct credentials
Verifies login through updated URL (Asserts)
Second Case :

Opens URL -> Asserts URL is opened (Through Title)
Logins with Wrong credentials
Verifies error msg is appeared (Asserting error messaging)
And user is on same page (Asserting current URl should be same)
