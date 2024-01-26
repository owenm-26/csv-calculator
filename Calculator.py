class Calculator:
    def add(operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = 0
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result += i
        
        return [result, error]
    
    def subtract(operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = 0
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result -= i
        return [result, error]

    def multiply(operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = 0
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result *= i
        return [result, error]

    def divide(operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = 0
        elif(0 in operands[1:]): # checks if dividing by 0
            error = 1
            result = 0
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result /= i
        return [result, error]

    def exponentiate(operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = 0
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result **= i
        return [result, error]
