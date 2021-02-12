import selenium
from selenium import webdriver
from numpy import random as r

print("1: WhatsApp")
print("2: Instagram")
print("3: Facebook")
print("4: Messenger")
print("5: Exit")

choice = int(input("Enter Your Choice: " ))
if choice >5 or choice <0:
    print('Please Enter a Valid Choice:')

driver = webdriver.Firefox(executable_path=r"C:\\Users\\Admin\\Desktop\\geckodriver.exe")

if choice ==1:
    print('Scan The Qr Code by Your Phone')
    url = "https://web.whatsapp.com/"
    
    driver.get(url)
    driver.maximize_window()
    input("enter any button after scanning: ")
    driver.implicitly_wait(30)
    name = input("name or number: ")
    new =driver.find_element_by_class_name('_3FRCZ').send_keys(name)
    driver.find_element_by_css_selector('div._210SC:nth-child(1)').click()
    msglist = input('Enter Messages Seperated by Commas').split(',')
    num = int(input('Enter How Many Messages You Want to Send: '))
    for i in range(num):
        msg = r.choice(msglist)
        driver.find_element_by_css_selector("._2UL8j > div:nth-child(2)").send_keys(msg)
        driver.implicitly_wait(4)
        driver.find_element_by_css_selector("html.js.serviceworker.adownload.cssanimations.csstransitions.webp.webp-alpha.webp-animation.webp-lossless body.web div#app div._347-w._2UMYL.app-wrapper-web.os-win div.h70RQ.two div._1-iDe.Wu52Z div#main._2WG1s footer._2vJ01 div._3ee1T._1LkpH.copyable-area div._1JNuk button._1U1xa").click()

if choice ==2 :
    url = 'https://www.instagram.com'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # username = driver.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)').send_keys('merci_noo')
    username = input("Enter Your Instagram Username: ")
    driver.find_element_by_class_name('zyHYP').send_keys(username)
    password = input("Enter Your Instagram Password: ")
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
    driver.find_element_by_class_name('y3zKF     ').click()
    driver.implicitly_wait(10)

    driver.find_element_by_class_name('cmbtv').click()
    driver.implicitly_wait(10)

    driver.find_element_by_class_name('HoLwm ').click()
    driver.implicitly_wait(10)
        
    driver.find_element_by_class_name('xWeGp').click()
    driver.implicitly_wait(10)

    driver.find_element_by_class_name('EQ1Mr').click()
    driver.implicitly_wait(8)
    driver.minimize_window()

    # print('If Username is more than 1 than seperate it by comma')
    user= input('Enter Friend\'s Username: ')

    driver.maximize_window()

    driver.find_element_by_class_name('j_2Hd    ').send_keys(user)
    driver.implicitly_wait(5)
    driver.find_element_by_class_name('dCJp8 ').click()
    driver.implicitly_wait(3)
    driver.find_element_by_class_name('rIacr').click()

    
    for i in range(4):
        driver.find_element_by_css_selector('.ItkAi > textarea:nth-child(1)').send_keys('Hello')
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()


if choice ==3 :
    url="https://www.facebook.com"
    driver.get(url)
    driver.maximize_window()
    email = input("enter Your Facebook Id: ")
    driver.find_element_by_id("email").send_keys(email)
    passwrd = input("Emter Your Facebook Password: ")
    driver.find_element_by_id("pass").send_keys(passwrd)
    driver.implicitly_wait(4)
    driver.find_element_by_id("u_0_b").click()
    driver.implicitly_wait(6)
    driver.find_element_by_css_selector('div.datstx6m:nth-child(3) > span:nth-child(1) > div:nth-child(1)').click()
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector('input.tv7at329').send_keys('Amrik Singh')
    driver.implicitly_wait(8)
    driver.find_element_by_xpath('//*[@id="100052465153195"]').click()