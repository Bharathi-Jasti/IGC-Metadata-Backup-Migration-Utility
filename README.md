# IGC-Metadata-Backup-Migration-Utility
# IGC Metadata Backup and Migration Utility
DESCRIPTION                                                                                                                                                                                        
IGC Metadata Backup and Migration tool is a Customized utility that focuses on enhancing content Migration and Backup automation process for multiple environments in single instance.
  
                                                                                                           
FUNCTIONALITY                                                                                          
   
It provides Backup storage files for multiple Assets in different environments at same instance and parallelly migrate them to required/all environments (Dev,QE and Production) with single utility.                                                                                        
INSTRUCTION                                                                                             
                                                                                             
Copy this backup folder with Run_backup script to your local directory then executes at Anaconda prompt (Python) as below:                                    
Run_backup.py <userID> <Password> <Asset File> <backup>
Then this will show us as imported or exported with backup or import process (["all","backup","qa","prd","prd_import","qa_import"]
                                                                                                           
RETURNCODE                                                                                                                                                                                       
1 - Required parameter not passed. Fix: Please pass the user/Password/file/cmd parameters while backup script execution
2 - No file found. Fix: Please check the excel file availability on your backup  directory with assets to be migrated/imported.               





This utility tool is developed out of the below needs:
1.	To Backup the Metadata content across environments using single utility tool 
2.	To Migrate/Import the Metadata content in multiple environments using single utility. 
3.	Quick storage and Manual Versus Automated Approach over 60% reduction in effort
4.	Easy to plug in anywhere.
How to install:
You'll need the following components installed:
Python(Anaconda ) – Install Python and Import all the pandas to run the script
IGC Application (Information Governance catalog- Business Glossary) - Access is required.
How to use:
1.	Once Python is installed with required Pandas, Copy the python script including backup folder to current home directory.
2.	Change the Server name (yellow)to required IGC server environment (QA/prod) in Run_backup.py script.
3.	Keep the assets to be imported in Excel file in backup folder with the given components in script as (host,db,schema and table)
4.	Execute the script like "Python Run_backup.py <userID> <Password> <Asset File> <backup> 
5.	This script will show output with number of Assets exported or migrated or both based on the selection given by user
