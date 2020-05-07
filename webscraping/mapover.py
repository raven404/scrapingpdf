import webbrowser, sys ,pyperclip

#reading from commandline/system
sys.argv

#to check if search is prompted from sys
if len(sys.argv)>1:
    address=''.join(sys.argv[1:]) #storing address to be searched 

#checking if search is prompted through copy on clipboard
else:
    address=pyperclip.paste()     #storing address to be searched 

#opening webbrowser on 'https://www.google.com/maps/places/<address>'
webbrowser.open('https://www.google.com/maps/place/' + address)