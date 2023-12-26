from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Firefox()
browser.install_addon('ublock_origin-1.54.0.xpi')


songs = [
         
]

autoplay = True
queryText = 'https://www.youtube.com/results?search_query='

for song in songs:
    query = f'{queryText}{song.replace(" ", "+")}'
    browser.get(query)
    link = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#video-title')))
    link.click()

    if autoplay:
        autoplayBtn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label*=Autoplay]')))
        autoplayBtn.click()
        autoplay = False

    
    songDurationElt = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.ytp-time-duration')))
    songDurationText = songDurationElt.text.partition(':')
    
    print(songDurationText)
    minutes = int(songDurationText[0])
    seconds = int(songDurationText[-1])
    songDuration = ((minutes * 60) + seconds)
    print(f'Time waiting rn: {songDuration//60}:{songDuration%60}' )
    time.sleep(songDuration)

    



