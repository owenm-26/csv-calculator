import csv
import numpy as np
from Calculator import Calculator
validMethods = ["add", "subtract", "multiply", "divide", "exponentiate"]
class CSVCalculatorHandler:
    
    def __init__(self):
        self.unsavedHistory = np.asarray(['input_file','operation','result','error']) # array variable to hold unsaved history ? 

    def process_csvs(self, filenames, output_prefix="output"):
        # iterate through each file
        for file in filenames:
            with open(file, 'r') as csvfile:
                oneFile = csv.reader(csvfile)

            # create a new CSV to write to throughout loop of single file
            outputFileName = output_prefix + file
            with open(outputFileName, 'w'):
                writer = csv.writer(file)
                writer.writerows([['result', 'error']])
            
            # iterate through each row of the CSV selected
            for row in oneFile:
                i = 0 #counter

                # instantiate inputs to function
                params = []
                method = ""
                error = 0
                result = ""
                
                # assign params var
                while(not row[i].isalpha()):
                    params += [int(row[i])] #cast to int and add to params list
                    i+=1
                
                # assign method var
                method = row[i] 
                if(method not in validMethods):
                    error = 3
                    print("Unknown Operator")
                
                try:
                    calc = Calculator()
                    # NEED TO CALL FUNCTION HERE (switch statement)
                    if(method == ("add")):
                        result = calc.add(params)
                    elif(method == ("subtract")):
                        result = calc.subtract(params)
                    elif(method == ("multiply")):
                        result = calc.multiply(params)
                    elif(method ==("divide")):
                        result = calc.divide(params)
                    else:
                        result = calc.exponentiate(params)

                #Error handling
                except:
                    error = 4
                    print("Unknown Error")
                
                # write new row to file
                with open(outputFileName, 'a') as workingFile:
                    writer = csv.writer(workingFile)
                    writer.writerows([result, error])
                    print('Row written: Method=' + method + ", params=" + params + ", \n**result=" + result + ", error=" + error)
                self.save_to_history(file, method, result, error)

    def save_to_history(self, filename, operation, result, error_code):
        # write method inputs to the global variable 
        self.unsavedHistory = np.append(self.unsavedHistory, [filename,operation,result,error_code])

    def history_export(self, export_filename):
        with open(export_filename, 'w'):
                writer = csv.writer(export_filename)
                writer.writerows([self.unsavedHistory])

    def testing(method, params, expected):
        calc = Calculator
        if(method == ("add")):
            result = calc.add(params)
        elif(method == ("subtract")):
            result = calc.subtract(params)
        elif(method == ("multiply")):
            result = calc.multiply(params)
        elif(method == ("divide")):
            result = calc.divide(params)
        else:
            result = calc.exponentiate(params)
        
        if(result[1] == 1):   # divide by zero catcher
            assert result[1] == expected
        
        else:
            assert result[0] == expected
    
    def unitTests():
        cch = CSVCalculatorHandler
        print('Calculator function Test Cases:')
        print('Calculator.add():') #add tests
        print("int + int: ")
        if (cch.testing('add', [1,2], 3) != AssertionError):
            print('----pass----')
        print("double + double: ")
        if (cch.testing('add', [1.0,2.0], 3.0) != AssertionError):
            print('----pass----')
        print("int + double: ")
        if (cch.testing('add', [1,2.0], 3.0) != AssertionError):
            print('----pass----')
        print("lots of params: ") 
        if (cch.testing('add', [1,2,3,4], 10) != AssertionError):
            print('----pass----')
        
        print("/n***********************************")

        print('Calculator.subtract():') #subtract tests
        print("int - int: ")
        if (cch.testing('subtract', [2,1], 1) != AssertionError):
            print('----pass----')
        print("double - double: ")
        if (cch.testing('subtract', [2.0,1.0], 1.0) != AssertionError):
            print('----pass----')
        print("int - double: ")
        if (cch.testing('subtract', [2,1.0], 1.0) != AssertionError):
            print('----pass----')
        print("lots of params: ") 
        if (cch.testing('subtract', [5,2,1], 2) != AssertionError):
            print('----pass----')
        print("negative int - double: ") 
        if (cch.testing('subtract', [1,3.0], -2.0) != AssertionError):
            print('----pass----')

        
        print("/n***********************************")

        print('Calculator.multiply():') #multiply tests
        print("int * int: ")
        if (cch.testing('multiply', [2,1], 2) != AssertionError):
            print('----pass----')
        print("double * double: ")
        if (cch.testing('multiply', [2.0,1.0], 2.0) != AssertionError):
            print('----pass----')
        print("int * double: ")
        if (cch.testing('multiply', [2,1.0], 2.0) != AssertionError):
            print('----pass----')
        print("lots of params: ") 
        if (cch.testing('multiply', [5,2,1], 10) != AssertionError):
            print('----pass----')
        print("int * -double: ") 
        if (cch.testing('multiply', [1,-3.0], -3.0) != AssertionError):
            print('----pass----')
        print("multiply by 0: ") 
        if (cch.testing('multiply', [1,-3.0,0], 0.0) != AssertionError):
            print('----pass----')

        print("/n***********************************")

        print('Calculator.divide():') #divide tests
        print("int / int: ")
        if (cch.testing('divide', [1,2], 0.5) != AssertionError):
            print('----pass----')
        print("double / double: ")
        if (cch.testing('divide', [4.0,4.0], 1.0) != AssertionError):
            print('----pass----')
        print("int / double: ")
        if (cch.testing('divide', [5,2.5], 2.0) != AssertionError):
            print('----pass----')
        print("lots of params: ") 
        if (cch.testing('divide', [10,2,5], 1) != AssertionError):
            print('----pass----')
        print("int / -double: ") 
        if (cch.testing('divide', [6,-3.0], -2.0) != AssertionError):
            print('----pass----')
        print("divide by 0: ") 
        if (cch.testing('divide', [1,-3.0,0], 1) != AssertionError):
            print('----pass----')

        print("/n***********************************")

        print('Calculator.exponentiate():') #exponentiate tests
        print("int ** int: ")
        if (cch.testing('exponentiate', [1,2], 1) != AssertionError):
            print('----pass----')
        print("double ** double: ")
        if (cch.testing('exponentiate', [4.0,2.0], 16.0) != AssertionError):
            print('----pass----')
        print("int ** double: ")
        if (cch.testing('exponentiate', [5,2.0], 25.0) != AssertionError):
            print('----pass----')
        print("lots of params: ") 
        if (cch.testing('exponentiate', [2,2,2], 16) != AssertionError):
            print('----pass----')
        print("int ** -double: ") 
        if (cch.testing('exponentiate', [2,-2.0], 0.25) != AssertionError):
            print('----pass----')
        print("exponentiate by 0: ") 
        if (cch.testing('exponentiate', [1,-3.0,0], 1) != AssertionError):
            print('----pass----')



if __name__ == '__main__':
    cch = CSVCalculatorHandler
    cch.unitTests()




####### General Sources ########
## CSV Library Documentation: https://docs.python.org/3/library/csv.html
## CSV Examples: https://www.geeksforgeeks.org/writing-csv-files-in-python/ 
## Numpy Array to CSV: https://stackoverflow.com/questions/6081008/dump-a-numpy-array-into-a-csv-file
