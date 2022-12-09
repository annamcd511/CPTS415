Project Demonstration
This set of programs takes approximately 2 minutes to run.
This set of programs is intended to do the following, broken down into three parts:
1 -- Retrieve only the documents for a specified bird as well as the latitude, longitude, and observation dates of said bird. 
Output these results into a csv file
2 -- From that csv file, record the number of times the same latitude, longitude, and observation date appears at the same time using
a mapReduce program. Then output these results into a txt file.
3 -- Create several graphs of the data found from step two. The first graph is observation counts over time. The second is an animated 
geoScatter map that looks at how the location of the bird changes year by year. The last graph is a geoscatter map that has an overall 
look at where the bird is seen over the years.  

Methodology
* Query
    - Performs a specific query on the dataset so that only the bird of interest is pulled. 
* Filter
    - Filters the data so that only the fields of interest are retrieved
* mapReduce 
    - Combines data together based on given keys
* graph
    - provides visual information of statistics


Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python
* You have a Windows machine. OS 10 or 11 are the current versions supported.

Libraries Used
The following libraries were used and are required to run this program:
* csv
* PyMongo
    -- install using python3 -m pip install pymongo
    -- allows connection to a MongoDB server to read and write data
* mrjob
    -- install using pip install mrjob
    -- creates a mapReduce program that can be used in conjunction with hadoop
* hadoop 
    -- see the following page to install: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html 
* pandas
    -- install using pip install pandas
* plotly
    -- intsall using pip install plotly==5.11.0
    -- graphing tool than can make interactive plots
* geopandas
    -- install using pip install geopandas
    -- similar to pandas but combines like geographical occurences 
* matplotlib
    -- install using python -m pip install -U matplotlib
    -- used to visualize statistical data

Using Project Demonstate
To use Programming Assignment 3, follow these steps:
1) Navigate to the folder (using a file navigator) in which the program resides. 
2) type the following command: python demo_part1.py 
    - Take note of the name of bird you chose and how its name is written
3) after the first command has finished running type the following command:
python demo_part2.py "Bird_name.csv" > "Bird_name.txt"
    - Change Bird_name to be exactly the bird name you typed above for demo_part1.py
4) after the second commmand has finished running, type the following command:
python demo_part3.py
5) Navigate to the folder where the program resides and view the results.