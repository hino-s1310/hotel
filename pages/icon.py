from playwright.sync_api import Page

class IconPage:
    URL = "https://hotel.testplanisphere.dev/ja/icon.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.iconpage_heading = page.get_by_role("heading", name="アイコン設定")
        self.upload_input = page.locator("id=icon")
        self.scaling_input = page.get_by_role("slider", name="拡大・縮小")
        self.color_input = page.locator("id=color")
        self.confirm_button = page.get_by_role("button", name="確定")

    def load(self) -> None:
        self.page.goto(self.URL)
    
    def upload_img(self, img_path) -> None:
        self.upload_input.set_input_files(img_path)

    def set_scaling(self, scale_value) -> None:
        self.scaling_input.fill(scale_value)

    def fill_color(self, color_value) -> None:
        self.color_input.fill(color_value)

    def click_confirm(self) -> None:
        self.confirm_button.click()
    