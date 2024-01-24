class Calculator:
    def add(operands):
        result = operands[0]
        for i in operands[1:]: #skip the first operand because it is assigned to result already
            result += i
        return result
    
    def subtract(operands):
        result = operands[0]
        for i in operands[1:]: #skip the first operand because it is assigned to result already
            result -= i
        return result

    def multiply(operands):
        result = operands[0]
        for i in operands[1:]: #skip the first operand because it is assigned to result already
            result *= i
        return result

    def divide(operands):
        result = operands[0]
        for i in operands[1:]: #skip the first operand because it is assigned to result already
            result /= i
        return result

    def exponentiate(operands):
        result = operands[0]
        for i in operands[1:]: #skip the first operand because it is assigned to result already
            result **= i
        return result
