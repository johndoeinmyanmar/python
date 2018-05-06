import selenium
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
profile = webdriver.FirefoxProfile()
geckopath = '~/geckodriver'
browser = selenium.webdriver.Firefox(
    capabilities=**DesiredCapabilities.FIREFOX**',
    executable_path=geckopath,
    firefox_profile=profile
    firefox_binary=binary
    )
browser.get("http://www.google.com")
