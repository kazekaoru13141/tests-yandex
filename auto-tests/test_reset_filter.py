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
    wait =WebDriverWait(driver, 10)
    try:
        with allure.step("Открыть Яндекс Маркет"):
            driver.get("https://market.yandex.ru/")
            driver.maximize_window()
        with allure.step("Найти плед"):
            sear=wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "header-search")
                )
            )
            sear.send_keys("плед")
            sear.send_keys(Keys.ENTER)
        with allure.step("Открыть фильтры"):
            filters_button=wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='allFiltersButton']")
                )
            )
            filters_button.click()
        with allure.step("Выбрать фильтр хлопок"):
            cotton=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='хлопок']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                cotton
            )
            driver.execute_script("arguments[0].click();", cotton)
        with allure.step("Выбрать фильтр отсутствует"):
            otsut=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='отсутствует']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                otsut
            )
            driver.execute_script("arguments[0].click();", otsut)
        with allure.step("Применить фильтры"):
            apply_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='applyFiltersButton']")
                )
            )
            apply_button.click()
        with allure.step("Снова открыть фильтры"):
            filters_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='allFiltersButton']")
                )
            )
            filters_button.click()
        with allure.step("Сбросить фильтры"):
            res_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[.//span[contains(text(),'Сбросить все фильтры')]]")
                )
            )
            res_button.click()
        with allure.step("Применить сброс"):
            apply_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='applyFiltersButton']")
                )
            )
            apply_button.click()
    finally:
        driver.quit()