from playwright.sync_api import expect
import pytest,re

@pytest.mark.parametrize("usr_name,email,password,password_confirm,rank,address,phone,gender,birthday,validate_birthday,check_flag",
                        [("森本雄介","yusuke@example.com","pazzw0rd","pazzw0rd","プレミアム会員","豊島区","04099999999","男性","1999-01-01","1999年1月1日", "受け取る"),
                        ("佐々木明","msasaki@example.com","pass0825","pass0825","プレミアム会員","千葉県千葉市","05099999999","女性","1995-07-21","1995年7月21日", "受け取らない"),
                        ("松田耕作","komatsu223@example.com","pazzw0rd","pazzw0rd","一般会員","埼玉県寄居町","06099999999","男性","1995-09-13","1995年9月13日", "受け取る"),
                        ("高田真美","mamidesu@example.com","mtaka01234","mtaka01234","一般会員","神奈川県川崎市","03099999999","女性","1994-03-22","1994年3月22日", "受け取らない")])

def test_signup(home_page,
                signup_page,
                my_page,
                usr_name,
                email,
                password,
                password_confirm,
                rank,
                address,
                phone,
                gender,
                birthday,
                validate_birthday,
                check_flag) -> None:
    home_page.load()
        
    # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
    expect(home_page.page).to_have_title(re.compile("HOTEL PLANISPHERE"))

    # 会員登録リンクを押下する
    home_page.click_signup()

    # ページの見出しが「会員登録」であることを確認する
    expect(signup_page.signup_heading).to_contain_text("会員登録")

    # メールアドレス欄を入力する
    signup_page.fill_email(email)

    # パスワード欄を入力する
    signup_page.fill_password(password)

    # パスワード確認欄に「<password_confirm>」を入力する
    signup_page.fill_password_confirm(password_confirm)

    # 氏名欄を入力する
    signup_page.fill_name(usr_name)

    # 会員ランクラジオボタンを選択する
    signup_page.select_rank(rank)

    # 住所欄を入力する
    signup_page.fill_address(address)

    # 電話番号欄を入力する
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