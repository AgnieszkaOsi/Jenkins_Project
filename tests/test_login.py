from tests.test_first import FirstTest


class LoginTest(FirstTest):
    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.click_log_in()


