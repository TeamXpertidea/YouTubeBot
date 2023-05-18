
import time
from csv import reader
from selenium.webdriver.common.by import By
from tqdm import tqdm
import   undetected_chromedriver as uc

def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        browser = uc.Chrome()
        try:
            browser.get('https://www.gmail.com/')

            email_field = browser.find_element("id","identifierId")
            email_field.clear()
            

            email_field.send_keys(id_str)

            email_next_button = browser.find_element("id","identifierNext")
            email_next_button.click()

            time.sleep(2)

            password_field = browser.find_element(By.NAME,"Passwd")
            password_field.clear()

            password_field.send_keys(pass_str)

            password_next_button = browser.find_element("id","passwordNext")
            password_next_button.click()

            time.sleep(3)

            browser.get('https://www.youtube.com/watch?v=FVumnHy5Tzo')

            browser.implicitly_wait(1000)
            # subscribe_next_button = browser.find_element(By.CLASS_NAME,"style-scope ytd-subscribe-button-renderer")
            # subscribe_next_button.click()
            subscribe_next_button = browser.find_element("id","segmented-like-button") # press like button 
            subscribe_next_button.click()

            subscribe_next_button = browser.find_element("id","subscribe-button") # press subscribe button
            subscribe_next_button.click()


            time.sleep(10)
            browser.quit()
        except Exception as e:
            print(e)
            browser.quit()
    else:
        print("Either ID or PASSWORD is null")

   

with open('details.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print("Total Ids and Passwords: ", len(list_of_rows)-1)
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

progress_bar = tqdm(total=total_Len)
for i in range(1,len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print(i)
    print("Login Id: ", id_str)
    print("Login Password: ", id_pass)

    Connecting_To_Browser(id_str, id_pass)
    progress_bar.update(1)

progress_bar.close()
