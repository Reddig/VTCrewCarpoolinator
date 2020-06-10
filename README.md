# VTCrewCarpoolinator
Script to hopefully save Dylan and future Dylans.

Steps: 

1) open up Windows PowerShell, and issue the following commands:
    
    pip install -r requirements.txt
    
2) Make an account on mapbox.com, and from this page: https://account.mapbox.com/ copy the access token
3) paste this key into a file named "key.txt", and place it in this folder
4) Open Windows PowerShell again, and type "python3 main.py"
5) Follow instructions in program

INSTRUCTIONS FOR EXCEL FORMATTING:

The program expects the following:

NAME HEADER;ADDRESS HEADER;DRIVE HEADER(Y/N);NUMBER OF SEATS HEADER;MPG HEADER;
name1;address1;y/n 1;seats1;mpg1;
name2;address2;y/n 2;seats2;mpg2;
.
.
.
[END]

Please name the file: "Address Sheet_CR.xlsx"