from typing import List


def ask_search_query() -> str:
    """ 
    Asks user for a search query

    Returns: 
        [str] -> https://www.google.com/search?q=search+query
    """

    query = input("Search Query >>> ")
    return f"https://www.google.com/search?q={'+'.join(query.split(' '))}"

def ask_link_to_open(page_content: List[List[str]]) -> List[str]:
    """
    Asks user for a link to open and view its content
    Args:
        page_content: List[List[str]]

    Returns:
        List[str] -> [website name, website link]
    """

    for idx, content in enumerate(page_content, start= 1): 
        print(f"{idx}) Website Host: {content[0]}")
        print(f"URL: {content[1]}")
        print()
    print()
    link_num = int(input("Please enter the number corresponding to the website you want to visit\n>>> "))
    while not 1 <= link_num <= len(page_content) + 1:
        link_num = int(input("Please enter a valid number corresponding to the website you want to visit\n>>> "))

    return page_content[link_num - 1] 
