from stored_values.common_values import user_one, password
from time import sleep

class TestLoginPage:

    def test_login_page(self, LoginPageObject):
        '''
        Login with the correct credentials . Try to make the test fail by looking for an error message
        that would appear whenever you put in the WRONG credentials. Since we log in correctly, we're navigated to the
        homepage instead and the error message never shows up on the login page. We do this just to verify that
        the fail screenshot appears on the html report, which it doesn't
        '''
        LoginPageObject.login(user_one, password) # pass in the correct credentials to log in
        assert LoginPageObject.error_message_present()