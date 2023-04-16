from SVG import SVG



class Tree:
    def __init__(self,val,*children):
        self.val = val
        self.children = list(children)
        self.x = 0
        self.y = 0


class DrawTree:
    def __init__(self,rootTree,width, height,fileName = 'Tree.svg'):
        self.__svg = SVG()
        self.__rootTree = rootTree
        self.__fileName = fileName
        self.__width = width
        self.__height = height
        self.__circleRad = 2  
        self.__margin = self.__circleRad+2
        self.__offSetY = (height-self.__margin*2)/self.findDepth(rootTree,0)

    def findDepth(self, tree, currentDepth):
            depth = currentDepth
            for child in tree.children:
                if (isinstance(child, Tree)):
                    depth = max(depth, self.findDepth(child, currentDepth + 1))
            return depth

    def setCircleRad(self, newRad):
            self.__circleRad = newRad


    def draw(self, tree = None, leftBorder = 0, rightBorder = 0, depth = 0):
        if tree == None:
            tree = self.__rootTree
            leftBorder = self.__margin
            rightBorder = self.__width - self.__margin
        
        numberOfChild = len(tree.children)

        tree.y = self.__offSetY*depth+self.__margin
        tree.x = (leftBorder+rightBorder)/2
        self.__svg.circle(tree.x, tree.y, self.__circleRad, 'black')

        if numberOfChild == 0:
            return

        offset = (rightBorder -leftBorder)/numberOfChild

        for index,child in enumerate(tree.children):
            newLeftBorder = leftBorder + index*(offset)
            newRightBorder = leftBorder + (index+1)*(offset)
            self.draw(child, newLeftBorder, newRightBorder, depth=depth+1)

        for child in tree.children:
            self.__svg.line(tree.x, tree.y, child.x, child.y,'black')
        
        if depth==0:
            self.__svg.save(self.__fileName, self.__width, self.__height)
            print('Done:', self.__fileName)
        


tree_1_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_1_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13, Tree(16)))), Tree(14, Tree(15)))
tree_1 = Tree(1, tree_1_2, tree_1_8)

drawTreeObj = DrawTree(tree_1, 100, 100, "Task5_4_1.svg")
drawTreeObj.setCircleRad(2)
drawTreeObj.draw()

drawTreeObj = DrawTree(tree_1_2, 100, 100, "Task5_4_2.svg")
drawTreeObj.draw()

drawTreeObj = DrawTree(tree_1_8, 100, 100, 'Task5_4_3.svg')
drawTreeObj.draw()

tree_2_l = Tree(2, Tree(3, Tree(4), Tree(4, Tree(6), Tree(7, Tree(8)))), Tree(9, Tree(10)))
tree_2_c = Tree(11, Tree(12, Tree(13), Tree(14, Tree(15))))
tree_2_r = Tree(16, Tree(17), Tree(18, Tree(19), Tree(20)), Tree(21), Tree(22))
tree_2 = Tree(1, tree_2_l, tree_2_c, tree_2_r)

drawTreeObj = DrawTree(tree_2, 200, 200, 'Task5_4_4.svg')
drawTreeObj.setCircleRad(3)
drawTreeObj.draw()