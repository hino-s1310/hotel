from playwright.sync_api import Page

class Header:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.home_link = page.get_by_role("link", name="ホーム")
        self.reserve_link = page.get_by_role("link", name="宿泊予約")
        self.signup_link = page.get_by_role("link", name="会員登録")
        self.mypage_link = page.get_by_role("link", name="マイページ")
        self.login_button = page.get_by_role("button", name="ログイン")
        self.logout_button = page.get_by_role("button", name="ログアウト")
