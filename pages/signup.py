from playwright.sync_api import Page, expect

class SignUpPage:
    URL = "https://hotel.testplanisphere.dev/ja/signup.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.signup_heading = page.get_by_role("heading", name="会員登録")
        self.email_input = page.get_by_role("textbox", name="メールアドレス 必須")
        self.password_input = page.get_by_role("textbox", name="パスワード 必須")
        self.password_confirm_input = page.get_by_role("textbox", name="パスワード（確認） 必須")
        self.name_input = page.get_by_role("textbox", name="氏名 必須")
        self.premium_rank_radiobox = page.get_by_role("radio", name="プレミアム会員")
        self.normal_rank_radiobox = page.get_by_role("radio", name="一般会員")
        self.address_input = page.get_by_role("textbox", name="住所")
        self.phone_input = page.get_by_role("textbox", name="電話番号")
        self.gender_combobox = page.get_by_role("combobox", name="性別")
        self.birthday_input = page.locator("id=birthday")
        self.notification_checkbox = page.get_by_role("checkbox", name="お知らせを受け取る")
        self.signup_button = page.get_by_role("button", name="登録")

    def load(self) -> None:
        self.page.goto(self.URL)

    # メールアドレス欄入力
    def fill_email(self, email) -> None:
        self.email_input.fill(email)

    # パスワード欄入力
    def fill_password(self, password) -> None:
        self.password_input.fill(password)
    
    # パスワード確認欄入力
    def fill_password_confirm(self, password_confirm) -> None:
        self.password_confirm_input.fill(password_confirm)

    # 氏名欄入力
    def fill_name(self, name) -> None:
        self.name_input.fill(name)
    
    # 会員ランクのラジオボックスを選択
    def  select_rank(self, rank) -> None:
        if rank == "プレミアム会員":
            if not self.premium_rank_radiobox.is_checked() == False:
                self.premium_rank_radiobox.check()
        elif rank == "一般会員":
            if not self.normal_rank_radiobox_rank_radiobox.is_checked() == False:
                self.normal_rank_radiobox.check()

    # 住所欄入力
    def fill_address(self, address) -> None:
        self.address_input.fill(address)
    
    # 電話番号欄入力
    def fill_phone(self, phone) -> None:
        self.phone_input.fill(phone)

    # 性別欄選択
    def select_gender(self, gender) -> None:
        self.gender_combobox.select_option(gender)

    # 誕生日入力
    def fill_birthday(self, birth_day) -> None:
#        birth_day = str(year) + "-" + str(month) + "-" + str(day)

        # 誕生日入力
        self.birthday_input.fill(birth_day)

    # 引数の値によってお知らせを受け取るかどうかチェックする
    def check_notification(self, check_flag) -> None:
        if check_flag == "受け取る":
            if not self.notification_checkbox.is_checked() == True:
                self.notification_checkbox.check()
        elif check_flag == "受け取らない":
            if not self.notification_checkbox.is_checked() == False:
                self.notification_checkbox.check()

    # 登録ボタンを押下
    def click_signup(self) -> None:
        self.signup_button.click()

