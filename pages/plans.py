from playwright.sync_api import Page

class PlansPage:
    URL = "https://hotel.testplanisphere.dev/ja/plans.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.plans_heading = page.get_by_role("heading", name="宿泊プラン一覧")
        self.logout_button = page.get_by_role("button", name="ログアウト")
        self.premium_text = page.get_by_role("heading", name="プレミアムプラン")
        self.reserve_this_plan = page.locator("a:below(:text(\"プレミアムプラン\"))").first


    def load(self) -> None:
        self.page.goto(self.URL)

    def click_logout(self) -> None:
        self.logout_button.click()

    def click_this_reserve(self) -> None:
        self.reserve_this_plan.click()