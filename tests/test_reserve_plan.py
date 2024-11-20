from pages.home import HomePage
from pages.login import LoginPage
from pages.mypage import MyPage
from pages.plans import PlansPage
from pages.reserve import ReservePage
from pages.confirm import ConfirmPage
from playwright.sync_api import Page, expect
import re,pytest

@pytest.mark.parametrize("name,email,pwd,plan_name,plan_id,stay_num,people_num,flag_morning,flag_noon_checkin,flag_reasnable_sightseeing,confirm_contact,total_bill,additional_plan,comment",
                        [("山田一郎","ichiro@example.com","password","お得な特典付きプラン","0","1","1",False,False,False,"希望しない","7,000","なし","なし")])

def test_validate_price(page: Page,
                        home_page: HomePage,
                        login_page: LoginPage,
                        my_page: MyPage,
                        plans_page: PlansPage,
                        reserve_page: ReservePage,
                        confirm_page: ConfirmPage,
                        name,
                        email,
                        pwd,
                        plan_name,
                        plan_id,
                        stay_num,
                        people_num,
                        flag_morning,
                        flag_noon_checkin,
                        flag_reasnable_sightseeing,
                        confirm_contact,
                        total_bill,
                        additional_plan,
                        comment) -> None:

        # ホームページを開く
        home_page.load()

        # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
        expect(page).to_have_title(re.compile("HOTEL PLANISPHERE"))

        # ログインボタンを押下する
        home_page.click_login()

        # ログイン画面に遷移していることを確認する
        expect(login_page.login_heading).to_contain_text("ログイン")

        # e-mailとパスワードを入力する
        login_page.submit_login(email,pwd)

        # マイページ画面に遷移しているか検証する
        expect(my_page.mypage_heading).to_contain_text("マイページ")

        #　予約ページへ移動
        my_page.click_reserve()

        #　プランページ遷移を検証
        expect(plans_page.plans_heading).to_contain_text("宿泊プラン一覧")

        # ページハンドリング
        with plans_page.page.context.expect_page() as new_page_info:
            plans_page.click_this_reserve(plan_name),
        new_page = new_page_info.value
        reserve_page.page.on("new_page", handle_page)

        # ReservePageインスタンス生成
        reserve_page = ReservePage(new_page)

        # 予約ページに遷移したことを検証
        reserve_page.set_reserveurl(plan_id)
        expect(reserve_page.page).to_have_url(reserve_page.URL)

        # 宿泊日欄で明日を選択する
        reserve_page.click_tomorrow()

        # 宿泊数欄を入力する
        reserve_page.fill_term(stay_num)

        #人数欄を入力する
        reserve_page.fill_head_count(people_num)

        # 朝食バイキングのチェックボックスを制御
        reserve_page.controll_mvc_checkbox(flag_morning)

        # 昼からチェックインのチェックボックスを制御
        reserve_page.controll_ncc_checkbox(flag_noon_checkin)

        # お得な観光プランのチェックボックスを制御
        reserve_page.controll_rsc_checkbox(flag_reasnable_sightseeing)

        # 確認のご連絡リストを選択する
        reserve_page.select_contact(confirm_contact)

        # 金額検証
        expect(reserve_page.total_bill).to_contain_text(total_bill)

        # 宿泊予約確認ページ遷移確認
        reserve_page.click_confirm_reserve_button()

        # ConfirmPageインスタンス生成
        confirm_page = ConfirmPage(new_page)

        # 予約確認ページにn遷移したことを確認
        expect(confirm_page.confirm_heading).to_contain_text("宿泊予約確認")

        # 合計金額の検証
        expect(confirm_page.total_bill).to_contain_text(total_bill)

        # プラン名の検証
        expect(confirm_page.plan_name).to_have_text(plan_name)
        
        # 追加プランの検証
        expect(confirm_page.plans).to_have_text(additional_plan)

        # 期間の検証
        term = confirm_page.calc_term(stay_num)
        expect(confirm_page.term).to_have_text(term)

        # お名前の検証
        validate_name = name + "様"
        expect(confirm_page.username).to_have_text(validate_name)

        # 確認のご連絡の検証
        expect(confirm_page.contact).to_have_text(confirm_contact)

        # ご要望・ご連絡事項等の検証
        expect(confirm_page.comment).to_have_text(comment)

        confirm_page.click_confirm()

        # 予約ページに遷移したことを検証
        expect(plans_page.plans_heading).to_have_text("宿泊プラン一覧")

def handle_page(page):
    page.wait_for_load_state()
    print(page.title())

