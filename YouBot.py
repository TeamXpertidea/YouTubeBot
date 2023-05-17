import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

from csv import reader


def Connecting_To_Browser(id_str, pass_str):
    browser = uc.Chrome()
    try:
        browser.get("https://gmail.com")

        email_field = browser.find_element("id","identifierId")
        email_field.clear()
        time.sleep(2)

        email_field.send_keys(id_str)

        email_next_button = browser.find_element("id","identifierNext")
        email_next_button.click()

        time.sleep(2)

        password_field = browser.find_element(By.NAME,"Passwd")   
        # password_field.clear()

        password_field.send_keys(pass_str)
        time.sleep(2)
        password_next_button = browser.find_element("id","passwordNext")
        password_next_button.click()

        time.sleep(10)
        
        print('Login Successful...!!')


        # Go to the YouTube URL
        # youtube_url="https://www.youtube.com/watch?v=s4ZUkwe0ZTI"

        youtube_url="https://www.youtube.com/watch?v=BagZCVtaCPk"
        browser.get(youtube_url)
        browser.implicitly_wait(1000)

        # WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
        # (By.XPATH, "//button[@aria-label='Play']"))).click()

        subscribe_next_button = browser.find_element("id","segmented-like-button")
        subscribe_next_button.click()
        time.sleep(20)
        print("channel liked")
        # Close the browser
        browser.quit()
    except NoSuchElementException:
        print("No Such Element Exception")
        browser.quit()


with open('details.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

ids_pass_list = list_of_rows


for i in range(1,len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    
    Connecting_To_Browser(id_str,id_pass)
