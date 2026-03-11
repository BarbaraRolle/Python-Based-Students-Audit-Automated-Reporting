import pandas as pd
import numpy as np
import os

#  Check if the file exists first (prevents crashing)
file_name = 'student_data.csv'

if os.path.exists(file_name):
    #  Load data
    df = pd.read_csv(file_name)
    
    #  Clean headers 
    df.columns = df.columns.str.strip()
    
    #  Standard 60% pass mark
    df['Status'] = np.where(df['Grade'] < 60, "NEEDS SUPPORT", "ON TRACK")
    
    print("\n--- STUDENT PROGRESS AUDIT SUCCESSFUL ---")
    print(df[['Name', 'Grade', 'Status']].to_string(index=False))
    
    
    df.to_csv('student_audit_report.csv', index=False)
else:
    print(f"Error: {file_name} not found in this folder.")
