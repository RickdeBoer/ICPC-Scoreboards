## Data processing
The following general pipeline was used to process the data. It comes down to reading in and structuring different parts of the data files.

![alt text](https://github.com/RickdeBoer/ICPC-Scoreboards/blob/master/images/data_processing_steps.png "Data structure")

#### Explanation of processing steps
* _locate_ and _collect_ resulted in the raw dataset in the 'raw data' folder.
* _process into CSV_ was done manually or with the help of tools such as https://www.becsv.com/table-csv.php by processing only the scoreboard table in the raw file.
* _cleaning and structuring_ was done by adapting and running a **structuring example** file.
* _transform and import_ each formatted file could now be entered into a database.
* _add missing information_ was done mostly manually by e.g. filling in countries.
* _enhance/correct information_ was done by manual inspection. For example, non-trivially abriviated universities were converted to full university names. The **convert university.py** file was used to then uniformly write the universities, other work was done manually. 

#### Files
Each file in this folder is used in a different part of the ETL process.
* **Structuring example_x** files are shown as an example of how to process a certain region and format. These can be adapted to work on other formatted files and regions as well.
* **Structuring help_scoreformatter.py** contains several different ways of formatting scores. The appropriate formatting function here was copied and used the main structuring file.
* **Convert university.py** was used to convert differently written universities in a uniform way. 
