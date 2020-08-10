from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# import time
driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver.get('http://light-it-03.tk/')
login_data = {
    'name': 'Anton',
    'email': 'antonberezhnoi@gmail.com',
    'password': '1234_poc'
}

order_data = {
    'o_name': 'Laptop'
}

# def login_valid_data():
#     driver.find_element_by_css_selector('#mat-input-0').send_keys(login_data['name'])
#     driver.find_element_by_css_selector('#mat-input-1').send_keys(login_data['email'])
#     driver.find_element_by_css_selector('#mat-input-2').send_keys(login_data['password'])
#     driver.find_element_by_css_selector('.btn-submit.btn-width.mat-raised-button.valid').click()
#     driver.implicitly_wait(3)
#     el = driver.find_element_by_css_selector('.mat-button.ng-star-inserted')
#     assert el.text == login_data['name']+'keyboard_arrow_down'
#
# login_valid_data()

def place_an_order ():
    driver.find_element_by_css_selector('#mat-input-0').send_keys(login_data['name'])
    driver.find_element_by_css_selector('#mat-input-1').send_keys(login_data['email'])
    driver.find_element_by_css_selector('#mat-input-2').send_keys(login_data['password'])
    driver.find_element_by_css_selector('.btn-submit.btn-width.mat-raised-button.valid').click()
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector('.btn.btn-width.mat-raised-button').click()
    driver.find_element_by_xpath('//*[@id="name"]/div/div/input').send_keys(order_data['o_name'])
    driver.find_element_by_xpath('//*[@id="quantity"]/div/div/input').send_keys('54')
    driver.find_element_by_xpath('//*[@id="cost"]/div/div/input').send_keys('9')
    driver.find_element_by_css_selector('[id="status"]').click()
    driver.find_element_by_xpath('//*[@id="status"]/div/qa-list/div/qa-item[1]/div/div').click()
    driver.find_element_by_css_selector('[id="type"]').click()
    driver.find_element_by_xpath('//*[@id="type"]/div/qa-list/div/qa-item[1]').click()
    driver.find_element_by_xpath('//button[contains(., "Save")]').click()
    driver.refresh()
    ass_element = driver.find_element_by_css_selector('[class="wrapper ng-star-inserted"]:nth-child(1) [class="order-name"]')
    assert ass_element.text == order_data['o_name']
    driver.quit()

place_an_order ()