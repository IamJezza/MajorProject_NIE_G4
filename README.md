# ATPG using Genetic Algorithm
This is the major project work of [POOJA](), [ASHISH](), [JAGRUTH]() and [SUHAS](https://github.com/IamJezza) of The national institute of engineering, Mysuru. 

## Tools required/ used
* iverilog
* vvp
* python 3.8
  * `random`
  * `pandas`
  * `numpy` 
  * `subprocess`
  * `multiprocessing`
* MatLab

## Discription of files
The folder `FullAdders` consist of verilog implementation of full adder with single stuck at faults. `full_adder0.v` is the fault-free and the rest are faulty implementations. 

Folder `TestBenches` contains the test bench implementation of 8-bit excess 3 encoder. `test_bench0.v` is for fault-free case, rest are for faulty case. 

`process.py` uses shell commands to generate verilog code for each combination of full adder and test bench i.e. Excess 3 encoder. The  Folder `Results` will contain all outputs for each combination in text file format `out{test-Bench-code}[{0indicated to full_adder0.v}, {the faulty full adder code}]`. 

`TXTtoCSV.py` collates all the output text files to a single text files of `DATA.txt`, this can be used to generate the `DATA.csv` file and further the **`transDATA.csv`**. 
> **`transDATA.csv`** contains the data formated to be used with pandas, use this file for all further processing and **don't make changes to this.** 

The folder `genetic_algorithm` contains both the genetic algorithm implementation and ATPG testing codes

