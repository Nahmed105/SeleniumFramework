from base.basepage import BasePage

class LoginPage(BasePage):

    uri = '/index.html'
    #
    username_field = '#user-name'
    password_field = '#password'
    login_button = '[value="LOGIN"]'
    error_message = '[data-test="error"]'

    def load(self):
        self.get(self.uri)

    def login(self, username, password):
        self.load()
        self.wait_for_element_clickable(self.username_field)
        self.send_keys(username, self.username_field)
        self.wait_for_element_clickable(self.password_field)
        self.send_keys(password, self.password_field)
        self.wait_for_element_clickable(self.login_button)
        self.click_element(self.login_button)

    def error_message_present(self):
        return self.is_element_present(self.error_message)