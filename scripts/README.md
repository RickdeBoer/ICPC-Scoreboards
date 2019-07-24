## Data processing
The following general pipeline was used to process the data. It comes down to reading in and structuring different parts of the data files.

![alt text](https://github.com/RickdeBoer/ICPC-Scoreboards/blob/master/images/data_processing_steps.png "Data structure")

#### Explanation of processing steps
* _locate_ and _collect_ resulted in the raw dataset in the other folder
* _process into CSV_ was done manually or with tools such as https://www.becsv.com/table-csv.php
* _cleaning and structuring_ was done by adapting a **structuring example** file
* _transform and import_ each formatted file was entered into a database
* _add missing information_ was done mostly manually by e.g. filling in countries
* _enhance/correct information_ was done by manual inspection. For example, non-trivially abriviated universities were converted to full university names. The **convert university.py** file was used to then uniformly write the universities, other work was done manually. 

#### Files
Each file in this folder is used in a different part of the ETL process.
* **Structuring example_x** files are shown as an example of how to process a certain region and format. These can be adapted to work on other formatted files and regions as well.
* **Structuring help_scoreformatter.py** contains several different ways of formatting scores. A function was copied and placed in the the main structuring file.
* **Convert university.py** was used to convert differently written universities in a uniform way. 
