from playwright.sync_api import expect
import re,pytest

@pytest.mark.parametrize("usr_name,email,pwd,rank,address,phone,gender,birthday,check_flag",
                        [("山田一郎","ichiro@example.com","password","プレミアム会員","東京都豊島区池袋","01234567891","男性","未登録","受け取る"),
                        ("松本さくら","sakura@example.com","pass1234","一般会員","神奈川県横浜市鶴見区大黒ふ頭","未登録","女性","2000年4月1日","受け取らない"),
                        ("林潤","jun@example.com","pa55w0rd!","プレミアム会員","大阪府大阪市北区梅田","01212341234","その他","1988年12月17日","受け取らない"),
                        ("木村良樹","yoshiki@example.com","pass-pass","一般会員","未登録","01298765432","未登録","1992年8月31日","受け取る"),])

def test_login( home_page,
                login_page,
                my_page,
                usr_name,
                email,
                pwd,
                rank,
                address,
                phone,
                gender,
                birthday,
                check_flag) -> None:

        # ホームページを開く
        home_page.load()
        
        # タイトルに「HOTEL PLANISPHERE」が含まれていることを確認
        expect(home_page.page).to_have_title(re.compile("HOTEL PLANISPHERE"))

        # ログインボタンを押下する
        home_page.click_login()

        # ログイン画面に遷移していることを確認する
        expect(login_page.login_heading).to_be_visible()

        # e-mailとパスワードを入力する
        login_page.submit_login(email,pwd)

        # マイページ画面に遷移しているか検証する
        expect(my_page.mypage_heading).to_be_visible()

        #　各項目の検証
        expect(my_page.email_text).to_have_text(email)
        expect(my_page.username_text).to_have_text(usr_name)
        expect(my_page.rank_text).to_have_text(rank)
        expect(my_page.address_text).to_have_text(address)
        expect(my_page.phone_text).to_have_text(phone)
        expect(my_page.gender_text).to_have_text(gender)
        expect(my_page.birthday_text).to_have_text(birthday)
        expect(my_page.notification_text).to_have_text(check_flag)

        #　ログアウトボタンを押下する
        my_page.click_logout()


