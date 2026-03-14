# Python-Students-Audit-Automated-Reporting
I noticed that identifying students for intervention took up valuable planning time. I applied my technical literacy in Python to automate this workflow, ensuring no student's progress is overlooked due to manual oversight.

# Features
- **Automated Flagging:** Instantly identifies students with grades below 60%.
- **Data Standardisation:** Cleans and processes CSV data automatically.
- **Scalability:** Handles any number of students (tested with 19+ records).

# How it Works
The script `student_audit.py` reads data from `student_data.csv` and generates a final `student_audit_report.csv` with a status column for each student.
