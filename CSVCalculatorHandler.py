import csv
import sys
from Calculator import Calculator
class CSVCalculatorHandler:
    
    def __init__(self):
        self.unsavedHistory = [['input_file','operation','result','error']] # array variable to hold unsaved history ? 

    def process_csvs(self, filenames, output_prefix="output"):
        validMethods = ["add", "subtract", "multiply", "divide", "exponentiate"]
        fileNum = 0
        # iterate through each file
        for file in filenames:
            newRows = [['result', 'error']]
            #open first file
            with open(file, 'r') as csvfile:
                oneFile = csv.reader(csvfile)
    
                # iterate through each row of the CSV selected
                for row in oneFile:
                    i = 0 #counter

                    # instantiate inputs to function
                    params = []
                    method = ""
                    error = 0
                    result = ""
                    output = []
                    processedInput = ""
                    
                    # assign params var
                    for arg in row[:-1]:
                        params += [float(arg)] #cast to float and add to params list
                   
                    # assign method var
                    method = row[-1] #it should be the last argument

                    if(method not in validMethods):
                        error = 3
                        print("Unknown Operator")
                    
                    if(error == 0):
                        try:
                            calc = Calculator()
                            # NEED TO CALL FUNCTION HERE (switch statement)
                            if(method == ("add")):
                                output = calc.add(operands=params)
                            elif(method == ("subtract")):
                                output = calc.subtract(operands=params)
                            elif(method == ("multiply")):
                                output = calc.multiply(operands=params)
                            elif(method ==("divide")):
                                output = calc.divide( operands=params)
                            else:
                                output = calc.exponentiate( operands=params)
                            result = output[0]
                            error = output[1]

                        #Error handling
                        except Exception as e:
                            error = 4
                            print("Unknown Error: ", e)

                    #add to running newRows var
                    newRows += [[result, error]]
                    
                    #prepare var for history
                    for i in range(len(row)):
                        processedInput += row[i]
                        if(i< len(row)-1):
                            processedInput += ","
                    self.save_to_history(filename=file, operation=processedInput, result=result, error_code=error)

            # create a new CSV to write to throughout loop of single file
            outputFileName = output_prefix + "_" + str(fileNum) + ".csv"
            with open(outputFileName, 'w', newline='') as outputFile:
                writer = csv.writer(outputFile)
                
                # Write new rows
                for row in newRows:
                    writer.writerow(row)
            fileNum +=1
            

    def save_to_history(self, filename, operation, result, error_code):
        # write method inputs to the global variable 
        self.unsavedHistory += [[filename,operation,result,error_code]]

    def history_export(self, export_filename):
        print("------------------\n", self.unsavedHistory, "\n------------------")
        with open(export_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in self.unsavedHistory:
                    writer.writerow(row)
                

    def testing(method, params, expected):
        calc = Calculator()
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
        cch = CSVCalculatorHandler()
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
    cch = CSVCalculatorHandler()
    #cch.unitTests() ##uncomment to test calc methods

    if(len(sys.argv) < 2):
        print('Need at least 1 csv to process')
    else:
        # Extract file names from command-line arguments
        args = []
        for arg in sys.argv[1:]:
            args += [arg]
        
        cch.process_csvs(filenames=args, output_prefix='output')

        cch.history_export(export_filename='history.txt')




####### General Sources ########
## CSV Library Documentation: https://docs.python.org/3/library/csv.html
## CSV Examples: https://www.geeksforgeeks.org/writing-csv-files-in-python/ 
## Numpy Array to CSV: https://stackoverflow.com/questions/6081008/dump-a-numpy-array-into-a-csv-file
## Command line argument lesson: https://machinelearningmastery.com/command-line-arguments-for-your-python-script/ 
