# Django Billing Software

A role-based Billing and Inventory Management System developed using Django, HTML, CSS, JavaScript, and MySQL.

This project provides authentication, customer management, order management, product/inventory management, and role-based access control. After successful login, users are redirected to different sections of the application based on their assigned role.

## Features

- User Signup
- User Login
- Django Authentication using authenticate()
- Role-based access control
- Customer management
- Product management
- Inventory management
- Order management
- Product creation and update forms
- MySQL database integration
- Django ORM
- Django migrations
- Responsive HTML/CSS interface
- Different pages based on user permissions

## Technology Stack

- Python - Backend programming
- Django - Web framework
- HTML5 - Frontend structure
- CSS3 - Frontend styling
- JavaScript - Client-side functionality
- MySQL - Database
- mysqlclient - MySQL database connector

# Installation and Setup

## 1. Download or Clone the Repository

Clone the repository:

    git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Move into the project directory:

    cd YOUR-REPOSITORY

Or download the repository as a ZIP file from GitHub, extract it, and open the project folder in VS Code.

## 2. Check Python Installation

    python --version

If required:

    python3 --version

## 3. Create a Virtual Environment

Windows:

    python -m venv venv

Activate:

    venv\Scripts\activate

PowerShell:

    .\venv\Scripts\Activate.ps1

macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

## 4. Upgrade pip

    python -m pip install --upgrade pip

## 5. Install Required Libraries

Install Django:

    pip install django

Install MySQL client:

    pip install mysqlclient

If the project contains requirements.txt:

    pip install -r requirements.txt

A basic requirements.txt can contain:

    Django
    mysqlclient

To generate requirements.txt:

    pip freeze > requirements.txt

# MySQL Database Setup

## 6. Start MySQL Server

Make sure MySQL Server is running.

You can use MySQL Workbench, MySQL Command Line, XAMPP, WAMP, or another MySQL environment.

## 7. Create the Database

Open MySQL Workbench or MySQL Command Line and run:

    CREATE DATABASE billing_db;

You can use another database name, but it must match the database name in settings.py.

## 8. Import the SQL Database

If the project contains an SQL file such as database.sql, import it into MySQL.

Example:

    mysql -u root -p billing_db < database.sql

Alternatively, open the SQL file in MySQL Workbench and execute it.

If Django migrations are being used to create the database tables, an SQL dump may not be required. Create the database first and use makemigrations and migrate.

# Configure MySQL in Django

## 9. Update settings.py

Open the Django project's settings.py and configure DATABASES:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'billing_db',
            'USER': 'root',
            'PASSWORD': 'YOUR_MYSQL_PASSWORD',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

Replace YOUR_MYSQL_PASSWORD with your local MySQL password.

Example:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'billing_db',
            'USER': 'root',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

Important: Do not upload your real MySQL password to a public GitHub repository. For production, use environment variables.

# Check Django Configuration

Run:

    python manage.py check

If everything is configured correctly, Django should report that no system check issues were identified.

# Django Migrations

## 10. Create Migrations

    python manage.py makemigrations

## 11. Apply Migrations

    python manage.py migrate

These commands create/update the database tables required by the Django models.

# Create Django Superuser

If Django Admin is enabled:

    python manage.py createsuperuser

Enter the requested username, email address, and password.

After starting the server, open:

    http://127.0.0.1:8000/admin/

# Run the Project

## 12. Start the Development Server

    python manage.py runserver

Open:

    http://127.0.0.1:8000/

If port 8000 is already in use:

    python manage.py runserver 8001

Then open:

    http://127.0.0.1:8001/

# Authentication

The application uses Django authentication to validate user credentials.

The login flow is:

    User enters username and password
                    |
                    v
              authenticate()
                    |
                    v
          Check credentials
                    |
              +-----+-----+
              |           |
           Invalid       Valid
              |           |
              v           v
        Login Error   Check User Role
                           |
                           v
                    Role-based Redirect

The authentication uses Django's authenticate() and login() functions.

# Role-Based Permissions

