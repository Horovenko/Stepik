from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

try:
   

        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        button = browser.find_element_by_id("book")

        WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100"))
     
        button.click()

        x = browser.find_element_by_id("input_value").text
    
    
        y = str(math.log(abs(12*math.sin(int(x)))))
    
        answer = browser.find_element_by_id("answer").send_keys(y)

        button1 = browser.find_element_by_id("solve")

        browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button1)
        button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


