class Calculator:
    def add(self, operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = ""
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result += i
        
        return [result, error]
    
    def subtract(self, operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = ""
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result -= i
        return [result, error]

    def multiply(self, operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = ""
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result *= i
        return [result, error]

    def divide(self, operands):
        error = 0
        if(len(operands) < 2):
            error = 2
            result = ""
        elif(0 in operands[1:]): # checks if dividing by 0
            error = 1
            result = ""
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result /= i
        return [result, error]

    def exponentiate(self, operands):
        error = 0
        if(len(operands) != 2):
            error = 2
            result = ""
        else:
            result = operands[0]
            for i in operands[1:]: #skip the first operand because it is assigned to result already
                result **= i
        return [result, error]
