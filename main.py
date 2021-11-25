from bs4 import BeautifulSoup
from scrape import scrape
import threading
import re

last_name = str(input("Enter Professor's last name\n"))
last_name = last_name + " "

departments = ['CS','MA','HY','ECN']

links = []
for depart in departments:
    links.append("https://www.uah.edu/cgi-bin/schedule.pl?file=sprg2022.html&segment=" + str(depart))
    links.append("https://www.uah.edu/cgi-bin/schedule.pl?file=fall2021.html&segment=" + str(depart))
    links.append("https://www.uah.edu/cgi-bin/schedule.pl?file=sprg2021.html&segment=" + str(depart))
    links.append("https://www.uah.edu/cgi-bin/schedule.pl?file=sum2021a.html&segment=" + str(depart))

#archive_links = []

for depart in departments:
    year = 2020
    for i in range(11):
        fall_link = "https://www.uah.edu/cgi-bin/schedule.pl?file=fall"+str(year)+".html&dir=archived&segment="+str(depart)
        sprg_link = "https://www.uah.edu/cgi-bin/schedule.pl?file=sprg"+str(year)+".html&dir=archived&segment="+str(depart)
        suma_link = "https://www.uah.edu/cgi-bin/schedule.pl?file=sum"+str(year)+"a.html&dir=archived&segment="+str(depart)
        links.append(fall_link)
        links.append(sprg_link)
        links.append(suma_link)
        year = year - 1

scraper = scrape(last_name)

TOTAL_THREADS = 17

index = 0
total = int(len(links)/TOTAL_THREADS) + 1
length = len(links)
print(total)
for i in range(total):
    threads = []
    remaining = length - index
    if(remaining < TOTAL_THREADS):
        TOTAL_THREADS = remaining
    for _ in range(TOTAL_THREADS):
        t = threading.Thread(target = scraper.scrapeCourses, args = [links[index]])
        index+=1
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

for item in scrape.data:
    print(item)

