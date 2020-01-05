import time
import re
import os

from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#os.environ["PATH"] += os.pathsep + r'/home/chewie/Downloads/geckodriver-v0.24.0-linux64'
os.environ["PATH"] += os.pathsep + r'/home/chewie/Downloads/operadriver_linux64'
download_dir = '/home/chewie/Downloads/'

####################
#  Opera settings
#####################
crx_path = '/home/chewie/Downloads/operadriver_linux64/extension_1_0_8_0.crx'
options = webdriver.ChromeOptions()
#options.headless = True
options.add_extension(crx_path)
driver = webdriver.Opera(options=options)

url = 'https://forvo.com/search/難しい/ja'
url = 'http://rm-eu.palemoon.org/tools/Pale%20Moon%20Commander_v1.7.0.pdf'
driver.get(url)
#a = input('hello')
