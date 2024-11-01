from playwright.sync_api import Page

class HomePage:
    URL = "https://hotel.testplanisphere.dev/ja/index.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_button = page.get_by_role("button", name="ログイン")
        self.signup_link = page.get_by_role("link", name="会員登録")

    def load(self) -> None:
        self.page.goto(self.URL)
    
    def click_login(self) -> None:
        self.login_button.click()

    def click_signup(self) -> None:
        self.signup_link.click()