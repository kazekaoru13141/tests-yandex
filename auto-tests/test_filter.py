import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Фильтрация товаров")
@allure.story("Применение фильтров к результатам поиска")
def test_apply_filters():
    driver=webdriver.Chrome()
    wait=WebDriverWait(driver, 10)
    try:
        with allure.step("Открыть Яндекс Маркет"):
            driver.get("https://market.yandex.ru/")
            driver.maximize_window()
        with allure.step("Выполнить поиск товара"):
            search=wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "header-search")
                )
            )
            search.send_keys("плед")
            search.send_keys(Keys.ENTER)
        with allure.step("Открыть все фильтры"):
            filters_button =wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='allFiltersButton']")
                )
            )
            filters_button.click()
        with allure.step("Выбрать фильтр «хлопок»"):
            cotton=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='хлопок']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                cotton
            )
            wait.until(
                EC.visibility_of(cotton)
            )
            driver.execute_script(
                "arguments[0].click();",
                cotton
            )
        with allure.step("Проверить выбор фильтра «хлопок»"):
            wait.until(
                lambda d: cotton.get_attribute("aria-selected") == "true"
            )
        with allure.step("Выбрать фильтр «кружево»"):
            lace=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='кружево']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                lace
            )
            wait.until(
                EC.visibility_of(lace)
            )
            driver.execute_script(
                "arguments[0].click();",
                lace
            )
        with allure.step("Проверить выбор фильтра «кружево»"):
            wait.until(
                lambda d: lace.get_attribute("aria-selected") == "true"
            )
        with allure.step("Применить выбранные фильтры"):
            show_products =wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='applyFiltersButton']")
                )
            )
            show_products.click()
        with allure.step("Проверить отображение результатов"):
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'плед')]")
                )
            )
    finally:
        driver.quit()