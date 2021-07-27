import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException



executable_path = "../saucedemo_auto/chromedriver.exe"

chrome_options = Options()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
wait = WebDriverWait(driver, 5)

try:
    # visiting the homepage
    print("- Visiting Sauce Demo")
    driver.get("https://www.saucedemo.com/")

    # screenshot function
    def screenshot(imageName):
        driver.maximize_window()
        driver.get_screenshot_as_file(imageName)
        print ("Verified via screenshot")
        
    # page wait time function
    def holup(sec):
        time.sleep(sec)

    # screenshot website
    screenshot("../saucedemo_auto/images/loginscreen.png")

    # username input
    username = driver.find_element_by_id("user-name").send_keys("standard_user")
    holup(1)

    # password input
    password = driver.find_element_by_id("password").send_keys("secret_sauce")
    holup(1)


    # clicking log-in
    login = driver.find_element_by_id("login-button").click()
    holup(2)

    # screenshot all items available
    screenshot("../saucedemo_auto/images/items.png")

    # add items to cart function
    def addToCart(WebElement):
        WebElement = driver.find_element_by_id(WebElement).click()

    addToCart("add-to-cart-sauce-labs-backpack")
    holup(1)
    addToCart("add-to-cart-sauce-labs-bolt-t-shirt")
    holup(1)
    addToCart("add-to-cart-sauce-labs-fleece-jacket")
    holup(1)

    # navigate to Cart Page
    cartPage = driver.find_element_by_class_name("shopping_cart_badge").click()
    holup(2)

    # screenshot cart
    screenshot("../saucedemo_auto/images/cartItems.png")

    # verify cart items
    item1 = driver.find_element_by_xpath('//*[@id="item_4_title_link"]/div').text
    item2 = driver.find_element_by_xpath('//*[@id="item_1_title_link"]/div').text
    item3 = driver.find_element_by_xpath('//*[@id="item_5_title_link"]/div').text
    print("List of items in the cart: " + '\n' + item1 + '\n' + item2 + '\n' + item3)

    # checkout
    checkout = driver.find_element_by_id("checkout").click()
    holup(2)

    # screeshot checkout page
    screenshot("../saucedemo_auto/images/checkoutPage.png")

    # input info
    firstName = driver.find_element_by_id("first-name").send_keys("Doja")
    holup(1)
    lastName = driver.find_element_by_id("last-name").send_keys("Cat")
    holup(1)
    zipCode = driver.find_element_by_id("postal-code").send_keys("12321")
    holup(1)
    # submit info
    submit = driver.find_element_by_id("continue").click()
    holup(2)

    # verify payment info
    payment = driver.find_element_by_xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[2]').text
    print("Your payment information: " + payment)

    # verify shipping information
    shipping = driver.find_element_by_xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[4]').text
    print("Your shipping information: " + shipping)

    # verify total:
    total = driver.find_element_by_xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[7]').text
    print(total)
    
    # screenshot delivery information
    screenshot("../saucedemo_auto/images/deliveryInfo.png")

    # click finish
    confirm = driver.find_element_by_id("finish").click()
    holup(2)

    # verify order message
    thanks = driver.find_element_by_xpath('//*[@id="checkout_complete_container"]/h2').text
    if thanks == 'THANK YOU FOR YOUR ORDER':
        print("Order completed.")
    else:
        print("something went wrong.")

    # screenshot order page
    screenshot("../saucedemo_auto/images/thankYouPage.png")
finally:
    driver.quit()


