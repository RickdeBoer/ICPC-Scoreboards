## Data structure
The data is structured as is described in the ERD below.

![alt text](https://github.com/RickdeBoer/ICPC-Scoreboards/blob/master/imgs/data_structure.png "Data structure")

## Notes
Each of the files in this dataset is a separate part of the data, containing the following information: <br />
* **Competition** contains basic information about competitions
* **Competition_year** contains information which years are present in this set for each competition
* **Entries** contains all meta information about teams and their final score and time
* **Probleminfo** contains minimal information about each problem. _A note here is that the number of problems in this set is not equal to that in competition_year. This is because some problems have 0 solutions and 0 attempts. These specific problems are: <br />
1 J <br />
8 F <br />
35 D <br />
36 I <br />
41 L <br />
49 J <br />
53 A <br />
58 G <br />
64 I <br />
70 I <br />
75 C <br />
82 A <br />
103 C G <br />
104 B J <br />
121 E <br />
123 C I <br />
126 J <br />
Also, in 47 (Latin America 2016) Problem E is disqualified and removed, so there is no information available for that problem_
* **Solution** contains information about the attempts and solutions from each team. If no time is given for a specific entry, then that problem is not solved by that team.
