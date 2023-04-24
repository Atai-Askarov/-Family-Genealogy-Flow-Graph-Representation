#A-Flow-Graph-Representation-f-a-Family-Genealogy

  Note: BeautifulSoup package must be installed for this to work on your computer

  The flow graph representation of a family lineage is designed to extract data from the website Britannica, organize it in a file, and display the relationships among historical figures using a flow chart. Through the visual representation of family graphs, the user will be able to learn about vast, familial networks that have spanned multiple generations, extended through nations, and survived to the present day – as long as the website permits.
  
  To use the program, the user must access the “core” file. The compiling function is initially disabled via the comment sign: #. The program is set on default to project the genealogy of Henry III. To view his roots, the user should input empty strings: “”, “”, “”, into the compiler function. The program will also create a file: “File.txt,” on default unless another file is specified. This is done to view the result since the function will take time to load the file with the data attributed to the individual and their lineage. If the user wishes to create their graph, they should remove the sign, input their own desired URL links, and disable the graphloader function. In the python file, two variables exist: b and c. They indicate the links at which the collection of data must start and end. However, it is possible for the program to never reach the end link. Since the relationships between the historical people could be poorly documented, some familial relationships could have been never recorded. Once the file has been loaded, the user should disable the variables and enable the graphloader. Next, the user must press Run to view the flowchart that represents the genealogy of the person in question.
Design Guide

  The project consists of 4 files: OOPparser, filecompiler, graphloader, and core. OOPparser contains the function: factpage_isolator, and the class: parser. Since the program is tailored for the use over Britannica.com only, the function intakes the URL link of an existing Britannica page and returns the link to the fact page, associated with the topic. The parser then creates an instance employing the resulting link that stores the extracted information. The extraction occurs with the use of the Beautifulsoup module, a parsing that enables data gathering over HTML tags. Furthermore, the class organizes the data, emphasizing easy retrieval using dictionaries and lists. Moreover, the class compartmentalizes the collected data and enables easy access to the URL links, and reference terms attributed to relatives of an individual. 
  
  Filecompiler takes the collected information from the parser class and stores it in a file. The whole program attempts at presenting chosen family trees at a specific time in history. The default mode targets the period when the War of the Roses took a turn: initiating with Henry III and ending with Henry VII. However, the parser does not reach Henry VII as it parses over the lineage of Henry III. This could be attributed to the missing URL links amongst the family members or the absence of their relation.
  
  Graphloader works with the compiled file and shows its contents in a flowchart using Graphviz, a graph structure visualizing tool.

  The program has much potential for improvement since not all the extracted information has been used for the display. Different colors could be attributed to connections between individuals, based on the House to which they belong, representing each house and showing its size and presence over the years. Furthermore, the line of kings could have its color. This could show how the throne has been passed from house to house and who has occupied it. The code could be altered to have multiple entries. This could lead to the projection of multiple families and verification of their relation.  
