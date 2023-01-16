import ast
import graphviz
import codecs
def node_creator(dict0,ls):
    if dict0 == None:
        pass
    else:
        ID = dict0["ID"]
        list0 = []
        for term in ls:
            try:
                characteristic = dict0[term]
                list0.append(str(characteristic))
            
            except KeyError:
                pass
            
        label = "\n".join(list0)
        return str(ID),label

def mostfrequent(foil):
    """finds the most frequently used terms basing on their frequency
        within the whole set"""
    fl = open(foil, encoding = "utf - 8" )
    terms = [list(ast.literal_eval(b).keys()) for b in fl]
    lengths = [len(i) for i in terms]
    m = max(lengths)  #determines the longest list of terms
    n = lengths.index(m)
    longest = terms[n] #finds the longest list of terms
    lilst = []
    
    howlong = len(terms)

    for b in longest:
        count = 0
        for i in terms:
            if b in i:
                count += 1
        percent = count/howlong*100 #determines how close each sublist of terms is close to the longest one
        if percent >= 90:
            lilst.append(b) #determines the most frequent terms found in the data according to the percentage
    return lilst

def graphloader(fl,ls):
    """ Comes along with the mostfrequent function.
        Extracts the pertinent information to include into the nodes"""
    gra = graphviz.Digraph()
    fl = open(fl)
    dictionaries = [ast.literal_eval(b) for b in fl]
    IDs = []
    ls += ["Title / Office", "House / Dynasty"]
    for dic in dictionaries: 
        pseudo_node = node_creator(dic,ls)
        gra.node(pseudo_node[0],pseudo_node[1])
        if "Notable Family Members" in dic:
            for fmember in list(dic["Notable Family Members"].values()):
                for dic0 in dictionaries:
                    if dic0["Name"] == fmember:
                        relative_node = node_creator(dic0,ls)
                        gra.node(relative_node[0],relative_node[1])
                        gra.edge(pseudo_node[0], relative_node[0])
    return gra.view()

