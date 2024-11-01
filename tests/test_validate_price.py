import re

from hotel.pages.home import HomePage
from hotel.pages.login import LoginPage
from hotel.pages.mypage import MyPage
from hotel.pages.plans import PlansPage
from hotel.pages.reserve import ReservePage
from playwright.sync_api import Playwright,Page, expect
import pytest

@pytest.mark.parametrize("email,pwd,plan_id,flag_morning,flag_noon,flag_sightseeing,price",
                        [("ichiro@example.com","password","1",False,False,False,"20,000"),
                        ("jun@example.com","pa55w0rd!","1",True,False,False,"22,000"),
                        ("ichiro@example.com","password","1",False,True,False,"22,000"),
                        ("jun@example.com","pa55w0rd!","1",False,False,True,"22,000"),
                        ("ichiro@example.com","password","1",True,True,False,"24,000"),
                        ("jun@example.com","pa55w0rd!","1",True,False,True,"24,000"),
                        ("ichiro@example.com","password","1",False,True,True,"24,000"),
                        ("jun@example.com","pa55w0rd!","1",True,True,True,"26,000")])

def test_validate_price(page: Page,
                        playwright: Playwright,
                        home_page: HomePage,
                        login_page: LoginPage,
                        my_page: MyPage,
                        plans_page: PlansPage,
                        email,
                        pwd,
                        plan_id,
                        flag_morning,
                        flag_noon,
                        flag_sightseeing,
                        price) -> None:
        
        browser = playwright.chromium.launch()
        context = browser.new_context()

        # ホームページを開く
        home_page.load()

        # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
        expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))

        # ログインボタンを押下する
        home_page.click_login()

        # ログイン画面に遷移していることを確認する
        expect(login_page.login_heading).to_be_visible()

        # e-mailとパスワードを入力する
        login_page.submit_login(email,pwd)

        # マイページ画面に遷移しているか検証する
        expect(my_page.mypage_heading).to_be_visible()

        #　emailを検証する
        expect(my_page.email_text).to_have_text(email)

        #　予約ページへ移動
        my_page.click_reserve()

        #　プランページ遷移を検証
        expect(plans_page.plans_heading).to_be_visible()

        # ページハンドリング、popupじゃないと何故かできない
        with page.expect_popup() as popup_info:
            plans_page.click_this_reserve(),
        popup = popup_info.value
        page.on("popup", handle_popup)

        #ReservePageインスタンス生成
        reserve_page = ReservePage(popup)

        #URLを選択したプランに変更
        reserve_page.set_reserveurl(plan_id)

        # 予約ページに遷移
        expect(reserve_page.reserve_heading).to_be_visible()

        # 朝食バイキングのチェエクボックスを制御
        reserve_page.controll_mvc_checkbox(flag_morning)
        #controll_mvc_checkbox(popup, flag_morning)

        # 昼からチェックインのチェエクボックスを制御
        reserve_page.controll_ncc_checkbox(flag_noon)

        # お得な観光プランのチェックボックスを制御
        reserve_page.controll_rsc_checkbox(flag_sightseeing)

        # 金額検証
        expect(reserve_page.total_bill).to_contain_text(price)

def handle_popup(popup):
    popup.wait_for_load_state()
    print(popup.title())

