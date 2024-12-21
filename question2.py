from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.myntra.com")
wait = WebDriverWait(driver, 20)

try:
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='desktop-searchBar']")))
    search_box.clear()
    search_box.send_keys("Plant")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    items = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'product-base')]")))

    if len(items) >= 6:
        driver.execute_script("arguments[0].scrollIntoView();", items[5])
        items[5].click()
        time.sleep(3)

        add_to_bag = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='pdp-add-to-bag pdp-button pdp-flex pdp-center']")))
        driver.execute_script("arguments[0].click();", add_to_bag)
        time.sleep(3)

        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Bag']")))
        driver.execute_script("arguments[0].scrollIntoView();", cart_button)
        cart_button.click()
        time.sleep(3)

        remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Remove']")))
        driver.execute_script("arguments[0].scrollIntoView();", remove_button)
        remove_button.click()
        time.sleep(3)

    else:
        print("Less than 6 items found on the search results page.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Attempting to debug the issue...")

finally:
    driver.quit()
