class SuperAdmin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def create_admin(self, admin_username, admin_password):
        # Create a new Admin account
        admin = Admin(admin_username, admin_password)
        return admin

    def delete_admin(self, admin):
        # Delete an Admin account
        # Implement the logic to remove the admin account from the system
        pass

    def update_admin(self, admin, new_name, new_email):
        # Update Admin account details
        admin.update_details(new_name, new_email)

    def get_company_details(self, company):
        # Access the details of any company
        return company.get_details()


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def create_company(self, name, address):
        # Create a new company
        company = Company(name, address)
        return company

    def delete_company(self, company):
        # Delete an existing company
        # Implement the logic to remove the company from the system
        pass

    def update_company(self, company, new_name, new_address):
        # Update company information
        company.update_details(new_name, new_address)

    def get_company_details(self, company):
        # Access the details of the company the admin manages
        return company.get_details()


class Employee:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
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