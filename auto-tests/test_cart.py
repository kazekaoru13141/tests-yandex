import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Поиск товаров")
@allure.story("Поиск товара по артикулу")
def test_search_product_by_article():
    driver=webdriver.Chrome()
    wait=WebDriverWait(driver,10)
    try:
        with allure.step("Открыть Яндекс Маркет"):
            driver.get("https://market.yandex.ru/")
            driver.maximize_window()
        with allure.step("Ввести артикул товара"):
            sear=wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "header-search")
                )
            )
            sear.send_keys("5325675802")
            sear.send_keys(Keys.ENTER)
        with allure.step("Проверить отображение найденного товара"):
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), '5325675802')]")
                )
            )
    finally:
        driver.quit()