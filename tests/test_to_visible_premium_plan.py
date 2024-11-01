import re

from hotel.pages.home import HomePage
from hotel.pages.login import LoginPage
from hotel.pages.mypage import MyPage
from hotel.pages.plans import PlansPage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("usr_name,email,pwd,rank",
                        [("山田一郎","ichiro@example.com","password","プレミアム会員"),
                        ("松本さくら","sakura@example.com","pass1234","一般会員"),
                        ("林潤","jun@example.com","pa55w0rd!","プレミアム会員"),
                        ("木村良樹","yoshiki@example.com","pass-pass","一般会員"),])


def test_to_visible_premium_plan(page: Page,
                                home_page: HomePage,
                                login_page: LoginPage,
                                my_page: MyPage,
                                plans_page: PlansPage,
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

    # ログイン処理を行う
    login_page.submit_login(email,pwd)

    # マイページ画面に遷移しているか検証する
    expect(my_page.mypage_heading).to_be_visible()

    #ログイン情報と会員の一致を検証
    expect(my_page.username_text).to_contain_text(usr_name)

    # 宿泊予約ボタンを押下
    my_page.click_reserve()

    # 宿泊予約画面に遷移しているか検証
    expect(plans_page.plans_heading).to_be_visible()

    if rank == "プレミアム会員":
        # プレミアム会員の場合、プレミアムプランが存在していることを検証する
        expect(plans_page.premium_text).to_be_visible()
    else:
        # 一般会員の場合、プレミアムプランが存在していないことを検証する
        expect(plans_page.premium_text).not_to_be_visible()
    #　ログアウトボタンを押下する
    plans_page.click_logout()
    