The application uses the user's role value to determine which section of the billing system they can access.

Current role configuration:

    Role 0 -> Customer Table
    Role 1 -> Product/Inventory Table
    Role 2 -> Orders

## Role 0 - Customer Management

If:

    user.role == 0

the user is redirected to:

    /order/customer_table/

This section is used for customer-related operations.

Possible operations:

- View customers
- Add customers
- Update customers
- Delete customers
- View customer information

## Role 1 - Inventory/Product Management

If:

    user.role == 1

the user is redirected to:

    /inventory/products_table/

This section is used for inventory and product management.

Possible operations:

- View products
- Add products
- Update products
- Delete products
- Manage product information
- Manage inventory

## Role 2 - Order Management

If:

    user.role == 2

the user is redirected to:

    /order/orders/

This section is used for order and billing management.

Possible operations:

- View orders
- Create orders
- Manage customer orders
- View order details
- Process billing information

# Role-Based Redirect Code

The implemented role-based redirect logic is:

    if user.role == 0:
        return redirect('/order/customer_table/')

    elif user.role == 1:
        return redirect('/inventory/products_table/')

    elif user.role == 2:
        return redirect('/order/orders/')

# Example Authentication Code

A simplified login view can look like:

    from django.contrib.auth import authenticate, login
    from django.shortcuts import render, redirect

    def login_view(request):

        if request.method == "POST":

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                if user.role == 0:
                    return redirect('/order/customer_table/')

                elif user.role == 1:
                    return redirect('/inventory/products_table/')

                elif user.role == 2:
                    return redirect('/order/orders/')

            else:
                return render(
                    request,
                    'login.html',
                    {'error': 'Invalid username or password'}
                )

        return render(request, 'login.html')

Adapt this example to the project's actual custom user model, URL configuration, templates, and authentication implementation.

# Application Pages

## 1. Login Page

The login page allows users to enter their username and password.

After successful authentication, the system checks the user's role and redirects them to the appropriate section.

For GitHub README, add:


## 2. Signup Page

The signup page allows new users to create an account.

Typical fields include:

- Username
- Password
- Password confirmation
- Role
- Other required user information

For GitHub README, add:

## 3. Customer Management Page

The customer page is used to view and manage customer information.

Possible operations include:

- Add customer
- View customer
- Update customer
- Delete customer

For GitHub README, add:




## 4. Orders Page

The orders page is used to manage customer orders and billing information.

Possible information includes:

- Customer
- Product
- Quantity
- Price
- Total
- Order details
- Order status

For GitHub README, add:



## 5. Product List Page

The product list page displays products available in the inventory.

Typical information includes:

- Product ID
- Product name
- Price
- Quantity
- Category
- Product actions

For GitHub README, add:


## 6. Product Form Page

The product form is used to add or update products.

Typical fields include:

- Product name
- Price
- Quantity
- Category
- Other product information

For GitHub README, add:

    <img width="1278" height="666" alt="image" src="https://github.com/user-attachments/assets/79f801c8-ef3c-4ae4-ab64-7fc36c536743" />


# Application Workflow

    Login Page
         |
         v
    authenticate()
         |
         v
    Check User Role
         |
    +----+----+----+
    |         |    |
    v         v    v
  Role 0    Role 1 Role 2
    |         |    |
    v         v    v
 Customer  Products Orders
  Table     Table   Page
    |         |    |
    v         v    v
Customers Inventory Orders
Management Management Management

# Project Structure

A typical project structure can look like:

    django-billing-software/
    |
    +-- manage.py
    +-- requirements.txt
    |
    +-- project_name/
    |   +-- settings.py
    |   +-- urls.py
    |   +-- wsgi.py
    |   +-- asgi.py
    |
    +-- order/
    |   +-- models.py
    |   +-- views.py
    |   +-- urls.py
    |
    +-- inventory/
    |   +-- models.py
    |   +-- views.py
    |   +-- urls.py
    |
    +-- templates/
    |
    +-- static/
    
Exact folder names may differ depending on the project implementation.

