from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests
webhook = "https://hooks.slack.com/services/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"
mechkey = {
    "text": 'Your keyboard is available at MechanicalKeyboards, get it quick'
}
microless = {
    "text": 'Your keyboard is available at Microless, get it quick'
}
chrome_options = Options()
chrome_options.add_argument('-headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
while True:


    driver.get('https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=5461&mkref=yzyfe1u')
    assert "Ducky" in driver.title
    keyswitch = Select(driver.find_element_by_name('option[1998]'))
    keyswitch.select_by_visible_text('Cherry MX Brown')
    element = driver.find_element_by_id('ebj_available')
    if element.text != 'Pre-Order Only':
        requests.post(webhook, json.dumps(mechkey))
        break
    else:
        print('test complete')

    driver.get('https://uae.microless.com/product/ducky-one-2-sf-65-cherry-blue-rgb-switch-type-c-usb-rgb-backlit-pbt-double-shot-black-keycaps-black-top-case-white-bottom-case-rgb-led-dkon1967st-buspdazt1/')
    assert "Ducky" in driver.title
    try:
        element = driver.find_element_by_class_name('instock-lable')
    except NoSuchElementException:
        pass
    else:
        requests.post(webhook, json.dumps(microless))
        break

    time.sleep(3600)
