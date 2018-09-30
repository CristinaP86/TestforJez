from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from faker import Faker

class TestForJez:
    def cristina_test(self):
        baseurl = 'https://www.google.com/'
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        pixitmedia_search = driver.find_element_by_id('lst-ib')
        pixitmedia_search.send_keys('pixitmedia')
        time.sleep(1)
        pixitmedia_search.send_keys(Keys.ENTER)
        time.sleep(3)

        open_site = driver.find_element_by_xpath('//a[@href="https://www.pixitmedia.com/"]')
        open_site.click()
        time.sleep(3)

        products_menu = driver.find_element_by_link_text('PRODUCTS')
        products_menu.click()
        time.sleep(3)

        pixtar_search = driver.find_element_by_xpath('//a[text()= "PixStor Search"]')
        pixtar_search.click()
        time.sleep(3)

        view_datasheet = driver.find_element_by_xpath("//span[text()='VIEW DATASHEET']")
        view_datasheet.click()
        time.sleep(3)

        pdf_display = driver.current_url
        assert 'https://www.pixitmedia.com/wp-content/uploads/2018/03/PixStor-Search-Datasheet.pdf' in pdf_display
        time.sleep(3)

        driver.execute_script("window.history.go(-1)")
        time.sleep(5)

        contact_us = driver.find_element_by_link_text('CONTACT US')
        contact_us.click()
        time.sleep(3)

        first_name = driver.find_element_by_xpath('//input[@id="field_qh4icy2"]')
        first_name.send_keys('Cristina')

        last_name = driver.find_element_by_name('item_meta[7]')
        last_name.send_keys('Test')

        email_address = driver.find_element_by_id('field_29yf4d2')
        random_email = Faker()
        email_address.send_keys(random_email.email())

        organisation_field = driver.find_element_by_id('field_fz52u')
        organisation_field.send_keys('Testing Land')

        telephone_num = driver.find_element_by_id('field_yuy03')
        telephone_num.send_keys('07530000000')

        subject_name = driver.find_element_by_id('field_e6lis62')
        subject_name.send_keys('Test For Jez')

        text_message = driver.find_element_by_id('field_9jv0r12')
        text_message.send_keys('This is a test for Jez')

        send_form = driver.find_element_by_xpath('//button[@type="submit"]')
        send_form.click()
        time.sleep(3)

        message_success = driver.find_element_by_xpath('//p[text()="Your responses were successfully submitted. '
                                                        'Thank you!"]')
        if message_success.is_displayed():
            print('Message was successfully sent')
        else:
            print('Please try again')
        driver.quit()


pixitmedia_test = TestForJez()
pixitmedia_test.cristina_test()