# Common Django Commands

Create virtual environment:

    python -m venv .venv

Activate virtual environment on Windows:

    .venv\Scripts\activate

Install Django:

    pip install django

Install MySQL client:

    pip install mysqlclient
Install Pillows to add images:

     pip install pillow

Create migrations:

    python manage.py makemigrations

Apply migrations:

    python manage.py migrate

Create superuser:

    python manage.py createsuperuser

Run server:

    python manage.py runserver

Run on another port:

    python manage.py runserver 8001

# Troubleshooting

## Django is not installed

If you receive:

    ModuleNotFoundError: No module named 'django'

activate the virtual environment:

    venv\Scripts\activate

Then install Django:

    pip install django

## MySQLdb Module Error

If you receive:

    ModuleNotFoundError: No module named 'MySQLdb'

install:

    pip install mysqlclient

## MySQL Access Denied

If you receive an error similar to:

    Access denied for user

check the MySQL username and password in settings.py:

    'NAME': 'billing_db',
    'USER': 'root',
    'PASSWORD': 'YOUR_MYSQL_PASSWORD',
    'HOST': 'localhost',
    'PORT': '3306',

Make sure MySQL is running.

## Unknown Database

If you receive:

    Unknown database 'billing_db'

create the database:

    CREATE DATABASE billing_db;

Then make sure the same name is configured in settings.py.

## Table Does Not Exist

If you receive a table-does-not-exist error, run:

    python manage.py makemigrations
    python manage.py migrate

## Port Already in Use

Run Django on another port:

    python manage.py runserver 8001

Then open:

    http://127.0.0.1:8001/

# Security Notes

Before deploying this project publicly:

- Do not commit passwords to GitHub.
- Do not expose the production SECRET_KEY.
- Set DEBUG = False in production.
- Configure ALLOWED_HOSTS.
- Use environment variables for database credentials and secret keys.
- Use HTTPS in production.
- Validate user permissions on the server side.
- Do not rely only on hiding frontend links/buttons for authorization.
- Use Django authentication and authorization for protected views.
- Never store user passwords as plain text.

# Future Improvements

Possible improvements include:

- Invoice generation
- PDF bill generation
- Printable invoices
- Payment gateway integration
- Sales dashboard
- Sales analytics
- Stock alerts
- Low-stock notifications
- Product search
- Customer search
- Order filtering
- Pagination
- CSV/Excel export
- Customer purchase history
- Product categories
- User permission groups
- REST API integration
- Email notifications
- WhatsApp notifications
- Cloud deployment

# Production Deployment

For production deployment, the project can be deployed using services such as:

- AWS
- Render
- Railway
- PythonAnywhere
- DigitalOcean
- Other Django-compatible hosting providers

For production:

    DEBUG = False

Use a secure SECRET_KEY.

Configure:

    ALLOWED_HOSTS

Use environment variables for sensitive credentials.

Use HTTPS and a production WSGI/ASGI server.

# Quick Start

    # Clone repository
    git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

    # Open project
    cd YOUR-REPOSITORY

    # Create virtual environment
    python -m venv venv

    # Activate virtual environment
    venv\Scripts\activate

    # Upgrade pip
    python -m pip install --upgrade pip

    # Install dependencies
    pip install -r requirements.txt

    # Configure MySQL database in settings.py

    # Check Django
    python manage.py check

    # Create migrations
    python manage.py makemigrations

    # Apply migrations
    python manage.py migrate

    # Create admin user if required
    python manage.py createsuperuser

    # Start server
    python manage.py runserver

Open:

    http://127.0.0.1:8000/

# Role Permission Summary

    Role 0 -> /order/customer_table/ -> Customer Management
    Role 1 -> /inventory/products_table/ -> Product/Inventory Management
    Role 2 -> /order/orders/ -> Order Management

# Author

Kishore

Technologies:
Python | Django | HTML | CSS | MySQL

# License

This project is developed for educational, portfolio, and software development purposes.

Add an appropriate open-source license if you plan to distribute the project publicly.
