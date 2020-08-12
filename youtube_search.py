import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


global youtube_driver

youtube_driver = webdriver.Chrome()
youtube_driver.maximize_window()


def play_song(song):
    search_url = 'https://www.youtube.com/results?search_query=' + song
    youtube_driver.get(search_url)
    video = youtube_driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
    video.click()