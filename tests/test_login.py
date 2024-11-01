import re

from hotel.pages.home import HomePage
from hotel.pages.login import LoginPage
from hotel.pages.mypage import MyPage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("usr_name,email,pwd,rank",
                        [("山田一郎","ichiro@example.com","password","プレミアム会員"),
                        ("松本さくら","sakura@example.com","pass1234","一般会員"),
                        ("林潤","jun@example.com","pa55w0rd!","プレミアム会員"),
                        ("木村良樹","yoshiki@example.com","pass-pass","一般会員"),])

def test_login(page: Page,
                home_page: HomePage,
                login_page: LoginPage,
                my_page: MyPage,
                usr_name,
                email,
                pwd,
                rank) -> None:

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

        #　メールアドレス、氏名、会員情報を検証する
        expect(my_page.email_text).to_have_text(email)
        expect(my_page.username_text).to_have_text(usr_name)
        expect(my_page.rank_text).to_have_text(rank)

        #　ログアウトボタンを押下する
        my_page.click_logout()


