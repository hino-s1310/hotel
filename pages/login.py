from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://hotel.testplanisphere.dev/ja/login.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_input = page.get_by_role("textbox", name="メールアドレス")
        self.password_input = page.get_by_role("textbox", name="パスワード")
        self.login_heading = page.get_by_role("heading", name="ログイン")
        self.login_submit = page.locator("id=login-button")

    def load(self) -> None:
        self.page.goto(self.URL)
    

    def submit_login(self, email: str, password:str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_submit.click()