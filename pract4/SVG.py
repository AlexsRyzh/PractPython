class SVG:

    def __init__(self):
        self.__svg_elem=[]

    def line(self, x1,y1,x2,y2,color):
        line = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" />'
        self.__svg_elem.append(line)

    def circle(self,cx,cy,r,color):
        circle = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" />'
        self.__svg_elem.append(circle)

    def save(self,path,width,height):
        with open('pract4/'+path,'w') as file:
            file.write(f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
            for i in self.__svg_elem:
                file.write(i+'\n')
            file.write(f'</svg>')

# svg = SVG()

# svg.line(10, 10, 60, 10, color='black')
# svg.line(60, 10, 60, 60, color='black')
# svg.line(60, 60, 10, 60, color='black')
# svg.line(10, 60, 10, 10, color='black')

# svg.circle(10, 10, r=5, color='red')
# svg.circle(60, 10, r=5, color='red')
# svg.circle(60, 60, r=5, color='red')
# svg.circle(10, 60, r=5, color='red')

# svg.save('pic.svg', 100, 100)