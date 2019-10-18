from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element_by_class_name('btn-default')
button_text = button.get_attribute('innerHTML')
# print(button_text)
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_btn = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_btn)
user_message.clear()
user_message.send_keys('I am extra cooool')
button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'I am extra cooool' in output_message.text

#to close current window
chrome_browser.close()

#to close entire chrome driver
chrome_browser.quit()