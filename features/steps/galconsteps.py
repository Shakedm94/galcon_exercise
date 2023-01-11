from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome('C:\PytonTemp\Drivers\chromedriver.exe')
    context.driver.get('https://tv-guide.walla.co.il/')
    context.driver.maximize_window()



@when('one channel page')
def openOneChannelPage(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/section[1]/div[2]/ul/li[35]/a'))).click()



@then('verify Zehu Ze broadcasted in thursday at 21:15')
def verifyShow(context):
    # find all days div
    days = context.driver.find_elements(By.CLASS_NAME, "next-day")

    # var for thurday index in div list
    day_num = 0

    # lop to find which index is thursday
    for i in range(len(days)):
        print(str(i) + ": " + days[i].find_element(By.CLASS_NAME, "day").text)
        if days[i].find_element(By.CLASS_NAME, "day").text == "חמישי":
            day_num = i
    print('thurday cass num is - ' + str(day_num))

    # list of the classes that contain the shows
    days_program = context.driver.find_elements(By.CLASS_NAME, "css-1bog2e")

    # choose only thursday using day_num var
    thursday_program = days_program[day_num]

    # create list of all shows in thursday
    programs = thursday_program.find_elements(By.CLASS_NAME, "css-ual8pl")

    # created a list of tuples containing show names and time and
    # and finding if the requested show exists in the list in the rigth time
    for i in [(i.find_element(By.TAG_NAME, "h3").get_attribute("innerText"),
               i.find_element(By.TAG_NAME, "time").get_attribute("innerText")) for i in programs]:
        if i[0] == "זהו זה!" and i[1] == "21:15":
            print("The Program Zehu Ze! is broadcasted on thursday at 21:15")


@then('close browser')
def closeBrowser(context):
    context.driver.close()

