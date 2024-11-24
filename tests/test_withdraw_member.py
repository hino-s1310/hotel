from playwright.sync_api import expect
import re

def test_withdraw_member(home_page,
                my_page,
                signup) -> None:

    # 退会するボタンを押下
    my_page.withdraw_member()

    # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
    expect(home_page.page).to_have_title(re.compile("HOTEL PLANISPHERE"))