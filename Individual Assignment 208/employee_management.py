import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_management"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the employee addition and database saving
def add_employee():
    employee_id = int(entry_id.get())
    name = entry_name.get()
    department = department_var.get()
    job_title = job_title_var.get()
    experience_years = int(entry_experience.get())
    monthly_salary = float(entry_salary.get())

    # Calculate annual salary
    annual_salary = monthly_salary * 12

    # Calculate total earnings based on experience years
    total_earnings = experience_years * annual_salary

    # To insert your Data into your database
    sql = "INSERT INTO `employees` (Employee_ID, Employee_Name, Employee_Department, Job_Title, Experience_Years, Monthly_Salary, Annual_Salary, Total_Earnings) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (employee_id, name, department, job_title, experience_years, monthly_salary, annual_salary, total_earnings)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output.
    output_text = (
        f"Employee ID: {employee_id}\n"
        f"Name: {name}\n"
        f"Department: {department}\n"
        f"Job Title: {job_title}\n"
        f"Experience Years: {experience_years}\n"
        f"Monthly Salary: RM{monthly_salary}\n"
        f"Annual Salary: RM{annual_salary}\n"
        f"Total Earnings: RM{total_earnings}"
    )

    output_label.config(text=output_text, foreground="blue", font=('Arial', 12, 'bold'))

# Function to update job titles based on the selected department
def update_job_titles(*args):
    selected_department = department_var.get()
    job_title_dropdown['values'] = job_titles.get(selected_department, [])

# Main window
root = tk.Tk()
root.title("Employee Management System")
root.geometry('600x700')
root.configure(bg='#FFECB3')  # Set background color

# Style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), foreground='#cc34ff')  # Set label color
style.configure('TButton', font=('Arial', 13))

# Page Title
title_label = ttk.Label(root, text='Add an Employee', style='TLabel', background='#cdf3ff')  # Set title background color
title_label.pack(pady=20)

# Employee ID Entry
id_label = ttk.Label(root, text="Employee ID:", background='#FFECB3')
id_label.pack()
entry_id = ttk.Entry(root)
entry_id.pack()

# Employee Name Entry
name_label = ttk.Label(root, text="Name:", background='#FFECB3')
name_label.pack()
entry_name = ttk.Entry(root)
entry_name.pack()

# Department Entry (Dropdown)
department_label = ttk.Label(root, text="Department:", background='#FFECB3')
department_label.pack()
departments = ["Executive", "Sales", "Marketing", "IT", "Operations", "Human Resources", "Finance"]
department_var = tk.StringVar(root)
department_var.set(departments[0])  # default value
department_var.trace_add('write', update_job_titles)  # update job titles when department changes
department_dropdown = ttk.Combobox(root, textvariable=department_var, values=departments, state='readonly')
department_dropdown.pack()

# Job Title Entry (Dropdown)
job_title_label = ttk.Label(root, text="Job Title:", background='#FFECB3')
job_title_label.pack()
job_titles = {'Executive': ['CEO', 'CFO', 'CIO', 'CMO', 'COO'],
              'Sales': ['Sales Manager', 'Sales Representative', 'Account Executive', 'Sales Analyst'],
              'Marketing': ['Marketing Manager', 'Marketing Coordinator', 'Social Media Specialist', 'SEO Specialist'],
              'IT': ['IT Manager', 'Systems Administrator', 'Network Engineer', 'Software Developer'],
              'Operations': ['Operations Manager', 'Project Manager', 'Business Analyst', 'Quality Assurance Manager'],
              'Human Resources': ['HR Manager', 'HR Generalist', 'Recruiter', 'Training and Development Manager'],
              'Finance': ['Finance Manager', 'Accountant', 'Financial Analyst', 'Payroll Specialist']}
job_title_var = tk.StringVar(root)
job_title_var.set(job_titles['Executive'][0])  # default value
job_title_dropdown = ttk.Combobox(root, textvariable=job_title_var, values=job_titles['Executive'], state='readonly')
job_title_dropdown.pack()

# Experience Entry
experience_label = ttk.Label(root, text="Experience (in years):", background='#FFECB3')
experience_label.pack()
entry_experience = ttk.Entry(root)
entry_experience.pack()

# Salary Entry
salary_label = ttk.Label(root, text="Monthly Salary:", background='#FFECB3')
salary_label.pack()
entry_salary = ttk.Entry(root)
entry_salary.pack()

# Save Button
save_button = ttk.Button(root, text="Add Employee", command=add_employee, style='TButton')
save_button.pack(pady=15)

# Output Label & result
output_label = ttk.Label(root, text="Employee Details", font=('Arial', 12, 'bold'), background='#cdf3ff', foreground='#cc34ff')
output_label.pack(pady=10)

root.mainloop()
