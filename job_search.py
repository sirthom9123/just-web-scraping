import requests
from bs4 import BeautifulSoup

job_title = input('Job Title: ')
location = input('Location: ')

URL = f'https://www.careers24.com/jobs/lc-{location}/kw-{job_title}/rmt-incl/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')
jobs = results.find_all('div', class_='job-card')
for jobs in jobs:
    link = jobs.find('a')['href']
    title = jobs.find('div', class_='col-12 job-card-head')
    company = jobs.find('div', class_='col-6 job-card-left')
    with open('job.txt', 'w')as file:
        file.write(str(jobs.text.strip()))
    
