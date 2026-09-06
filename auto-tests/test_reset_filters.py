import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Фильтрация товаров")
@allure.story("Сброс выбранных фильтров")
def test_reset_filters():
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
            filters_button=wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='allFiltersButton']")
                )
            )
            filters_button.click()
        with allure.step("Выбрать фильтр «хлопок»"):
            cotton =wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='хлопок']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                cotton
            )
            driver.execute_script(
                "arguments[0].click();",
                cotton
            )
        with allure.step("Выбрать фильтр «отсутствует»"):
            absent=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='отсутствует']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                absent
            )
            driver.execute_script(
                "arguments[0].click();",
                absent
            )
        with allure.step("Применить фильтры"):
            show_products = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='applyFiltersButton']")
                )
            )
            show_products.click()
        with allure.step("Повторно открыть все фильтры"):
            filters_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='allFiltersButton']")
                )
            )
            filters_button.click()
        with allure.step("Сбросить все фильтры"):
            reset_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[.//span[contains(text(),'Сбросить все фильтры')]]")
                )
            )
            reset_button.click()
        with allure.step("Применить сброс фильтров"):
            show_products =wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='applyFiltersButton']")
                )
            )
            show_products.click()
    finally:
        driver.quit()