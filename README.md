# ETL Pipeline

Welcome to my ETL portfolio project, which is designed to extract, transform and load invoice transactions 
data from a Redshift database to an S3 bucket. This project is designed to help you understand how to work 
with data transformation, Docker, and AWS services as a beginner.

### Introduction
The project's main goal is to extract invoice transaction data from a Redshift database, filter the data 
according to specified requirements, transform the data to eliminate duplicates, transform the data type of 
the invoice_date field, and load the transformed data to an S3 bucket. The transformed data is then loaded 
into a Docker container to make it easier for you to work with.

1. Connect to a Redshift Database filter and extract transactional data.
2. Transform the data - identify duplicates and remove
3. Transform invoice_date data type to datetime
4. Load transformed data to S3 bucket

### System Requirements

#### Docker for Mac :

#### Docker for Windows:
1. From your Windows Store Download WSL or update if already installed
2. From your Windows Store Download Ubuntu or update if already installed
3. Open a terminal window in Ubuntu by clicking on the Ubuntu icon in the taskbar and searching for 
   "terminal".
4. Update the package list and install any updates that are available by running the following commands:
```bash
  sudo apt-get update
  sudo apt-get upgrade                                                                                                           
```
4. dfdf

  

