import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

from jobFetcher import getJob

url = "https://www.linkedin.com/jobs/search?keywords=Full%20Stack%20Engineer&location=Bengaluru%20South&geoId=112565523&distance=25&f_TPR=r604800&f_JT=F&position=1&pageNum=0"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)

n = driver.find_element(By.CLASS_NAME , 'results-context-header__job-count')
print(n.text)

SCROLL_WAIT_TIME = 3
SCROLL_BREAK_ITERATION = 0

keepScrolling = True
scrollIterations = 0


while keepScrolling and scrollIterations < SCROLL_BREAK_ITERATION:
    scrollIterations = scrollIterations + 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_WAIT_TIME)

    try:
        loadMoreButton = driver.find_element(by = By.CLASS_NAME, value = 'infinite-scroller__show-more-button')
        if (loadMoreButton.is_displayed()):
            driver.execute_script("arguments[0].click();", loadMoreButton)
            time.sleep(5)
    except:
        pass
        time.sleep(5)
    
    try:
        allSearchViewed = driver.find_element(by = By.CLASS_NAME, value = 'inline-notification__text')
        if (allSearchViewed.is_displayed()) :
            keepScrolling = False
    except:
        pass

    print(f'scrolled {scrollIterations} times')

print('Loading of page done!')

jobLinkElements = driver.find_elements(by=By.CLASS_NAME, value='base-card__full-link')

job_ids = []

for jobLinkElement in jobLinkElements:
    link = jobLinkElement.get_attribute('href')
    cleansedLink = link[0 : link.index('?')]
    job_id = cleansedLink[cleansedLink.rindex('-')+1 : len(cleansedLink)]
    job_ids.append(job_id)

print('Job IDs collected')

jobs = []

for jobid in job_ids:
    print(f'Getting {jobid}')
    try:
        job = getJob(jobid)
        jobs.append(job)
        print(job['title'])
    except:
        print(f'Error getting {jobid}')
        continue

df = pd.DataFrame.from_records(jobs)

df.to_csv('linkedin_jds_dataset.csv')

print('Data written to CSV')

print('Task complete!')