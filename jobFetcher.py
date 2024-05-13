import requests
import time
from bs4 import BeautifulSoup as BS

def getHtmlContent(link: str) -> str:
    page = requests.get(link)
    time.sleep(4)
    content = page.content.decode(encoding = "utf-8")
    return content

def getJob(id: str) -> object:
    url_link = f'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{id}'
    content = getHtmlContent(url_link)
    soup = BS(content, features = "html.parser")
    title_element = soup.find('h2', { 'class': 'top-card-layout__title' })
    jd_title = title_element.text
    company_element = soup.find('a', { 'class': 'topcard__org-name-link' })
    jd_company = company_element.text
    location_element = soup.find('span', { 'class': 'topcard__flavor topcard__flavor--bullet' })
    jd_location = location_element.text
    markup_element = soup.find('div', { 'class': 'show-more-less-html__markup' })
    jd_markup = markup_element.text
    job_object = {
        'id': 3918664773,
        'title': jd_title,
        'company': jd_company,
        'location': jd_location,
        'jd': jd_markup
    }
    return job_object

