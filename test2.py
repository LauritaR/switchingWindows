from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math
try:
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(2)
    
    button= driver.find_element(By.XPATH,'/html/body/form/div/div/button')
    button.click()
    
    new_window_switch=driver.window_handles[1]
    driver.switch_to.window(new_window_switch)
    
    x_value=driver.find_element(By.ID,'input_value').text
    
    calc_function=str(math.log(abs(12*math.sin(int(x_value)))))
    
    solve_problem=driver.find_element(By.NAME,'text').send_keys(calc_function)
    
    driver.find_element(By.XPATH,'/html/body/form/div/div/button').click()
    
    time.sleep(10)
finally:
    driver.quit()
    