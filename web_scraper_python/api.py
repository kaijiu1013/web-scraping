import flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # the Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    #未来在请求量增大的时候，可以考虑使用multi-thread 来增加爬虫的效率, 也许需要申请更多的crux账号来执行multi-thread
    #启动储存在本地文件夹里的chrome driver，然后go to 需要进行操作的网页地址
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://track.cruxsystems.com/login")

    # 首先到login页面，然后输入账号密码，再点击login后进入到crux系统
    element_email = driver.find_element_by_name("email")
    element_password = driver.find_element_by_name("password")
    element_email.send_keys("")
    element_password.send_keys("")
    element_password.send_keys(Keys.RETURN)

    #Explicit wait for search container number in the search bar textarea
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    element_search_containers = driver.find_element_by_tag_name("textarea")
    element_search_containers.send_keys("TGHU8666330")
    element_search_containers.send_keys(Keys.RETURN)

    #ask selenium to click the saved container area to get container detail data
    time.sleep(5) # 延时5秒以保证 asynchronous web page loading completed
    driver.find_element_by_xpath('//*[@id="saved-container"]/div/div[2]/div[1]/div[1]/span').click()

    # Parse the html content ('strong' tag)
    time.sleep(5)
    element_containers_details = driver.find_element_by_tag_name("div.details")
    htmlConDetail = element_containers_details.get_attribute('innerHTML')
    soup = BeautifulSoup(htmlConDetail, 'lxml')
    for strong_tag in soup.find_all('strong'):
        print (strong_tag.text, strong_tag.next_sibling) 

    #Parse html table
    element_containers_table = driver.find_element_by_tag_name("table")
    htmlConTable = element_containers_table .get_attribute('innerHTML')
    soup2 = BeautifulSoup(htmlConTable, 'lxml')
    #option2 for table parsing
    for items in soup2.find_all('tr'):
        data = items.find_all(['td'])
        title = data[1].find('p')
        information = data[2].find('p')
        print(title.text, information.text)    

    return "<h1>I get container data from Crux </p>"

app.run()