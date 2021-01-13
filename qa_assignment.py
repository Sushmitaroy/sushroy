from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="C:\\Users\\Sushmita\\Downloads\\chromedriver.exe")

''' ----------- a) Assert Broken images ----------- '''

browser.get("http://the-internet.herokuapp.com/broken_images")
list_of_images = browser.find_elements(By.XPATH, "//*[@id='content']/div/img")
print("Total number of images: ",len(list_of_images))
image_files = []
for images in list_of_images:
    image_files.append(images.get_attribute('src').split("http://the-internet.herokuapp.com/")[1])

print("List of Image files names: ", image_files)

broken_images = []
count =0
for i in image_files:
    if "img/" not in i:
        broken_images.append(i)
        count += 1

print("List and count of broken images: ", broken_images, " :", count)


''' ----------- b) Select 'option 2' from the drop-down ----------- '''

browser.get("http://the-internet.herokuapp.com/dropdown")
browser.implicitly_wait(5)  # Wait for the page to load
xpath_option2 = "//*/option[text() = 'Option 2']"  # xpath for option2
xpath_dropdown = "//*[@id='dropdown']"  # xpath for the dropdown menu
browser.find_element_by_xpath(xpath_dropdown).click()  # click on the dropdown menu to open and view the options
option2 = browser.find_element_by_xpath(xpath_option2)  # Identifying the option
option2.click()  # Clicking on the option
browser.find_element_by_xpath(xpath_dropdown).click()  # click on the dropdown menu to close the list of options

# Verify that option 2 is selected
content_of_option2 = []  # empty list to store content of option 2 attribute

xpath_option2_webelement = browser.find_elements(By.XPATH, xpath_option2)  #  variable to store the
for i in xpath_option2_webelement:
    content_of_option2.append(i.get_attribute("selected"))

assert 'true' in content_of_option2, "Option 2 not selected"  # Raise AssertionError if option 2 is not selected


''' -------- c) Assert 'Hello world!' text which appears on click of 'Start' ---------- '''

browser.get("http://the-internet.herokuapp.com/dynamic_loading/1")

xpath_start_button = "//*/button[text() = 'Start']"
start = browser.find_element_by_xpath(xpath_start_button)
# element = browser.find_element_by_xpath("//*/h4[text()='Hello World!']")
element = browser.find_element_by_xpath(
    "//*/div[@class = 'example']/div[@id = 'finish']/h4[text()='Hello World!']")

print("Start should be true", start.is_displayed())
print(element.is_displayed())
browser.find_element_by_xpath(xpath_start_button).click()  # find the Start button and click on it

# xpath_option2_webelement = browser.find_elements(By.XPATH, xpath_text)  #  variable to store the
browser.implicitly_wait(10)
element2 = browser.find_elements(By.XPATH, "//h4[contains(text(),'Hello World!')]")  # for i in element2:
a = []
for i in element2:
    print(i.text)
    a.append(i.find_elements(By.XPATH, "//h4[contains(text(),'Hello World!')]"))

print(a)

print("Start should be false", start.is_displayed())


''' ----------- f) Assert forgot password success message on the page ----------- '''

browser.get("http://the-internet.herokuapp.com/forgot_password")
email = browser.find_element_by_xpath('//*[@id="email"]')    # storing webelement of e-mail text box
email.send_keys("abc@mail.com")     # Entering abc@mail.com in the e-mail text box
retrieve_password = browser.find_element_by_xpath('//*[@id="form_submit"]')  # storing webelement of retrieve password button
retrieve_password.click()     # click on retrieve password button
sucess_msg = browser.find_element_by_xpath("//*[@id='content']")   # webelement of the success message
# Verify whether the success message is visible to the user
assert sucess_msg.is_displayed() is True, "Forgot Password message not successfully triggered"


''' ------ g) Assert form validation functionality Post entering a dummy username and password ------- '''

browser.get("http://the-internet.herokuapp.com/login")
username = browser.find_element_by_xpath('//input[@id="username"]')    # storing webelement of username text box
username.send_keys('tomsmith')    # Entering value in the username text box
password = browser.find_element_by_xpath('//input[@id="password"]')    # storing webelement of username text box
password.send_keys('SuperSecretPassword!')    # Entering password in the password text box
login = browser.find_element_by_xpath('//button[@type= "submit"]')     # storing webelement of login button
login.click()   # click on login button
success_msg = browser.find_element_by_xpath('//div[@class="flash success"]')   # storing webelement of success message
# Verify whether the success message is visible to the user
assert success_msg.is_displayed() is True, "Login not successful"

'''j) Right a looped script to assert a 'successful notification" after repeated unsuccessful notification on page'''

browser.get("http://the-internet.herokuapp.com/notification_message_rendered")
browser.find_element_by_xpath('//a[text()="Click here"]').click()   # click on click here link
message = browser.find_elements(By.XPATH, "//div[@id='flash']")
message_type = []
for i in message:
    message_type.append(i.text)

while message_type[0].find('Action successful') != 0:
    browser.find_element_by_xpath('//a[text()="Click here"]').click()   # Click Click here link until Action successful
    break  # stop once Action successful

''' ------ h) Write a test to enter alphabets on this and mark it as a failure if we cannot enter on page ------ '''

browser.get("http://the-internet.herokuapp.com/inputs")
input_xpath = browser.find_element_by_xpath('//input[@type="number"]')
input_xpath.send_keys("abc")

input_type = input_xpath.get_attribute("type")  # click on click here link
if input_type == 'number':
    print("Test Failed")
else:
    print("Test Passed!")

''' -------- i) Write a test to sort the table by the amount due on page ---------- '''

browser.get("http://the-internet.herokuapp.com/tables")
due_xpath_table1 = browser.find_element_by_xpath('//*[@id="table1"]/thead/tr/th[4]/span')
due_xpath_table1.click()  # sorts the elements by clicking on due

due_xpath_table2 = browser.find_element_by_xpath('//*[@id="table2"]/thead/tr/th[4]/span')
due_xpath_table2.click()  # sorts the elements by clicking on due

''' ----------- d) Close the modal window and re-enable it on page ----------- '''

browser.get("http://the-internet.herokuapp.com/entry_ad")
browser.find_element_by_xpath("//*[@id='restart-ad']").click()   # click on click here link

try:
    browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[3]/p').click()   # click close button on modal window
    browser.find_element_by_xpath('//*[@id="modal"]/div[2]/div[3]/p').click()
except Exception as e:
    print("Exception is: ", e)
browser.close()
