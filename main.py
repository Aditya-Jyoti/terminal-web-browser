from browser.logic import search_page_content, read_page_content, clear_screen
from browser.user_interactions import ask_link_to_open, ask_search_query
from time import sleep
from sys import exit
import keyboard

def displaying_search_page(search_link: str):
    """
    displays webpage content from a provided search term

    Args:
        search_link: [str] -> https://domain_name/other_text
    """

    website_link = ask_link_to_open(search_page_content(search_link))
    print(f"\nopening link: {website_link[1]}")
    sleep(0.2)
    clear_screen()
    read_page_content(website_link[1])

def main():
    search_link = ask_search_query()
    sleep(0.2)
    clear_screen()
    displaying_search_page(search_link)

    while True:
        if keyboard.is_pressed("ctrl+s"):
            clear_screen()
            main()
        
        if keyboard.is_pressed("ctrl+b"):
            clear_screen()
            displaying_search_page(search_link)
            
        if keyboard.is_pressed("ctrl+q"):
            clear_screen()
            print("QUITTING PROGRAM")
            return


if __name__ == "__main__":
    clear_screen()
    print(r"""
     _    _ ___________  ____________ _____  _    _ _____ ___________ 
    | |  | |  ___| ___ \ | ___ \ ___ \  _  || |  | /  ___|  ___| ___ \
    | |  | | |__ | |_/ / | |_/ / |_/ / | | || |  | \ `--.| |__ | |_/ /
    | |/\| |  __|| ___ \ | ___ \    /| | | || |/\| |`--. \  __||    / 
    \  /\  / |___| |_/ / | |_/ / |\ \\ \_/ /\  /\  /\__/ / |___| |\ \ 
     \/  \/\____/\____/  \____/\_| \_|\___/  \/  \/\____/\____/\_| \_|
    """)

    print() 
    print("This is a extreamly barebones terminal emulation of a web browser")
    print("Works best when trying to read pages which contain maximum text")
    print("Keyboard Shotcuts:- ")
    print("     1) ctrl+s -> Open up prompt to ask for search query")
    print("     2) ctrl+b -> Return back to main page containing links to search results")
    print("     3) ctrl+q -> Quit the program")
    print()
    print("Please press enter when you want to continue")
    print("Please press ctrl+q to quit the program")

    while True:
        if keyboard.is_pressed("enter"):
            filler = input()
            clear_screen()
            break 
        
        if keyboard.is_pressed("ctrl+q"):
            exit(0)

    main()
