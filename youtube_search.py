import sys
from selenium import webdriver
from selenium.webdriver.common.by import By



if __name__ == "__main__":
    search_url = ""
    search_str = ""

    sys.argv[0] = ""

    try:
        for i in sys.argv:
            search_str += i
            search_str += " "
        search_url = 'https://www.youtube.com/results?search_query=' + search_str
    except:
        search_str = input("->  ")
        search_url = 'https://www.youtube.com/results?search_query=' + search_str


    youtube_driver = webdriver.Chrome()
    youtube_driver.maximize_window()
    youtube_driver.get(search_url)


    while True:
        
        search_url = 'https://www.youtube.com/results?search_query=' + search_str


        youtube_driver.get(search_url)



        video = youtube_driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')

        video.click()

        search_str = input("->  ")
        usr_inp = input("enter for next video")
        if usr_inp == "0":
            break
        

    youtube_driver.close()


#/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/div/ytd-menu-renderer/yt-icon-button