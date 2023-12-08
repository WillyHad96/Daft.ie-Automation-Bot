# LIBRARIES

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import schedule

# CONSTANTS

home_page_url = "https://www.daft.ie/property-for-rent/dublin-city?radius=5000&rentalPrice_from=500&rentalPrice_to=2000"
applied_urls = set()
announcement_number = 1

# FUNCTIONS

def click_element(driver, by, locator):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, locator)))
        element.click()
    except TimeoutException:
        print(f"Element with {by}='{locator}' not found within the specified time.")
    except NoSuchElementException:
        print(f"Element with {by}='{locator}' not found. Check the selectors.")

def scroll_down(driver, pixels=400):
    try:
        driver.execute_script(f"window.scrollTo(0, {pixels});")
    except:
        print("Scroll down was not possible.")

def return_to_main_page(driver):
    # RETURN TO MAIN PAGE
    time.sleep(1)
    driver.back()
    time.sleep(1)

def open_chrome():
    # OPEN CHROME
    driver = webdriver.Chrome()
    driver.get(home_page_url)
    driver.maximize_window()
    time.sleep(0.5)
    return driver

def sign_in(driver):

    # ACCEPT ALL COOKIES BUTTON
    click_element(driver, By.XPATH, "//span[contains(text(), 'Accept All')]")
    time.sleep(0.5)

    # CLICK SIGN IN BUTTON
    click_element(driver, By.XPATH, '//*[@id="__next"]/header/div/div[2]/div[3]/ul/li/a')
    time.sleep(0.5)

    # ENTER CREDENTIALS
    username_locator = (By.CSS_SELECTOR, "input[name='username']")
    password_locator = (By.CSS_SELECTOR, "input[name='password']")

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(username_locator))
    username.clear()
    username.send_keys("Your email")

    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(password_locator))
    password.clear()
    password.send_keys("Your password")

    sign_in_button_locator = (By.XPATH, '//*[@id="login"]')
    click_element(driver, *sign_in_button_locator)
    time.sleep(0.5)

def search_and_click(driver, announcement_number):

    # SEARCH AND CLICK
    announcement_locator = (By.XPATH, f'//*[@id="__next"]/main/div[3]/div[1]/ul/li[{announcement_number}]/a/div[2]/div[1]/div[2]/div')
    click_element(driver, *announcement_locator)

    #CHECK THE URL 
    current_url = driver.current_url
    return current_url


def apply(driver):

    # SCROLL DOWN
    scroll_down(driver)

    #CLICK THE EMAIL AGENT BUTTON
    try:
        email_agent_locator = (By.XPATH, '//*[@id="__next"]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/button/div/span')
        click_element(driver, *email_agent_locator,)
    except:
        return_to_main_page()

    #FILL THE  EMAIL AGENT FORM
    time.sleep(1)
    first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keyword1"]')))
    #first_name.clear()                                                                  
    first_name.send_keys("Your First Name")

    last_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keyword2"]')))
    #last_name.clear()
    last_name.send_keys("Your Last Name")

    email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keyword3"]')))
    #email.clear()
    email.send_keys("youremail@yourdomain.com")

    phone_number = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keyword4"]')))
    #phone_number.clear()
    phone_number.send_keys("Your Phone Number")
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 2500);")  #SCROLL DOWN

    number_of_adults_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-wrapper-adultTenants"]/div/div/div/button[2]'))).click()

    no_pets_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hasPets"]/label[2]'))).click()

    moveindates_expandable_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="moveInDate"]'))).click()
    selectdate_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-wrapper-moveInDate"]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[5]'))).click()

    message = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="message"]')))
    message.clear()
    message.send_keys("We are Guillermo and Carlota, a lovely Spanish couple that would love to live in your appartment. I am 28 and I work at Datadog as an IT Customer Support Engineer and she works as a Visual Merchandiser at Zara and we are very interested in your appartment. We use to live in Cork for two year but we think Dublin is a most exciting city to live in and we are currently sharing an appartment with another couple but we would love to have our own one.")


    driver.execute_script("window.scrollTo(0, 2500);")  #SCROLL DOWN
    send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contact-form-modal"]/div[2]/form/div/div[9]/div/button'))).click()

    #CLICK THE X BUTTON
    time.sleep(1)
    x_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contact-form-modal"]/div[1]/button'))).click()

    #RETURN TO MAIN PAGE
    return_to_main_page(driver)


# MAIN PROGRAM

driver = open_chrome()
sign_in(driver)

while announcement_number <= 20:  # LOOP FOR THE DIFFERENT ANNOUNCEMENTS
    current_url = search_and_click(driver, announcement_number)

    if current_url not in applied_urls: # FILTER TO APPLY OR NOT FOR THE ANNOUNCEMENT
        apply(driver)
        applied_urls.add(current_url)
        
    return_to_main_page(driver)
    announcement_number += 1


# FINISH THE PROGRAM

driver.quit()


# SCHEDULE JOB
#schedule.every().monday.to("friday").at("07:00").to("22:00").every(1).minutes.do(search_and_click)

# RUN THE SCHEDULER
#while True:
#    schedule.run_pending()
#    time.sleep(1)
