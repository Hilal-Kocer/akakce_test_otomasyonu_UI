from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

def akace_otomasyon():
    try:
        USERNAME = "testhilal_123@hotmail.com"
        PASSWORD = "gfYwT&w$sGL;kE3"

        driver.get("https://www.akakce.com/")
        driver.maximize_window()
        time.sleep(2)

        login = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/a[2]").click()
        time.sleep(3)
        email_box = driver.find_element(By.ID, "life")
        email_box.send_keys(USERNAME)
        password_box = driver.find_element(By.ID, "lifp")
        password_box.send_keys(PASSWORD)

        login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/input[3]").click()

        wait = WebDriverWait(driver, 10)
        search_element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("iPhone")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        product = driver.find_element(By.CLASS_NAME, "bt_v8").click()

        follow_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ufo_v8")))
        follow_button = driver.find_element(By.CLASS_NAME, "ufo_v8")

        print("Butona tıklandı.")
        print("Test başarılı!")
    except Exception as e:
        print("Test sırasında hata oluştu!}")
    finally:
        driver.quit()
if __name__ == '__main__':
    akace_otomasyon()








