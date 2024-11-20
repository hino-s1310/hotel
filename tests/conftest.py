import pytest
import re,os,sys
sys.path.append(os.getcwd())

from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from pages.signup import SignUpPage
from pages.icon import IconPage
from components.header import Header
from playwright.sync_api import Page, expect

@pytest.fixture
def header(page: Page) -> Header:
    return Header(page)

@pytest.fixture
def home_page(page: Page, header:Header) -> HomePage:
    return HomePage(page, header)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def my_page(page: Page, header:Header) -> MyPage:
    return MyPage(page, header)

@pytest.fixture
def plans_page(page: Page, header:Header) -> PlansPage:
    return PlansPage(page,header)

@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)

@pytest.fixture
def confirm_page(page: Page) -> ConfirmPage:
    return ConfirmPage(page)

@pytest.fixture
def signup_page(page: Page) -> SignUpPage:
    return SignUpPage(page)

@pytest.fixture
def icon_page(page: Page) -> IconPage:
    return IconPage(page)

#  新規会員登録する処理
@pytest.fixture
def signup(page: Page,
            home_page: HomePage,
            signup_page: SignUpPage,
            my_page: MyPage):
    # setup
    # ホームページを開く
    home_page.load()
        
    # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
    expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))

    # 会員登録リンクを押下する
    home_page.click_signup()

    # ページの見出しが「会員登録」であることを確認する
    expect(signup_page.signup_heading).to_contain_text("会員登録")

    # メールアドレス欄を入力する
    signup_page.fill_email("yusuke@example.com")

    # パスワード欄を入力する
    signup_page.fill_password("pazzw0rd")

    # パスワード確認欄に「<password_confirm>」を入力する
    signup_page.fill_password_confirm("pazzw0rd")

    # 氏名欄を入力する
    signup_page.fill_name("森本雄介")

    # 会員ランクラジオボタンを選択する
    signup_page.select_rank("プレミアム会員")

    # 住所欄を入力する
    signup_page.fill_address("豊島区")

    # 電話番号欄を入力する
    signup_page.fill_phone("04099999999")

    # 性別リストダウンを選択する
    signup_page.select_gender("男性")

    # 生年月日欄を入力する
    signup_page.fill_birthday("1999-01-01")

    # お知らせを受け取るにチェックを入れる
    signup_page.check_notification("受け取る")

    # 登録ボタンを押下する
    signup_page.click_signup()

    # ページの見出しが「マイページ」であることを確認する
    expect(my_page.mypage_heading).to_contain_text("マイページ")

    yield