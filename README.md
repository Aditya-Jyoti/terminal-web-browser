# terminal-web-browser

This project was made to emulate a web browser in a terminal. Its extremely
barebones as of yet and still has many more features planned for it. As of yet
it works partially for reading webpage content and displaying it in a sort of
markdown fashion.

This is project is still in its **Beta Phase**.

#### Known Issues:

As of writing this since I'm using the `html2text` library to convert my html
responses to text, there are times when text tends to be ignored. Currently on
visiting a wikipedia page no real text is displayed out and on `a` tag links are
visible, though I don't know why.

#### How To Run It:

```
1) Clone the repository
Note: since the keyboard module is being used for linux machines root access is required

2) run `&sudo pip3 install -r requirements.txt`
3) run `&sudo python3 main.py`

Note: the above commands may change for windows and there may not be a need to use `sudo`
      use at your own discreation
```

_Since I'm on `ubuntu` I'm not exactly sure if Windows users can run the program
or not._

#### Keyboard Shortcuts:

1. `ctrl+s`: returns back to the search query page
2. `ctrl+b`: returns back to the page containting search query links
3. `ctrl+q`: quits the program

**Note: all keyboard shortcuts work only in non entry field times, ie, when user
input is not being asked**

#### After Thoughts:

I would appreciate your feedback on this project and would like if you could
open issues suggesting how to fix the known issues, as well as contributing to
the project to make this even better
