import mysql.connector

# Create a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shahnawaz@12345",
    database="superset"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()


class SuperAdmin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        # Execute SQL query to validate SuperAdmin credentials
        query = "SELECT * FROM superadmins WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def create_admin(self, admin_username, admin_password):
        # Create a new Admin account
        admin = Admin(admin_username, admin_password)

        # Execute SQL query to insert Admin into the database
        query = "INSERT INTO admins (username, password) VALUES (%s, %s)"
        cursor.execute(query, (admin.username, admin.password))
        db.commit()

        return admin

    def delete_admin(self, admin):
        # Delete an Admin account
        # Implement the logic to remove the admin account from the system

        # Execute SQL query to delete Admin from the database
        query = "DELETE FROM admins WHERE username = %s"
        cursor.execute(query, (admin.username,))
        db.commit()

    def update_admin(self, admin, new_name, new_email):
        # Update Admin account details
        admin.update_details(new_name, new_email)

        # Execute SQL query to update Admin in the database
        query = "UPDATE admins SET name = %s, email = %s WHERE username = %s"
        cursor.execute(query, (admin.name, admin.email, admin.username))
        db.commit()

    def get_company_details(self, company):
        # Access the details of any company
        return company.get_details()


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        # Execute SQL query to validate Admin credentials
        query = "SELECT * FROM admins WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def create_company(self, name, address):
        # Create a new company
        company = Company(name, address)

        # Execute SQL query to insert Company into the database
        query = "INSERT INTO companies (name, address) VALUES (%s, %s)"
        cursor.execute(query, (company.name, company.address))
        db.commit()

        return company

    def delete_company(self, company):
        # Delete an existing company
        # Implement the logic to remove the company from the system

        # Execute SQL query to delete Company from the database
        query = "DELETE FROM companies WHERE name = %s"
        cursor.execute(query, (company.name,))
        db.commit()

    def update_company(self, company, new_name, new_address):
        # Update company information
        company.update_details(new_name, new_address)

        # Execute SQL query to update Company in the database
        query = "UPDATE companies SET name = %s, address = %s WHERE name = %s"
        cursor.execute(query, (company.name, company.address, company.name))
        db.commit()

    def get_company_details(self, company):
        # Access the details of the company the admin manages
        return company.get_details()


class Employee:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        # Execute SQL query to validate Employee credentials
        query = "SELECT * FROM employees WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def get_company_details(self, company):
        # Access the details of the company the employee belongs to
        return company.get_details()


class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def update_details(self, new_name, new_address):
        self.name = new_name
        self.address = new_address

    def get_details(self):
        return f"Name: {self.name}\nAddress: {self.address}"


# Usage example:

# Create SuperAdmin
superadmin = SuperAdmin("superadmin", "password123")

# Create Admin
admin = superadmin.create_admin("admin", "admin123")

# Create a company
company = admin.create_company("ABC Corp", "123 Main St")

# Update company details
admin.update_company(company, "XYZ Corp", "456 Elm St")

# Get company details
company_details = admin.get_company_details(company)
print(company_details)

# Access company details as an Employee/User
employee = Employee("user1", "user123")
employee_company_details = employee.get_company_details(company)
print(employee_company_details)

# Close the database connection
cursor.close()
db.close()