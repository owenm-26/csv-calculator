# CSV-Calculator

**Objective:** To create a calculator program that reads operations and operands from CSV files,
performs the operations, and saves the result to another CSV file. Furthermore, the program will maintain a history of
all operations and results.


- **Error Codes**:
  Below is a table of error codes, your program is expected to categorize and record errors according to this table.

  | Error                | Code |
  | -------------------  | ---- |
  | No Error             | 0    |
  | Division by Zero     | 1    |
  | Bad Number of Params | 2    |
  | Unknown Operator     | 3    |
  | Unknown Error        | 4    |

- **Operator Specifications**:
  - **Addition:** The result of adding all the numbers together. Supports any number of operands greater than 2.
  - **Subtraction:** The result of subtracting all the numbers from the first number. Supports any number of operands greater than 2.
  - **Multiplication:** The result of multiplying all the numbers together. Supports any number of operands greater than 2.
  - **Division:** The result of dividing the first number by the second number. Supports only two operands.
  - **Exponentiation:** The result of raising the first number to the power of the second number. Supports only two operands.
---

#### **Specifications:**

- **process_csv:** This method should read each CSV file provided in the `filenames` list, calculate results using
  the `Calculator` class, and save the results to a new CSV file prefixed with `output_prefix`. Each input file should have exactly one output file.

- **save_to_history:** After processing each row in the input CSV, this method should save details about the operation,
  its result, and any errors to the history of the `CSVCalculatorHandler` class. The history should be stored on the class and not saved to a file until the user calls the `history_export()` function.

- **history_export:** This method should export the entire history of operations, results, and errors to a CSV file
  specified by `export_filename`.

---

**. Example:**

Below is an example input and output:

`python3 CSVCalculatorHandler.py input.csv`

File name: `input.csv`

```
5,10,add
8,2.5,3.5,multiply
7,3,subtract
9,0,divide
2,3,exponentiate
10,divide
10,2,unknown_operator
```

File name: `output_0.csv`

```
result,error
15.0,0
70.0,0
4.0,0
,1
8.0,0
,2
,3

```

File name: `history.txt`

```
input_file,operation,result,error
input.csv,"5,10,add",15.0,0
input.csv,"8,2.5,3.5,multiply",70.0,0
input.csv,"7,3,subtract",4.0,0
input.csv,"9,0,divide",,1
input.csv,"2,3,exponentiate",8.0,0
input.csv,"10,divide",,2
input.csv,"10,2,unknown_operator",,3

```


