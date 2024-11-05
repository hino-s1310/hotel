import re

from hotel.pages.home import HomePage
from hotel.pages.mypage import MyPage
from hotel.pages.signup import SignUpPage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("usr_name,email,rank,address,phone,gender,validate_birthday,check_flag",
                        [("森本雄介","yusuke@example.com","プレミアム会員","豊島区","04099999999","男性","1999年1月1日", "受け取る")])


def test_signup2(signup,
                my_page: MyPage,
                usr_name,
                email,
                rank,
                address,
                phone,
                gender,
                validate_birthday,
                check_flag) -> None:
    

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