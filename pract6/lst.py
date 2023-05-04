
def create_node(v, nextNode):
    def node():
        return v, nextNode
    return node

def hasNext(lst):
    _, nodeNext = lst()
    return nodeNext!=None

def iter_lst(lst):
    
    if lst==None:
        return

    val, nodeNext = lst()

    yield val
    while nodeNext!=None:
        val, nodeNext = nodeNext()
        yield val
    
    return
