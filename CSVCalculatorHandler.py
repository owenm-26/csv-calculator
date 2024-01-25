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
                if(len(params) < 2): #make sure the call has enough params
                    error = 2
                    print("Bad Number of Params")
                
                # assign method var
                method = row[i] 
                if(method not in validMethods):
                    error = 3
                    print("Unknown Operator")
                
                try:
                    calc = Calculator()
                    # NEED TO CALL FUNCTION HERE (switch statement)
                    if(method.equals("add")):
                        result = calc.add(params)
                    elif(method.equals("subtract")):
                        result = calc.subtract(params)
                    elif(method.equals("multiply")):
                        result = calc.multiply(params)
                    elif(method.equals("divide")):
                        result = calc.divide(params)
                    else:
                        result = calc.exponentiate(params)
                #Error handling
                except ZeroDivisionError:
                    error = 1
                    print("Divided by Zero")

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


if __name__ == '__main__':

    print("write some code, your testing software will call this main function")






####### General Sources ########
## CSV Library Documentation: https://docs.python.org/3/library/csv.html
## CSV Examples: https://www.geeksforgeeks.org/writing-csv-files-in-python/ 
## Numpy Array to CSV: https://stackoverflow.com/questions/6081008/dump-a-numpy-array-into-a-csv-file
