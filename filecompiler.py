from OOPparser import factpage_isolator, parser

def compiler(link, filename,flink):
    """Insert a Britannica link
       as a starting point of your Britannica parsing,
       the file name for storage,
       and the endpoint link of your parsing journey.
       If not, the default setting will start from Henry III and end with Henry VIII,
       compiling File.txt
    """
    default = "https://www.britannica.com/biography/Henry-III-king-of-England-1207-1272"
    fdefault = "https://www.britannica.com/biography/Henry-VI-Holy-Roman-emperor"

    ilink = default if link == "" else link
    flink  = fdefault if flink == "" else flink
    name = "File.txt" if filename == "" else filename
     
    terms = []
    factpage0 = factpage_isolator(ilink)
    first = parser(str(factpage0), factpage0.name)
    adjacent = first.links
    exitpoint = ''
    count = 0
    
    
    with open (name, "w", encoding = "utf-8") as f:
        for i in adjacent:
            
            factpage1 = factpage_isolator(i)
            parsed = parser( str(factpage1), factpage1.name())
            count += 1
            for s in parsed.links:
                if s in adjacent:
                    pass
                else:
                    adjacent.append(s)
            f.write(str(parsed) + "\n")
            if i == flink:
                break
            print(str(count)+" historical figures have been identified.")
