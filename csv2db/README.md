# CSV to DB merger
#### Video Demo:  [link](https://youtu.be/cz_SF9zM6KQ)
## Introduction:
Hello, my name is Chih-ho Howard Tang, from Taiwan.\
My “CSV to DB merger” is a batch CSV to SQL database file converter. It reads multiple CSV files and writes them into a single SQL database, where the data is structured to be easily readable by computers for data analysis.

## Overview:
This is designed for when there are multiple CSV files with the same format, such as data logged for multiple experiments where each data set is its own file.
For example, AQI data organized by region, where you can treat the “date” as a key to analyze Particulate Matter (PM) ratings across multiple regions.\
https://aqicn.org/data-platform/register/

## Features:
The program iterates over multiple CSV files and writes the data into a single database, creating a table per CSV with the filename as table name, creates the schema identical to the CSV’s format, and determines the respective SQL data type based on the data (INT, FLOAT, DATE/DATETIME, TEXT). It also creates an additional table that contains all of the names of the tables.

By creating an additional index that contains all of the table names, this allows any other programs to iterate automatically over all of the tables.

## Usage:
The “convert.py” will read all of the CSV files inside the local folder “csv”, and write the data into a “data.db”. Using ".schema", you will be able to see how the tables are structured. Note the additional table, called "tables", which contains all of the other table names.

The example reader “reader.py” will be able to iterate automatically over all of the tables using the "tables" list, and retrieve data with a specified condition, such as PM2.5 > 80. The returned data would be organized as “table name” and its data. This data can be used in another program for analysis.

The "convert.py" is dynamic, and can be used on many files with varying sizes of any format.

## Notes:
I actually designed this program to solve a problem in another project, where I was trying to analyze some AQI data. I was creating a script for merging the specifically AQI formatted CSV files for different regions, when I decided to make it more dynamic, to be able to organize any other CSV files too. The "reader.py" is just a proof of concept, where you can see how the data can be used. Anyways, I hope this program helped you in some way. Thank you for reading!


## Example schema
CREATE TABLE tables (\
----id INTEGER PRIMARY KEY AUTOINCREMENT,\
----name TEXT);


CREATE TABLE Taipei (\
----date DATE,\
----pm25 INT,\
----pm10 INT,\
----o3 INT,\
----no2 INT,\
----so2 TEXT,\
----co INT);