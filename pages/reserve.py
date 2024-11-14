from playwright.sync_api import Page

class ReservePage:
    URL = "https://hotel.testplanisphere.dev/ja/reserve.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.reserve_heading = page.get_by_role("heading", name="宿泊予約")
        self.date_input = page.locator("id=date")
        self.tomorrow_td = page.locator("td.ui-datepicker-current-day")
        self.term_input = page.locator("id=term")
        self.head_count_input = page.locator("id=head-count")
        self.morning_viking_checkbox = page.get_by_role("checkbox", name="朝食バイキング")
        self.noon_checkin_checkbox = page.get_by_role("checkbox", name="昼からチェックインプラン")
        self.reasonable_sightseeing_checkbox = page.get_by_role("checkbox", name="お得な観光プラン")
        self.name_input = page.get_by_role("textbox", name="氏名 必須")
        self.contact_combobox = page.get_by_role("combobox", name="確認のご連絡 必須")
        self.total_bill = page.locator("id=total-bill")
        self.confirm_reserve_button = page.get_by_role("button", name="予約内容を確認する")

    def load(self) -> None:
        self.page.goto(self.URL)

    # URLにプランIDを付与
    def set_reserveurl(self, id:str) -> None:
        self.URL = self.URL + "?plan-id=" + id

    # 宿泊日に明日の日付を入力する
    def click_tomorrow(self) -> None:
        self.date_input.click()
        #カレンダーで翌日を選択
        self.tomorrow_td.click()

    # 宿泊数の入力
    def fill_term(self, term) -> None:
        self.term_input.fill(term)
    
    # 人数の入力
    def fill_head_count(self, head_count) -> None:
        self.head_count_input.fill(head_count)

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

    def fill_name(self, name) -> None:
        self.name_input.fill(name)

    # 確認のご連絡欄を選択する
    def select_contact(self, confirm_contact) -> None:
        self.contact_combobox.select_option(confirm_contact)

    # 予約内容を確認するボタンを押下する
    def click_confirm_reserve_button(self) -> None:
        self.confirm_reserve_button.click()


