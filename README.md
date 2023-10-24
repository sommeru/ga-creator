# GA-Creator
A creator for KNX Group Addresses. Just provide a YAML file and the group creator will do a the magic to provide the ETS with an importable csv file.

## Usage
- Create YAML file according to provided skeleton files.
- poetry install
- .venv/bin/python ga-creator.py [FILE].yaml 

## Structure of group addresses
Currently on the following GA-structure is supported:  
DEVICETYPE / FLOOR / Device1-DATAPOINT1  
DEVICETYPE / FLOOR / Device1-DATAPOINT2  
DEVICETYPE / FLOOR / Device1-DATAPOINTX  
DEVICETYPE / FLOOR / ...  
DEVICETYPE / FLOOR / Device2-DATAPOINT1  
DEVICETYPE / FLOOR / Device2-DATAPOINT2  
DEVICETYPE / FLOOR / Device2-DATAPOINTX  
DEVICETYPE / FLOOR / ...
