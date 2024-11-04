import re

from hotel.pages.home import HomePage
from hotel.pages.mypage import MyPage
from hotel.pages.signup import SignUpPage
from playwright.sync_api import Page, expect
import pytest



@pytest.mark.parametrize("usr_name,email,pwd,pwd_confirm,rank,address,phone,gender,birthday,validate_birthday,check_flag",
                        [("森本雄介","yusuke@example.com","pazzw0rd","pazzw0rd","プレミアム会員","豊島区","04099999999","男性","1999-01-01","1999年1月1日", "受け取る")])


def test_withdraw_member(page: Page,
                home_page: HomePage,
                my_page: MyPage,
                signup_page: SignUpPage,
                usr_name,
                email,
                pwd,
                pwd_confirm,
                rank,
                address,
                phone,
                gender,
                birthday,
                validate_birthday,
                check_flag) -> None:
    
    # ホームページを開く
    home_page.load()
        
    # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
    expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))

    # 会員登録リンクを押下する
    home_page.click_signup()

    # ページの見出しが「会員登録」であることを確認する
    expect(signup_page.signup_heading).to_contain_text("会員登録")

    # メールアドレス欄を入力する
    signup_page.fill_email(email)

    # パスワード欄を入力する
    signup_page.fill_password(pwd)

    # パスワード確認欄を入力する
    signup_page.fill_password_confirm(pwd_confirm)

    # 氏名欄を入力する
    signup_page.fill_name(usr_name)

    # 会員ランクラジオボタンを選択する
    signup_page.select_rank(rank)

    # 住所欄を入力する
    signup_page.fill_address(address)

    # 電話番号欄に「<phone>」を入力する
    signup_page.fill_phone(phone)

    # 性別リストダウンを選択する
    signup_page.select_gender(gender)

    # 生年月日欄を入力する
    signup_page.fill_birthday(birthday)

    # お知らせを受け取るにチェックを入れる
    signup_page.check_notification(check_flag)

    # 登録ボタンを押下する
    signup_page.click_signup()

    # ページの見出しが「マイページ」であることを確認する
    expect(my_page.mypage_heading).to_contain_text("マイページ")

    # 退会するボタンを押下
    my_page.withdraw_member()

    # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
    expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))
