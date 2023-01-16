from bs4 import BeautifulSoup
import requests
from requests.exceptions import MissingSchema
import collections
import re
import random


class factpage_isolator(object):
    def __init__(self,linkin):
        result = requests.get(linkin) #returns the contents of the page
        self.doc = BeautifulSoup(result.content, "html.parser")
        funnel = self.doc.find_all("a", class_="btn btn-sm btn-outline-blue border")
        self.flink = ''
        try:
            self.flink = "https://www.britannica.com/" + str([i.get("href") for i in funnel][0])
        except IndexError:  #If the website does not have the facts-containing table, it will pass
            pass
        
    def name(self):
        self.name = self.doc.find('h1', class_='mb-0').text    
        return str(self.name)
    
    def __str__(self):
        return str(self.flink)
        

class parser(object):
    def __init__(self, link, name = None):
        try:
            self.links = []
            self.terms = []
            self.info = collections.defaultdict(dict)
            self.info["Name"] = name
            self.info["ID"] = random.randint(100,900)
            gogetter = requests.get(link)
            doc = BeautifulSoup(gogetter.content, "html.parser")
            funnel = doc.find("table")#finds the only table on the page
            all_trs = funnel.find_all("tr")
            for tr in all_trs:
                    th = tr.find_all("th")
                    if not any(th):
                        continue
                    th = th[0]
                    k = th.text.translate({160:' '}).strip()   #The term
                    self.terms.append(k)           
                    try:
                        v = tr.find("td")
                        text = v.text.translate({160:''}).strip(" ")
                        if re.search("[A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}", text):
                            text = str(re.findall("[A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}", text)[0])  #gets the dates
                        else: 
                            text = text.strip().split("•")
                            names = []
                            b = [i for i in v.find_all("a") if k == "Notable Family Members"]
                            for i in b:
                                newlink = str("https://www.britannica.com/" + str(i.get("href")))
                                name = str(factpage_isolator(newlink).name())
                                names.append(name)
                                self.links.append(newlink)  #gets the links of each family member   
                        self.info[k] = dict(zip([i.strip().split(" ", 1)[0] for i in text],names)) if k == "Notable Family Members" else text
                    except IndexError:
                        pass
        except MissingSchema: #Passes in case of a missing link
            pass
    
    def links(self):
        return list(self.links)
    
    def terms(self):
        return list(self.terms)
    
    def __str__(self):
        return str(dict(self.info))



