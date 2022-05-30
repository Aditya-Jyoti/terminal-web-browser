from browser.logic import search_page_content, read_page_content
from browser.user_interactions import ask_link_to_open, ask_search_query

read_page_content(ask_link_to_open(search_page_content(ask_search_query()))[1])
