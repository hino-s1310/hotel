from playwright.sync_api import Page
from components.header import Header


class HomePage:
    URL = "https://hotel.testplanisphere.dev/ja/index.html"

    def __init__(self, page: Page, header:Header) -> None:
        self.page = page
        self.login_button = header.login_button
        self.signup_link = header.signup_link

    def load(self) -> None:
        self.page.goto(self.URL)
    
    def click_login(self) -> None:
        self.login_button.click()

    def click_signup(self) -> None:
        self.signup_link.click()