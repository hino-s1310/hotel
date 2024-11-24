from playwright.sync_api import expect
import pytest,datetime

@pytest.mark.parametrize("img_path,slider_value,RGB_value,validate_RGB_value,screenshot_path",
                        [("tests/imgs/icon_img.jpg","50","#000000","rgb(0, 0, 0)","screenshots/icon/")])

def test_set_icon(signup,
                my_page,
                icon_page,
                img_path,
                slider_value,
                RGB_value,
                validate_RGB_value,
                screenshot_path) -> None:

    # アイコン設定ボタンを押下
    my_page.set_icon_button.click()

    # アイコンページに遷移したことを確認
    expect(icon_page.iconpage_heading).to_contain_text("アイコン設定")

    # 各項目の表示待機
    icon_page.upload_input.wait_for()
    icon_page.scaling_input.wait_for()
    icon_page.color_input.wait_for()

    # 画像のアップロード
    icon_page.upload_img(img_path)
    
    #拡大縮小スライダーの設定
    icon_page.set_scaling(slider_value)

    # 枠線の色を選択
    icon_page.fill_color(RGB_value)

    # 確定ボタンを押下
    icon_page.click_confirm()

    # ページの見出しが「マイページ」であることを確認する
    expect(my_page.mypage_heading).to_contain_text("マイページ")

    # アイコンが存在していることを検証する
    expect(my_page.icon).to_be_visible()

    # アイコンの枠の色が設定した色であることを確認する
    expect(my_page.icon).to_have_css("background-color", validate_RGB_value)

    # アイコンのスクリーンショットを作成する
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    my_page.icon.screenshot(path=screenshot_path + now + "_icon_screenshot.png")
