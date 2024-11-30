# Gas Utility Service Management System

A Gas Utility Service Management System where users can submit service requests, track their status, and optionally upload attachments. Administrators can manage requests and update their status. The system provides a simple and intuitive interface for both customers and administrators.

## Features

- **User Authentication**: Users can register, log in, and view their service requests.
- **Create Service Request**: Users can submit service requests with descriptions and attachments (optional).
- **Admin Dashboard**: Admins can view all service requests, update their status, and manage the requests.
- **User Dashboard**: Users can view and track the status of their submitted requests.
- **File Upload**: Attach files to service requests.
- **Status Management**: Admins can update the status of requests (Pending, In Progress, Completed).

## Screenshots

Here are some screenshots of the application:

- **Home Page**  
![Home Page](../Assets/Screenshot%202024-11-30%20134336.png)


- **Admin & Login / Register Page**  
![Login Page](Assets\image.png)
![Login Page](Assets\login.png)

- **Dashboard Page**  
![Dashboard Page](https://link-to-your-screenshot-image.com/dashboard_page.png)

- **Create Service Request Page**  
![Create Request Page](https://link-to-your-screenshot-image.com/create_request_page.png)

- **Admin Dashboard**  
![Admin Dashboard](https://link-to-your-screenshot-image.com/admin_dashboard.png)

## Technologies Used

- **Django**: Backend framework for handling business logic and database operations.
- **SQLite**: Database used for development (can be replaced with PostgreSQL or MySQL in production).
- **HTML/CSS**: For rendering templates and styling the frontend.
- **Django Forms**: For handling user input and validation.
- **Django Messages**: For displaying success/error messages.

## Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/isha4700/Gas-Utility-Customer-Management-.git
cd service-request-management
```

### 2. Set Up Virtual Environment
- **Create a virtual environment to manage dependencies:**

```bash

python -m venv venv
```
- **Activate the virtual environment:**

On Windows:
```bash

venv\Scripts\activate
```
On macOS/Linux:

```bash

source venv/bin/activate
```
### 3. Install Dependencies
Install the required dependencies by running:

```bash

pip install -r requirements.txt
```
### 4. Apply Migrations
Run the following command to create the necessary database tables:

```bash

python manage.py migrate
```
### 5. Create a Superuser (Optional)
If you want to access the admin panel, create a superuser:

```bash

python manage.py createsuperuser
```
Follow the prompts to create the superuser account.

### 6. Run the Development Server
Start the Django development server:

```bash

python manage.py runserver
Visit http://127.0.0.1:8000/ 
```
in your browser to access the application.

### 7. Access the Admin Panel
```bash
To access the admin panel, visit http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created.
```
### Project Structure
```bash

service-request-management/
│
├── main/
│   ├── migrations/
│   ├── templates/
│   │   └── main/
│   │       ├── home.html
│   │       ├── register.html
│   │       ├── dashboard.html
│   │       ├── create_request.html
│   │       ├── admin_dashboard.html
│   │       ├── update_request_status.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py          # ServiceRequest form
│   ├── models.py         # ServiceRequest model
│   ├── urls.py           # URL routing
│   └── views.py          # Views handling business logic
│
├── db.sqlite3            # SQLite database file
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```
### Usage
User Registration and Login:
Users can register and log in using the built-in Django authentication system.

### Create Service Request:
After logging in, users can submit a service request by providing a description and an optional attachment (file upload).

### User Dashboard:
Users can view all their service requests and their current status (Pending, In Progress, Completed).

### Admin Dashboard:
Admin users (superusers) can view all service requests and update their status.

### Important URLs
Home Page: /
Register Page: /register/
User Dashboard: /dashboard/
Create Service Request: /create-request/
Admin Dashboard: /admin-dashboard/
Update Service Request Status: /update-status/<int:pk>/
### Dependencies
- **The project uses the following dependencies:**

Django: Web framework for developing the application.
SQLite: Default database used by Django.
Django Messages: For handling success/error messages.
To install all dependencies, ensure that requirements.txt is up to date:

### txt

Django==5.1.3

You can install them by running:

```bash

pip install -r requirements.txt
```
### Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes. If you find a bug or have a feature request, please open an issue.

### License
This project is open-source and available under the MIT License.
