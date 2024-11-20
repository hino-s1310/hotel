from playwright.sync_api import Page
from components.header import Header

class MyPage:
    URL = "https://hotel.testplanisphere.dev/ja/mypage.html"

    def __init__(self, page: Page, header:Header) -> None:
        self.page = page
        self.mypage_heading = page.get_by_role("heading", name="マイページ")
        self.email_text = page.locator("id=email")
        self.username_text = page.locator("id=username")
        self.rank_text = page.locator("id=rank")
        self.address_text = page.locator("id=address")
        self.phone_text = page.locator("id=tel")
        self.gender_text = page.locator("id=gender")
        self.birthday_text = page.locator("id=birthday")
        self.notification_text = page.locator("id=notification")
        self.set_icon_button = page.get_by_role("button", name="アイコン設定")
        self.withdraw_button = page.get_by_role("button", name="退会する")
        self.logout_button = header.logout_button
        self.reserve_link = header.reserve_link
        self.icon = page.get_by_role("img")

    def load(self) -> None:
        self.page.goto(self.URL)
    
    def click_reserve(self) -> None:
        self.reserve_link.click()

    def click_logout(self) -> None:
        self.logout_button.click()

    def click_set_icon(self) -> None:
        self.set_icon_button.click()

    def withdraw_member(self) -> None:
        self.withdraw_button.click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.on("dialog", lambda dialog: dialog.accept())

