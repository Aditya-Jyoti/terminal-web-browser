import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urlparse
from html2text import html2text
from os import name, system


def search_page_content(search_query: str) -> List[List[str]]: 
    """
    Reads content from the google search page html content and returns
    list of visitable website names and their links

    Args:
        search_query: [str] -> https://www.google.com/search?q=search+term  

    Returns:
        List[List[str]] -> [[website name, website link]]
    """

    html_content = requests.get(search_query).text
    soup = BeautifulSoup(html_content, "html.parser") 
    results = soup.find_all("div", {"class": "ZINbbc luh4tb xpd O9g5cc uUPGi"}) 
    
    page_content = []
    for html in results:
        raw_url = html.a.get("href")
        link_to_result = raw_url.replace("/url?q=", "").split("/&")[0]
        
        parser = urlparse(link_to_result)
        website_name = parser.hostname
        
        page_content.append([website_name, link_to_result])

    return page_content

def read_page_content(link_to_page: str):
    """
    Reads the urls provided and prints out a pretty version of the text contained in the website 

    Args:
        link_to_page: [str] -> https://domain_name/other_text
    """

    html_content = requests.get(link_to_page).text 
    
    soup = BeautifulSoup(html_content, "html.parser")
    for data in soup(["script", "noscript", "link", "meta", "path", "form", "style", "link", "path"]):
        data.decompose()

    print(html2text(soup.prettify()))

def clear_screen():
    """
    cleans the terminal space, works for both windows and non windows machines 
    """

    if name == "nt":
        _ = system("cls")
        print("\n"*100)
        print("THE TERMINAL WAS CLEARED HERE")
        print("\n"*10)
        _ = system("cls")

    else:
        _ = system("clear")
        print("\n"*100)
        print("THE TERMINAL WAS CLEARED HERE")
        print("\n"*10)
        _ = system("clear")


