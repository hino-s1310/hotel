import re

from hotel.pages.mypage import MyPage
from playwright.sync_api import Page, expect

def test_withdraw_member(page: Page,
                my_page: MyPage,
                signup) -> None:

    # 退会するボタンを押下
    my_page.withdraw_member()

    # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
    expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))
