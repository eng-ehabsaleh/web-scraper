import requests
from bs4 import BeautifulSoup

 


def get_citations_needed_count(url):
    url=str(url)
    res=requests.get(url)
    html_text=res.text
    soup=BeautifulSoup(html_text,"html.parser")
    
    num=soup.find_all("a",title="Wikipedia:Citation needed")
    return (len(num))
    

def get_citations_needed_report(url):
    url=str(url)
    res=requests.get(url)
    html_text=res.text
    soup=BeautifulSoup(html_text,"html.parser")
    parent=soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    num=0
    for ele in parent:
        num+=1
        print(f'number {num}. references needed for report: {ele.parent.text}')
        
    
