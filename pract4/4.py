class HTML():
    
    def __init__(self):
        self.__html = []
        self.__close_tag = []

    def get_code(self):
        print('\n'.join(self.__html))

    def body(self):
        self.__html.append(f'<body>')
        self.__close_tag.append(f'</body>')
        return self

    def div(self):
        self.__html.append(f'<div>')
        self.__close_tag.append(f'</div>')
        return self

    def p(self,text):
        self.__html.append(f'<p>{text}<\p>')
    

    def __enter__(self):
            return self

    def __exit__(self, type, value, traceback):
        self.__html.append(self.__close_tag.pop())
        return True

html = HTML()

with html.body():
    with html.div():
        html.p('Hello world')
    with html.div():
        pass

html.get_code()