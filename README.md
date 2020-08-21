# kb-Anonymity-Data-Protection-and-Privacy
Final period project of the course *Data Protection & Privacy*: an implementation of the *KB-anonymization* technique, a framework useful for anonymizing data for testing purpose.

## Getting started
To run the project is sufficient to clone or download this repository, with the command:
```
git clone https://github.com/A-725-K/kb-Anonimity-Data-Protection-and-Privacy.git
```
Our project relies on **Z3** solver, if you don't have it installed, please refer to their [main page](https://github.com/Z3Prover/z3).

## How to launch the program
You have only to run this simple command from your terminal:
```
python3 main.py [-h] -i INPUT_FILE -o OUTPUT_FILE -a ALGORITHM -k K -c CONFIG_FILE
```
where:
<ul>
  <li>-<i>i</i>: choose a dataset in json format as input</li>
  <li>-<i>o</i>: choose an output file, it will be in json format</li>
  <li>-<i>a</i>: choose the technique to apply to enhance the anonymization of data
    <ul>
      <li><b><i>P-F</i></b>: same Path, no Field repeat</li>
      <li><b><i>P-T</i></b>: same Path, no Tuple repeat</li>
    </ul>
  </li>
  <li>-<i>k</i>: the degree of anonymization you would apply on data</li>
  <li>-<i>c</i>: a configuration file that contains the range constraints to apply over the fields of tuples in dataset</li>
</ul>

Otherwise you can simply launch the *test_runner* utility:
```
cd utilities
./test_runner
```

## How the *repo* works
<ul>
  <li><b><i>datasets</i></b>: it contains all the data used in our experiments, and a bash script to gather them through an open API</li>
  <li><b><i>kb_anonymity</i></b>: the core of the program, it contains the library proposed by us</li>
  <li><b><i>mappings</i></b>: each file contains a map that represents some values transformed in integer</li>
  <li><b><i>main.py</i></b>: the entry point of the program, the users would like to modify it depending on their needs</li>
  <li><b><i>p_test.py</i></b>: the SUT, the user have to encode its program like this</li>
  <li><b><i>stat</i></b>: contains graphics of the results produced by the test runner</li>
  <li><b><i>utilities</i></b>
    <ul>
      <li><b><i>configs.txt</i></b>: an example of configuration file, it must follow a specific syntax</li>
      <li><b><i>json_reader.py</i></b>: a utility to parse the dataset, the user should modify it depending on their data</li>
      <li><b><i>draw_graphics.py</i></b>: a script that plot the results of the algorithms executed in batch</li>
      <li><b><i>test_runner.sh</i></b>: a simple script to perform some experiments with different parameters to understand the behavior of the algorithm</li>
    </ul>
  </li>
</ul>

**1. *p_test* format** <br>
p_test must contains a function called P_Test which simulates the behaviour of the system we want to test. It takesa raw tuple and a list of constraints as input(initially empty). A *constraint* is a triple (*field*, *operation symbol*, *value*).

**2. *configs* format** <br>
In this file the user specify the range constraints for each field of a tuple. The first row must contain all the fields present in the dataset as strings. Then each row must follow this syntax: if the constraints are related to a single field:
```
field:(([op_symbol value]+),?)+
```
otherwise, if the constraints involve two related fields:
```
#field1 op_symbol field2
```
The *comma* symbol separates the conditions to be put in **OR**, while the *whitespaces* are for conditions in **AND**.

## Authors

* **<i>Andrea Canepa</i>** - Computer Science, UNIGE - *Data Protection and Privacy a.y. 2018/2019*
* **<i>Alessio Ravera</i>** - Computer Science, UNIGE - *Data Protection and Privacy a.y. 2018/2019*
