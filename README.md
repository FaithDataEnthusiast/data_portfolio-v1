# ETL Pipeline

Welcome to my ETL portfolio project, which is designed to extract, transform and load invoice transactions 
data from a Redshift database to an S3 bucket. This project is designed to help you understand how to work 
with data transformation, Docker, and AWS services as a beginner.

## Introduction
The project's main goal is to extract invoice transaction data from a Redshift database, filter the data 
according to specified requirements, transform the data to eliminate duplicates, transform the data type of 
the invoice_date field, and load the transformed data to an S3 bucket. The transformed data is then loaded 
into a Docker container to make it easier for you to work with.

1. Connect to a Redshift Database filter and extract transactional data.
2. Transform the data - identify duplicates and remove
3. Transform invoice_date data type to datetime
4. Load transformed data to S3 bucket

## System Requirements

#### Docker for Mac : [Docker >= 4.1.1](https://docs.docker.com/desktop/install/mac-install/)

#### Docker for Windows:
1. Download [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/) for Windows.

Before you launch Docker Desktop, you should make sure that your WSL(Windows Subsystem for Linux) Ubuntu 
environment is set as the default WSL distribution. This will ensure that Docker uses the Ubuntu environment 
for its Linux containers.
2. From your Windows Store Download WSL or update if already installed
3. From your Windows Store Download Ubuntu or update if already installed
4. Open a terminal window in Ubuntu by clicking on the Ubuntu icon in the taskbar and searching for 
   "terminal".
5. Update the package list and install any updates that are available by running the following commands:
```bash
  sudo apt-get update                                  
  sudo apt-get upgrade                                                    
```
6. Install Docker by running the following command:
```bash
  sudo apt-get install docker.io                                                                          
```
7. Once the installation is complete, start the Docker service by running the following command:
```bash
  sudo systemctl start docker                                                                             
```
8. To confirm that Docker is running correctly, run the following command:
```bash
  sudo docker version                                                                                     
```

## How to Execute the Code

### To execute the code, follow these steps:

1. Clone the repository to your local machine.
2. Ensure that Docker is running on your system.
3. Navigate to the directory where you cloned the repository.
4. Open the .env file and enter your environment variables that is AWS credentials and Database Credentials.
5. Open the terminal and first run it locally to build the image
```bash
docker image build -t etl .
```
6. Run the Docker container.
```bash
docker run --env-file .env etl .
```
7. Once the container is running, open PyCharm and open the main.py file.
8. Run the main.py file to execute the code.

## Files Included

### This project includes the following files:

- main.py: This is the main file that executes the code.
- extract.py: This file contains the code for extracting data from a Redshift database.
- transform.py: This file contains the code for transforming data by removing duplicates and fixing data types.
- load_data_to_S3: This file contains the code for loading data to an S3 bucket.
- .env: This file contains all environment variables required.
- Dockerfile: This file contains the instructions for building the Docker container.
- requirements.txt: This file contains the required packages for the Docker container.

## Conclusion
Thank you for taking the time to review my portfolio project. I hope that this project has provided you with 
a better understanding of how to extract, transform, and load data from a Redshift database to an S3 bucket 
using Docker and AWS services. Please let me know if you have any questions or comments.