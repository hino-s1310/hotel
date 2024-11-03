import re

from hotel.pages.home import HomePage
from hotel.pages.mypage import MyPage
from hotel.pages.signup import SignUpPage
from hotel.pages.icon import IconPage
from playwright.sync_api import Page, expect
import pytest



@pytest.mark.parametrize("usr_name,email,pwd,pwd_confirm,rank,address,phone,gender,birthday,validate_birthday,check_flag,img_path,slider_value,RGB_value,validate_RGB_value,screenshot_path",
                        [("森本雄介","yusuke@example.com","pazzw0rd","pazzw0rd","プレミアム会員","豊島区","04099999999","男性","1999-01-01","1999年1月1日", "受け取る","tests/imgs/icon_img.jpg","50","#000000","rgb(0, 0, 0)","screenshots/icon/icon_screenshot.png")])


def test_set_icon(page: Page,
                home_page: HomePage,
                my_page: MyPage,
                signup_page: SignUpPage,
                icon_page: IconPage,
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
                check_flag,
                img_path,
                slider_value,
                RGB_value,
                validate_RGB_value,
                screenshot_path) -> None:
    
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

    # パスワード確認欄に「<password_confirm>」を入力する
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

    # メールアドレス検証
    expect(my_page.email_text).to_contain_text(email)

    # 氏名検証
    expect(my_page.username_text).to_contain_text(usr_name)

    # 会員ランク検証
    expect(my_page.rank_text).to_contain_text(rank)

    # 住所検証
    expect(my_page.address_text).to_contain_text(address)

    # 電話番号検証
    expect(my_page.phone_text).to_contain_text(phone)

    # 性別の検証
    expect(my_page.gender_text).to_contain_text(gender)

    # 生年月日の検証
    expect(my_page.birthday_text).to_contain_text(validate_birthday) 

    # お知らせの検証
    expect(my_page.notification_text).to_contain_text(check_flag)

    # アイコン設定ボタンを押下
    my_page.set_icon_button.click()

    # アイコンページに遷移したことを確認
    expect(icon_page.iconpage_heading).to_contain_text("アイコン設定")

    # 画像のアップロード
    icon_page.upload_img(img_path)
    
    #拡大縮小スライダーの設定
    icon_page.set_scaling(slider_value)

    # 枠線の色を選択
    icon_page.fill_color(RGB_value)

    # 確定ボタンを押下
    icon_page.click_confirm()

    # ページの見出しが「マイページ」であることを確認する
    expect(my_page.mypage_heading).to_contain_text("マイページ")

    # アイコンが存在していることを検証する
    expect(my_page.icon).to_be_visible()

    # アイコンの枠の色が設定した色であることを確認する
    expect(my_page.icon).to_have_css("background-color", validate_RGB_value)

    # アイコンのスクリーンショットを作成する
    my_page.icon.screenshot(path=screenshot_path)
