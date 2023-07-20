# Complex data migration and transformation project
import pandas as pd
import os

# Define source data paths
legacy_data_folder = "/path/to/legacy/data/folder"

# Define target data path
cloud_platform_data_path = "/path/to/cloud/platform/data"

# Define transformation functions
def transform_data(data):
  
    # Apply data transformation logic
    transformed_data = data.apply(...)  
  
    return transformed_data

# Iterate through legacy data files
for file_name in os.listdir(legacy_data_folder):
    file_path = os.path.join(legacy_data_folder, file_name)
    
    # Check if file is a valid data file
    if file_name.endswith(".csv"):
      
        # Read data from the legacy file
        legacy_data = pd.read_csv(file_path)
        
        # Apply data transformations
        transformed_data = transform_data(legacy_data)
        
        # Perform data migration to the cloud platform
        transformed_data.to_csv(os.path.join(cloud_platform_data_path, file_name), index=False)
        
        # Log successful migration for the specific file
        print(f"Data migration successful for {file_name}")
    else:
        # Log unsupported file format
        print(f"Ignoring {file_name}. Unsupported file format.")

# Migration completed
print("Data migration and transformation process completed.")
