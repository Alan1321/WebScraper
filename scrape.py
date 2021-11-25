from bs4 import BeautifulSoup
import requests
import re

class scrape:
    data = []
    def __init__(self, last_name):
        self.last_name = last_name
        print("Courses................................................")

    def scrapeCourses(self, link):
        courses = ""
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        info = soup.find('pre')
        info_str = str(info)
        all_matches = re.finditer(pattern = self.last_name, string = str(info))
        for match in all_matches:
            courses += info_str[match.start() - 150:match.start()-81]
            courses += "\n"
            #print(info_str[match.start() - 120:match.start()-80])
        
        if(courses != ""):
            scrape.data.append(link[45:53])
            scrape.data.append(courses)