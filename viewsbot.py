# ETHICAL HACKING: youtube viewsbot
import time
from selenium import webdriver

driver = webdriver.Chrome('[..]/chromedriver')

# number of seconds to refresh browser
Timer = 10

# url of video to view
link = 'https://www.youtube.com/watch?v=wTcNtgA6gHs'

# number of views to achieve
views = 5

driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()