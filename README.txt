Okay so the way this works is:

main.py :
*Takes a URL and list of DNS servers
*Tests that URL address against the DNS servers, comparing it to the expected IP Address
*Gets the results and stores it in a readable format in a txt document
*The txt document is named URL + ".txt"

config.txt :
*Stores the URLs used in main.py, making them easy to gather in the rest of the program

pretty.py and pretty.txt :
*pretty.py creates a tabular format of the txt file data
*it outputs this into pretty.txt which is essentially a html document

flask_DNS-Tester.py :
*takes pretty.txt and broadcasts it to http://localhost:5000

dependencies.txt :
*pretty self explanatory

TO LAUNCH THE FLASK IN COMMAND PROMPT type the following: 
  C:\path\to\app>set FLASK_APP=flask_DNS-Tester.py
  export FLASK_APP=flask_DNS-Tester.py
  python -m flask run
