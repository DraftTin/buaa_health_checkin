from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

try_count = 0

def get_hint_show(driver):
    try:
        hint_show = driver.find_element(by=By.CLASS_NAME, value='alert')
        if hint_show.value_of_css_property('display') == 'none':
            hint_show = None
    except Exception as e:
        hint_show = None

def checkin():
    DRIVER_PATH = '../chromedriver'
    with open('../account.json') as ac_file:
        ac = json.load(ac_file)

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get('https://app.buaa.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.buaa.edu.cn%2Fsite%2FbuaaStudentNcov%2Findex')
    # 登录部分
    inputs = driver.find_elements(by=By.TAG_NAME, value='input')
    account_field = inputs[0]
    password_field = inputs[1]
    login_btn = driver.find_element(by=By.CLASS_NAME, value='btn')

    account_field.send_keys(ac.get('account'))
    password_field.send_keys(ac.get('password'))
    login_btn.click()
    time.sleep(6)
    
    # 填写表单, 判断是否已经提交过了
    submit_btn = driver.find_element(by=By.CLASS_NAME, value='sub-info')
    if submit_btn.text == '您已提交过信息':
        return True
    # 是否住宿
    living_on_campus_today = driver.find_element(by=By.NAME, value='sfzs')
    living_on_campus_today.find_elements(By.TAG_NAME, 'span')[2].click()
    time.sleep(1)
    hint_show = get_hint_show(driver)
    if hint_show:
        confirm_btn = hint_show.find_element(by=By.TAG_NAME, value='a')
        confirm_btn.click()
    # 健康情况是否正常
    in_health = driver.find_element(by=By.NAME, value='brsfzc')
    in_health.find_elements(By.TAG_NAME, 'span')[2].click()
    # 接触环境是否正常
    in_normal_env = driver.find_element(by=By.NAME, value='sfzc_14')
    in_normal_env.find_elements(By.TAG_NAME, 'span')[2].click()
    # 所在地点
    position = ("39.97805900941237", "116.34515751812742")
    location_btn = driver.find_element(by=By.TAG_NAME, value='input')
    driver.execute_script("window.navigator.geolocation.getCurrentPosition=function(success){" +
                           "var position = {\"coords\" : {\"latitude\": \"" + position[0] + "\",\"longitude\": \""
                           + position[1] + "\"}};" +
                           "success(position);}")
    location_btn.click()
    time.sleep(2)
    # 提交
    submit_btn = driver.find_element(by=By.CLASS_NAME, value='sub-info')
    submit_btn.click()
    time.sleep(1)
    confirm_submit_btn = driver.find_elements(by=By.CLASS_NAME, value='wapcf-btn')[1]
    confirm_submit_btn.click()
    time.sleep(1)
    hint_show = get_hint_show(driver)
    if hint_show:
        confirm_btn = hint_show.find_element(by=By.TAG_NAME, value='a')
        confirm_btn.click()
        return True
    try_count += 1
    if try_count <= 5:
        return checkin()
    # time.sleep(10)
    return False


if __name__ == '__main__':
    checkin()


