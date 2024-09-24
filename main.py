import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

service = Service(executable_path="/Users/donatoprabahar/Desktop/coding_projects/selenium-project/chromedriver")
driver = webdriver.Chrome(service=service)

product_price_prefix = "productPrice"
product_prefix = "product"

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

cookies_xpath = "//div[@id='cookies']"

def click_cookie():
    while True:
        try:
            cookie = driver.find_element(By.ID, "bigCookie")
            cookie.click()

            cookies_count_element = driver.find_element(By.XPATH, cookies_xpath).text
            cookies_count = cookies_count_element.split(" ")[0]
            cookies_count = int(cookies_count.replace(",", ""))  
            print(f"Cookies: {cookies_count}")

        except StaleElementReferenceException:
            continue  
        except Exception as e:
            print(f"An error occurred in clicking: {e}")
            break

def buy_products():
    while True:
        try:
            cookies_count_element = driver.find_element(By.XPATH, cookies_xpath).text
            cookies_count = cookies_count_element.split(" ")[0]
            cookies_count = int(cookies_count.replace(",", ""))  

            for i in range(4):
                try:
                    product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

                    if not product_price.isdigit():
                        continue

                    product_price = int(product_price)

                    if cookies_count >= product_price:
                        product = driver.find_element(By.ID, product_prefix + str(i))
                        product.click()
                        print(f"Bought product {i}")
                        break

                except NoSuchElementException:
                    print(f"Product {i} not available yet")
                    continue
        except StaleElementReferenceException:
            continue  
        except Exception as e:
            print(f"An error occurred in buying products: {e}")
            break

        time.sleep(1)


click_thread = threading.Thread(target=click_cookie)
click_thread.start()

buy_thread = threading.Thread(target=buy_products)
buy_thread.start()

click_thread.join()
buy_thread.join()

driver.quit()
