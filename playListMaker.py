import os
import time
import shutil
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

music_playlist = ['arabic kuthu']

for name in music_playlist:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/results?search_query=' +
               str(name.replace(' ', '+')))

    yt_link = driver.find_element(By.ID, 'video-title')
    link = yt_link.get_attribute('href')

    driver.get('https://en.onlymp3.to/22/')

    yt_url_input = driver.find_element('id', 'txtUrl')
    yt_url_input.send_keys(link)

    submit_button = driver.find_element('id', 'btnSubmit')
    submit_button.click()

    time.sleep(15)

    downlaod_button = driver.find_element(
        By.PARTIAL_LINK_TEXT, 'Download').click()

    time.sleep(15)

    list_dir = os.listdir('/Users/tsnevan/Downloads')
    for file in list_dir:
        if 'onlymp3.to' in file:
            use_file = file

    shutil.move('/Users/tsnevan/Downloads/' + str(use_file),
                '/Users/tsnevan/Desktop/very_good_music')
