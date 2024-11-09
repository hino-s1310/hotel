from playwright.sync_api import Page

class ConfirmPage:
    URL = "https://hotel.testplanisphere.dev/ja/confirm.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.confirm_heading = page.get_by_role("heading", name="宿泊予約確認")
        self.total_bill = page.locator("id=total-bill")
        self.term = page.locator("id=term")
        self.head_count = page.locator("id=head-count")
        self.plans = page.locator("id=plans")
        self.username = page.locator("id=username")
        self.contact = page.locator("id=contact")
        self.coment = page.locator("id=comment")
        self.confirm_button = page.get_by_role("button", name="この内容で予約する")
        self.modal_title = page.locator("class=modal-title")
        self.modal_body_text = page.locator(".modal-body > p")
        self.modal_close_button = page.locator(".modal-footer > button")


    def load(self) -> None:
        self.page.goto(self.URL)
    
    def click_confirm(self) -> None:
        self.confirm_button.click()

        


    