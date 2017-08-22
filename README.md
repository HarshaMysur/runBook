# runBook
Python project runBook automation task to have a master control a bunch of servers as minions

I built the project using Python and Flask.

This project has a Master Server (Master.py) that handles the user's request by calling respective minions to complete the task.
I have implemented 3 minion servers.

minion1.py -> To Handle mkdir (create directory) requests.
minion2.py -> To Handle cp (Copy files) requests.
minion3.py -> To handle ls (List files) requests.

I have Dockerized the project.

minion1.py - It creates the directory if not present in the common_folder 
             I have completed error handling for if the directory already present by sending out appropriate message to the user.

minion2.py - It copies the files from common_folder to a new file name. It can handle .txt, .docx, .xlsx. 
             Please provide the complete name of the file with extension.
             I have completed the error handling for source_file not present by sending out appropriate message to the user.
            
minion3.py - It lists all the files in the common_folder.

Execution Steps:
1. Please clone the project from my github to your directory.
2. From the Docker terminal, enter into the folder Dock.
3. Execute the below commands
   -> docker-compose build
   -> docker-compose execute
4. From web browser please go to 192.168.99.100:5000

Devops:
I have automated the deployment of all the servers by wriring Dockerfile for each of the servers in its respective folders.
Then I have scripted the docker-compose.yml to have these servers up and running in specific ports.

Folder-Structure:

--Dock
 |
 |--master
 |    |
 |    |--templetes
 |    |
 |    |--Master.py
 |    |
 |    |-- Dockerfile
 |    |
 |    |--requirements.txt
 |
 |--minion1
 |    |
 |    |--requirements.txt
 |    |
 |    |--minion1.py
 |    |
 |    |-- Dockerfile
 |  
 |--minion2
 |    |
 |    |--requirements.txt
 |    |
 |    |--minion2.py
 |    |
 |    |-- Dockerfile
 |  
 |--minion3
 |    |
 |    |--requirements.txt
 |    |
 |    |--minion3.py
 |    |
 |    |-- Dockerfile
 |
 |--docker-compose.yml
 |
 |--common_folder
 
