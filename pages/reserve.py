from playwright.sync_api import Page, expect

class ReservePage:
    URL = "https://hotel.testplanisphere.dev/ja/reserve.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.reserve_heading = page.get_by_role("heading", name="宿泊予約")
        self.morning_viking_checkbox = page.get_by_role("checkbox", name="朝食バイキング")
        self.noon_checkin_checkbox = page.get_by_role("checkbox", name="昼からチェックインプラン")
        self.reasonable_sightseeing_checkbox = page.get_by_role("checkbox", name="お得な観光プラン")
        self.total_bill = page.locator("id=total-bill")
        self.confirm_reserve_button = page.get_by_role("button", name="予約内容を確認する")

    def load(self) -> None:
        self.page.goto(self.URL)

    # 引数の値によって朝食バイキングチェックボックスの押下を制御する
    def controll_mvc_checkbox(self, add_flag1: bool) -> None:
        if not self.morning_viking_checkbox.is_checked() == add_flag1:
            self.morning_viking_checkbox.check()

    # 引数の値によって昼からチェックインチェックボックスの押下を制御する
    def controll_ncc_checkbox(self, add_flag2: bool) -> None:
        if not self.noon_checkin_checkbox.is_checked() == add_flag2:
            self.noon_checkin_checkbox.check()    

    # 引数の値によってお得な観光プランチェックボックスの押下を制御する
    def controll_rsc_checkbox(self, add_flag3: bool) -> None:
        if not self.reasonable_sightseeing_checkbox.is_checked() == add_flag3:
            self.reasonable_sightseeing_checkbox.check()

    # URLにプランIDを付与
    def set_reserveurl(self, id:str) -> None:
        self.URL = self.URL + "?plan-id=" + id

