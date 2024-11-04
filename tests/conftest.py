import pytest
import sys

sys.path.append('../')
from hotel.pages.home import HomePage
from hotel.pages.login import LoginPage
from hotel.pages.mypage import MyPage
from hotel.pages.plans import PlansPage
from hotel.pages.reserve import ReservePage
from hotel.pages.signup import SignUpPage
from hotel.pages.icon import IconPage

from hotel.components.header import Header

from playwright.sync_api import Page

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
def plans_page(page: Page) -> PlansPage:
    return PlansPage(page)

@pytest.fixture
def reserve_page(page: Page) -> ReservePage:
    return ReservePage(page)

@pytest.fixture
def signup_page(page: Page) -> SignUpPage:
    return SignUpPage(page)

@pytest.fixture
def icon_page(page: Page) -> IconPage:
    return IconPage(page)