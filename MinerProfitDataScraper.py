from bs4 import BeautifulSoup 
import requests 

#miner site 
website = requests.get("https://www.asicminervalue.com/miners")

#get content
soup = BeautifulSoup(website.content, "html.parser")

#find id for table
#id = soup.find(id = 'datatable_profitability')

#for tr in soup.find_all('tr')[2:]:
#    tds = tr.find_all('td')
#    print ("Model: %s, Power: %s, ProfitPerDay: %s" % \
#          (tds[0].text, tds[3].text, tds[6].text))

with open('output.txt', 'w') as f:
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        f.write("%s, %s, %s\n" % \
              (tds[0].text, tds[3].text.strip("W"), tds[6].text.strip("/day")))
        



#print(id.text)
#print(soup.prettify())