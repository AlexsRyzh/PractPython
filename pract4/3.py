
##3.1
class Num:
    def __init__(self, number):
        self.number = number

class Add:
    def __init__(self,expr1,expr2):
        self.expr1 = expr1
        self.expr2 = expr2

class Mul(Add):
    pass



##3.2
class PrintVisitor:
    def visit(self, expr):
        return (isinstance(expr, Mul) and f'({self.visit(expr.expr1)} * {self.visit(expr.expr2)})') \
                or (isinstance(expr, Add) and f'({self.visit(expr.expr1)} + {self.visit(expr.expr2)})') \
                or (expr.number)



##3.3
class CalcVisitor:
    def visit(self,expr):
        return (isinstance(expr, Mul) and (self.visit(expr.expr1) * self.visit(expr.expr2))) \
                or (isinstance(expr, Add) and (self.visit(expr.expr1) + self.visit(expr.expr2))) \
                or (expr.number)

##3.4
class StackVisitor:
    def visit(self,expr):
        return (isinstance(expr, Mul) and f'{self.visit(expr.expr1)}\n{self.visit(expr.expr2)}\nMUL') \
                or (isinstance(expr, Add) and f'{self.visit(expr.expr1)}\n{self.visit(expr.expr2)}\nADD') \
                or (f'PUSH {expr.number}')


ast = Add(Num(7),Mul(Num(3),Num(2)))

pv = PrintVisitor()

cv = CalcVisitor()

sv = StackVisitor()

print(sv.visit(ast))


