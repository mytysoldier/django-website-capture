from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# トップページ表示
class IndexView(TemplateView):
    template_name = "index.html"

# Webサイトのキャプチャ画像を取得しレスポンス返却
def websiteCapture(request):
    # 前回処理時のキャプチャファイルが残っていれば削除
    if os.path.exists("capture.png"):
        os.remove("capture.png")
    websiteurl = request.POST.get("websiteurl")
    # chrome driverを定義
    options = Options()
    # headlessモード（ブラウザを立ち上げない）
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    driver.get(websiteurl)
    # ウィンドウを最大化
    driver.maximize_window()
    time.sleep(2)
    # 画面最下部まで読み込む
    S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
    driver.set_window_size(S("Width"), S('Height'))
    time.sleep(2)
    # スクリーンキャプチャ取得
    driver.find_elements_by_tag_name("body")[0].screenshot("capture.png")
    # driverを閉じる
    driver.quit()
    return FileResponse(open('capture.png', "rb"), as_attachment=True, filename="capture.png")
