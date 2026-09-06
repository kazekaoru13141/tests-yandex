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
        with allure.step("Найти товар"):
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
            var=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='хлопок']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                var
            )
            driver.execute_script("arguments[0].click();", var)
            wait.until(
                lambda d: var.get_attribute("aria-selected") == "true"
            )
        with allure.step("Выбрать фильтр кружево"):
            lace=wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[normalize-space()='кружево']]")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                lace
            )
            driver.execute_script("arguments[0].click();", lace)

            wait.until(
                lambda d: lace.get_attribute("aria-selected") == "true"
            )
        with allure.step("Применить фильтры"):
            filtr=wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[data-auto='applyFiltersButton']")
                )
            )
            filtr.click()
        with allure.step("Проверить результаты поиска"):
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'плед')]")
                )
            )
    finally:
        driver.quit()