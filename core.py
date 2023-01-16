from graphloader import node_creator, mostfrequent, graphloader
from OOPparser import factpage_isolator, parser
from filecompiler import compiler
#for b choose your starting point for website parsing
#for c choose your end point for website parsing
#you can create a file variable. However, if you choose not to, the code will automatically create a file named File.txt

#If you are interested in the result, see the pdf file
b = "https://www.britannica.com/biography/Henry-VI-Holy-Roman-emperor"
c = ""
file = "Newfile.txt"
#The file has been loaded, to see the graph press run, or access the pdf file manualy
#o = compiler(start, file, end) #It will take some time for the compiler to load up
#b = compiler ("","","")
terms = mostfrequent(file) #Determines the most frequent terms among the given data
graphloader(file,terms)
