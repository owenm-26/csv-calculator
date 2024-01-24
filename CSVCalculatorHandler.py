class CSVCalculatorHandler:
    def __init__(self):
        pass
        # array variable to hold unsaved history ?

    def process_csvs(self, filenames, output_prefix="output"):
        pass
        # create output csv
        # read input csv
            # store numbers (operands) in an array
            # checks if operator is a thing
                # if it is then call method and store result
                # assign error code 
            # write to file called "output_prefix_<file_name>"
    
        # assign necessary variables and call save_to_history()

    def save_to_history(self, filename, operation, result, error_code):
        pass
        # write method inputs to the global variable 

    def history_export(self, export_filename):
        pass
        # write (without erasing)? the global variable to a "export_filename" (history.txt)
        # clear global variable


if __name__ == '__main__':
    print("write some code, your testing software will call this main function")
