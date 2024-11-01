import pytest
import sys

sys.path.append('../')
from hotel.pages.home import HomePage
from hotel.pages.login import LoginPage
from hotel.pages.mypage import MyPage
from hotel.pages.plans import PlansPage
from hotel.pages.reserve import ReservePage

from playwright.sync_api import Page, sync_playwright

""" # ブラウザの設定
@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# ブラウザのセッション情報を引き継ぐ
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close() """

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def my_page(page: Page) -> MyPage:
    return MyPage(page)

@pytest.fixture
def plans_page(page: Page) -> PlansPage:
    return PlansPage(page)

@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)
