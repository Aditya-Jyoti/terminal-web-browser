from browser.logic import search_page_content, read_page_content, clear_screen
from browser.user_interactions import ask_link_to_open, ask_search_query
from time import sleep
import keyboard

def main():
    search_link = ask_search_query()
    sleep(0.2)
    clear_screen()
    website_link = ask_link_to_open(search_page_content(search_link))
    print(f"\nopening link: {website_link[1]}")
    sleep(0.2)
    read_page_content(website_link[1])
    while True:
        if keyboard.is_pressed("ctrl+s"):
            clear_screen()
            main()
     


if __name__ == "__main__":
    print(r"""
     _    _ ___________  ____________ _____  _    _ _____ ___________ 
    | |  | |  ___| ___ \ | ___ \ ___ \  _  || |  | /  ___|  ___| ___ \
    | |  | | |__ | |_/ / | |_/ / |_/ / | | || |  | \ `--.| |__ | |_/ /
    | |/\| |  __|| ___ \ | ___ \    /| | | || |/\| |`--. \  __||    / 
    \  /\  / |___| |_/ / | |_/ / |\ \\ \_/ /\  /\  /\__/ / |___| |\ \ 
     \/  \/\____/\____/  \____/\_| \_|\___/  \/  \/\____/\____/\_| \_|
    """)
    
    print("Press [ctrl+s] key to go back to the search page")
    sleep(1)
    clear_screen()
    main()
