This is the webscraping code to fetch the data from the nist data base
Replace the url in the code with the required element
The nist will only give 600 data points if you want the data at 60 bar from 100k to 1000k at an increment of 1 it will auto adjust to the 600 values only.
but here the python code is in such a wa that the first 600 values will be webscraped then the next 600 then concinate them and make a single consilidated file for each pressure.

MANUALLY install this package **"pip install openpyxl**" from terminal to merge the txt files into a excel file
install python extension

change the name of the file in the webscrap and combine files, like if you are extraxcting oxygen data edit the file name as oxygen.