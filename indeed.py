import requests
from bs4 import BeautifulSoup


def get_last_page(word, place):
    BASE_URL = (
        f"https://kr.indeed.com/jobs?q={word}&l={place}&vjk=84329a66291839cd&start=0"
    )
    html = requests.get(BASE_URL)
    soup = BeautifulSoup(html.text, "html.parser")
    max_page = (
        int(
            soup.find("div", {"class", "resultsTop"})
            .find(id="searchCountPages")
            .string.split()[-1][:-1]
        )
        // 10
    )
    return max_page


def extract_job(result):
    exp_contents = result.find("div", {"class", "job-snippet"}).contents
    exp = ""
    for content in exp_contents:
        exp += content.string
    info = result.find("td", {"class", "resultContent"})
    title = info.find("h2", {"class", "jobTitle"}).find("span", class_=None).string
    location = info.find("div", {"class", "companyLocation"}).string
    url = "https://kr.indeed.com" + result.parent["href"]
    try:
        if info.find("span", {"class", "companyName"}).find("a"):
            company = info.find("span", {"class", "companyName"}).find("a").text
        else:
            company = info.find("span", {"class", "companyName"}).text
    except:
        company = ""
    return {
        "title": title,
        "company": company,
        "location": location,
        "explanation": exp,
        "url": url,
    }


def extract_jobs(word, place):
    jobs = []
    max_page = get_last_page(word, place)
    for page_num in range(max_page):
        URL = f"https://kr.indeed.com/jobs?q={word}&l={place}&vjk=84329a66291839cd&start={page_num * 10}"
        html = requests.get(URL)
        soup = BeautifulSoup(html.text, "html.parser")
        results = soup.find_all("div", {"class", "slider_container"})
        for result in results:
            jobs.append(extract_job(result))
    return jobs
