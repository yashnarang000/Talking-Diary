# Importing required modules

import time
from os import path

# Setting up WebDriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")

options = Options()

# Getting Data Directory Path

# with open('Data/data_dir.dat', 'r') as f:
#     data_dir = f.read()

# Using WebDriver in existing chrome profile

chrome_profile = r'C:\Users\scien\AppData\Local\Google\Chrome\User Data\Profile 69'
options.add_argument(f"user-data-dir={chrome_profile}")

options.add_argument("--headless=new")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# Setting up the website

driver.get("https://pi.ai/talk")

# Creating classes

class Voice:
    pass

class Chat:
    pass

class Misc:
    pass


# Voice Selector Function

def voice_select(voice):
    try:
        if int(voice) <= 8 and int(voice) >= 1:
            profile = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/a[2]')
            profile.click()

            time.sleep(1)

            voice_settings = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/a[2]')
            voice_settings.click()

            time.sleep(1)

            voice_num = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div/div[3]/div[2]/div/button[{voice}]')
            voice_num.click()

            time.sleep(9)

            profile = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/a[2]')
            profile.click()
        
        else:
            print("Voice unavailable.")
    
    except:
        print("Voice unavailable.")

# Voice Toggle Function

def voice_toggle(v):
    try:
        switch = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[1]')
        switch.click()
    except:        
        switch = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]')
        switch.click()

        time.sleep(1)
        try:
            voice = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[{v}]')
            voice.click()
        except:
            pass

# Wait for dynamic text to load

def misc_dynamic(element):
    while True:
        old = element.text
        time.sleep(1)
        new = element.text

        if old == new:
            return new
        
        else:
            pass


Misc.dynamic = lambda element: misc_dynamic(element)

def popup_handler():
    popup_handler = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div/div[2]/button')
    popup_handler.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div/div/div[2]/button'))
    )

    no_account = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div/div/div[2]/button')
    no_account.click()


# Chat Functions

def chat_input(input):

    textarena = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea')
    textarena.send_keys(input + Keys.ENTER)

def chat_output():
    def chat_output_process():
        global final_output
        while True:
            response = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div')
            final_output = Misc.dynamic(response)

            if final_output == "":
                pass
            else:
                break
    try:
        chat_output_process()

    except:
        popup_handler()
        chat_output_process()

    return final_output

# Creating a wait function

def misc_wait():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea'))
    )

# Creating screenshot function

def misc_screenshot(n):
    driver.save_screenshot(f'screenshot{n}.png')

# Creating a quit function

def misc_quit():
    driver.quit()

def misc_getname():
    profile = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/a[2]')
    profile.click()

    Misc.screenshot(3)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[1]/div/div/h1'))
    )

    Misc.screenshot(4)

    name = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[1]/div/div/h1')
    name = name.text

    profile.click()

    return name

# Assignning functions to their classes

Voice.select = voice_select
Voice.toggle = voice_toggle
Chat.input = chat_input
Chat.output = chat_output
Misc.wait = misc_wait
Misc.quit = misc_quit
Misc.screenshot = misc_screenshot
Misc.getname = misc_getname

# Login Function

def misc_login(facebook_id, facebook_pass):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/a[2]'))
        )

        profile = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/a[2]')
        profile.click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/a[1]'))
        )

        account = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/a[1]')
        account.click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div[3]/div[2]/div/div/div/div/div/div[1]/button[2]'))
        )

        facebook = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[3]/div[2]/div/div/div/div/div/div[1]/button[2]')
        facebook.click()

    except:

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/button'))
            )

        login = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/button')
        login.click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div/div/div/div/div[1]/button[2]'))
            )
        
        facebook = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div/div/div/div/div[1]/button[2]')
        facebook.click()

    address = driver.find_element(By.XPATH, '//*[@id="m_login_email"]')
    address.send_keys(facebook_id)

    password = driver.find_element(By.XPATH, '//*[@id="m_login_password"]')
    password.send_keys(facebook_pass)

    time.sleep(1)

    login = driver.find_element(By.XPATH, '//*[@id="login_password_step_element"]/button')
    login.click()

    try:
        time.sleep(10)

        cont = driver.find_element(By.NAME, '__CONFIRM__')
        cont.click()
    
    except:
        pass


    try:

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div/div[2]/button'))
        )

        nothanks = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div/div[2]/button')
        nothanks.click()

    except:
        pass

    with open(r'Data\loginStatus.dat', 'w') as f:
        f.write("")


Misc.login = lambda facebook_id, facebook_pass: misc_login(facebook_id, facebook_pass)

if path.exists(rf'Data\loginStatus.dat'):
    Misc.wait()
    Misc.username = Misc.getname()

else:
    pass