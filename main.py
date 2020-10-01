from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from decouple import config
import page
import time


def wait(sec, xpath_element):
    try:
        element = WebDriverWait(driver, sec).until(
            EC.visibility_of_element_located((By.XPATH, xpath_element))
            )
    except:
        print('Error')

def find_element(driver, xpath):
    return driver.find_element_by_xpath(xpath)

opt = Options()
opt.add_experimental_option("prefs", {
      "profile.default_content_setting_values.geolocation": 1   # 1 to low 2 to block
})

driver = webdriver.Chrome(options=opt)

driver.get('https://tinder.com/')
driver.maximize_window()
time.sleep(6)

login_button = find_element(driver, page.login_button)
login_button.click()

time.sleep(15)

login_with_google = find_element(driver, page.google_login_button)
login_with_google.click()

driver.switch_to.window(driver.window_handles[-1])

time.sleep(10)
email_input = find_element(driver, page.google_email_input)

time.sleep(1)
email_input.send_keys('myemail@gmail.com')
time.sleep(2)

email_input.send_keys(Keys.RETURN)
time.sleep(4)

password_input = find_element(driver, page.google_password_input)

time.sleep(4)
password_input.send_keys('myPassword')
password_input.send_keys(Keys.RETURN)

time.sleep(4)

driver.switch_to.window(driver.window_handles[0])

time.sleep(8)

#POP-UPS
accept_cookies = find_element(driver, page.accept_cookies)
accept_cookies.click()
time.sleep(4)
allow_location = find_element(driver, page.allow_location_button)
allow_location.click()
time.sleep(4)
not_interested = find_element(driver, page.not_interested_button)
not_interested.click()
time.sleep(4)
gold_maybe_later_button = find_element(driver, page.gold_maybe_later_button)
gold_maybe_later_button.click()
time.sleep(4)

main_pic = find_element(driver, page.main_image)
like_button = find_element(driver, page.LIKE)

if main_pic.is_displayed():
    while(True):
        try:
            like_button.click()
            time.sleep(2)
        except:
            try:
                print('Something went wrong, trying to press not interested')
                time.sleep(1)
                not_interested_during_swipe = find_element(driver, page.not_interested_during_swipe)
                not_interested_during_swipe.click()
                continue
            except:
                try:
                    print('Trying to press back to matching.')
                    time.sleep(1)
                    back_to_matching = find_element(driver, page.back_to_matching_button)
                    back_to_matching.click()
                    continue
                except:
                    driver.close()
                    break
            # driver.close()

else:
    print('Could not find the main pic.')
    # driver.close()