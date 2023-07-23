# To automate the backup process of files from a specific folder to a backup location
import os
import shutil
from datetime import datetime

def backup_files(source_folder, backup_folder):
  
                                                                        # Function automate the process of backing up files from source folder to backup folder.
    try:
                                                                        # Create a new folder in the backup directory with the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_path = os.path.join(backup_folder, f"backup_{timestamp}")
        os.makedirs(backup_path)

                                                                        # Get a list of all files in the source folder
        files = os.listdir(source_folder)

                                                                        # Copy each file from the source folder to the backup folder
        for file in files:
            source_file_path = os.path.join(source_folder, file)
            backup_file_path = os.path.join(backup_path, file)
            shutil.copy(source_file_path, backup_file_path)

        print("Backup completed successfully.")
    except Exception as e:
        print(f"An error occurred during the backup process: {e}")
