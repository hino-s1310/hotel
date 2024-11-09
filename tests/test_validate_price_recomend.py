import re

from hotel.pages.home import HomePage
from hotel.pages.login import LoginPage
from hotel.pages.mypage import MyPage
from hotel.pages.plans import PlansPage
from hotel.pages.reserve import ReservePage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("flag_morning,flag_noon,flag_sightseeing,price",
                        [(False,False,False,"8,750"),
                        (True,False,False,"9,750"),
                        (False,True,False,"9,750"),
                        (False,False,True,"9,750"),
                        (True,True,False,"10,750"),
                        (True,False,True,"10,750"),
                        (False,True,True,"10,750"),
                        (True,True,True,"11,750")])

def test_validate_price(page: Page,
                        reserve_page: ReservePage,
                        flag_morning,
                        flag_noon,
                        flag_sightseeing,
                        price) -> None:

        # 予約ページを開く
        reserve_page.load()

        # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
        expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))


        #　予約ページに遷移
        expect(reserve_page.reserve_heading).to_be_visible()

        #　朝食バイキングのチェエクボックスを制御
        reserve_page.controll_mvc_checkbox(flag_morning)

        #　昼からチェックインのチェエクボックスを制御
        reserve_page.controll_ncc_checkbox(flag_noon)

        #　お得な観光プランのチェックボックスを制御
        reserve_page.controll_rsc_checkbox(flag_sightseeing)

        #　金額検証
        expect(reserve_page.total_bill).to_contain_text(price)
        



