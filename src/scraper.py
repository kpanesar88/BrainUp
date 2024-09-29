import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scraper(sample_City,what_to_search):
    listing_name = "Test"
    listing_description = "Test-description"
    listing_address = "Test-address"

    # sample_City = "ottawa"
    # what_to_search = "Painting Classes"

    # Initialize the webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open a webpage
    driver.get('https://www.kijiji.ca/')  # Replace with the target webpage URL

    # Maximize the browser window
    driver.maximize_window()
    #clicking location
    location = driver.find_element(By.CSS_SELECTOR, '#global-header > div > div.sc-e36a51ed-3.irgRLE > div.sc-ca5b14e9-0.eWUdkQ > button')
    location.click()

    #select_location
    time.sleep(1)
    import traceback
    try:
        location_select = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="modal-overlay"] input[type="search"]'))
        )
        print(location_select.get_attribute("id"))
        # downshift-22-input
    #location_select = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
        time.sleep(1)
        for i in range(30):
        # try:
        #     location_select = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="search"]'))
        #     )

            location_select.send_keys(Keys.BACKSPACE)
    except Exception as e:
        print(traceback.format_exc())
        print('expec')
        print(f"Error: {e}")

    time.sleep(1)
    location_select.send_keys(sample_City)
    time.sleep(1)
    location_select.send_keys(Keys.RETURN)
    time.sleep(1)
    apply =driver.find_element(By.CSS_SELECTOR, 'body > reach-portal > div:nth-child(2) > div > div > div > footer > button')
    time.sleep(1)
    apply.click()

    #Searching Main Lesson
    search_bar = driver.find_element(By.ID, 'global-header-search-bar-input')
    search_bar.send_keys(what_to_search)  # Replace with desired search text
    search_bar.send_keys(Keys.RETURN)  # Simulates hitting the Enter key


    #Clicking top listing
    try:
        top_add = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-testid="listing-card-list-item-0"]'))
        )
        # Click the listing item
        top_add.click()
    except Exception as e:
        print(f"Error: {e}")

    #Saving name
    try:
        title = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#ViewItemPage > div:nth-child(5) > div > div.mainColumn-3280634428 > div > h1'))
        )

        listing_name = title.text
        print(f"Title: {listing_name}")
    except Exception as e:
        print(f"Error: {e}")

    #address
    try:
        address = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#ViewItemPage > div:nth-child(5) > div > div.sidebarColumn-3280634428 > div > div.locationContainer-1255831218 > span'))
        )

        listing_address = address.text
        print(f"Address: {listing_address}")
    except Exception as e:
        print(f"Error: {e}")

    #show more clicker
    try:
        show_more = driver.find_element(By.CSS_SELECTOR, '#vip-body > div.showMoreWrapper-3595478869 > button')
        show_more.click()
    except Exception as e:
        pass
    #Description
    try:
        desc = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#vip-body > div.showMoreWrapper-3595478869.showMoreWrapper__expanded-915389175 > div.showMoreChild-3209653031 > div > div'))
        )

        listing_description = desc.text
        print(f"Description: {listing_description}")
        #html_content = desc.get_attribute('innerHTML')
        #print(f"HTML Content: {html_content}")

    except Exception as e:
        #print ('oh wait')
        print(f"Error: {e}")

    current_url = driver.current_url


    open_image = driver.find_element(By.CSS_SELECTOR, '#mainHeroImage > div.generalOverlay-377726457')
    open_image.click()

    image = driver.find_element(By.XPATH, '//*[@id="reset"]/body/div[11]/div/div/div[2]/ul/li[1]/div/div[2]/div/picture/img')
    image_source = image.get_attribute('src')
    #print(image_source)




    # Close the driver
    time.sleep(2)
    driver.quit()
    return [listing_name, listing_address,listing_description, image_source,current_url]
