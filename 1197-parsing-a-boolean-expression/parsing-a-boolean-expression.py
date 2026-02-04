class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operator = []
        operand = []
        
        for c in expression:
            if c == ',':
                continue
            if self.is_operator(c):
                operator.append(c)
            elif self.is_operand(c) or c == '(':
                operand.append(c)
            else:
                op = operator.pop()
                result = None
                while operand[-1] != '(':
                    op1 = operand.pop()
                    result = self.perform_operation(op, op1, result)
                operand.pop()
                operand.append(result)

        return operand.pop() == 't'

    
    def is_operand(self, ch):
        return ch == 't' or ch == 'f'

    def is_operator(self, ch):
        return ch == '|' or ch == '&' or ch == '!'

    def perform_operation(self, operator, op1, op2):
        if operator == '!':
            return self.not_op(op1)
        elif operator == '&':
            return self.and_op(op1, op2)
        else:
            return self.or_op(op1, op2)
    
    def not_op(self, op):
        return 'f' if op == 't' else 't'

    def and_op(self, op1, op2):
        if op2 == None:
            return op1
        return 'f' if op1 == 'f' or op2 == 'f' else 't'

    def or_op(self, op1, op2):
        if op2 == None:
            return op1
        return 'f' if op1 == 'f' and op2 == 'f' else 't'