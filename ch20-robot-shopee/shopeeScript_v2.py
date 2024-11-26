import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 設置日誌
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

# 初始化瀏覽器
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

# 初始化驅動
driver = webdriver.Chrome(options=options)

# 進入要搶的咖啡頁面
driver.get(
    "https://shopee.tw/Apple-iPhone-16-128GB-A18-%E8%98%8B%E6%9E%9C-%E5%8E%9F%E5%BB%A0-%E9%80%81%E9%96%80%E5%B8%82%E4%BF%9D%E8%B2%BC%E5%85%8C%E6%8F%9B%E5%88%B8-%E7%A5%9E%E8%85%A6%E7%94%9F%E6%B4%BB-i.54598032.26110824009?xptdk=142b9d01-5b26-465a-94ca-687659173036"
)


# 選擇器
SELECTORS = {
    "product_button": "button[aria-label='11.25商城狂購節(不挑色)']",  # 11.25商城狂購節(不挑色), 白(現貨)
    "buy_now_button": "button[class='btn btn-solid-primary btn--l YuENex eFAm_w']",
    "checkout_button": "button[class='shopee-button-solid shopee-button-solid--primary']",
    "place_order_button": "button[class='stardust-button stardust-button--primary stardust-button--large LtH6tW']",
}


# 工具函式：等待並點擊
def wait_and_click(selector, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        ).click()
        logger.info(f"「成功」點擊按鈕: {selector}")
    except Exception as e:
        logger.error(f"無法點擊按鈕 {selector}: {e}")


# 按照流程執行
wait_and_click(SELECTORS["product_button"])  # 選定商品
wait_and_click(SELECTORS["buy_now_button"])  # 直接購買
time.sleep(0.5)  # 若必要可保留短暫靜態等待
wait_and_click(SELECTORS["checkout_button"])  # 去買單
time.sleep(0.2)
wait_and_click(SELECTORS["place_order_button"])  # 下訂單 (測試階段可註解)
