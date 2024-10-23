
# Task Management API using Python, Django REST Framework
Task Management that allows users to register, log in, manage their tasks, and ensure security by restricting access to their own tasks.

# Features:
User Registration and Authentication:

Registration: Users can register by providing their email, first name, last name, phone number, address, and password (with confirmation) using `AbstractBaseUser`.

Login: Users can log in to obtain `JWT` access and refresh tokens.

Task Management:

Basic CRUD operations along with custom validation, permissions and authentication.

Filtering and Sorting:
- Tasks can be `filtered` by status and priority as well as can be `searched` by title.
- Tasks can be `sorted` by due date, priority, or creation date.

Pagination

Permissions:
- Authenticated Users can view and manage their own tasks.

## Installation

clone the repo

```bash
  git clone https://github.com/rohn21/task_management_api_drf.git
```

```bash
  cd task_management
```

## Usage/Examples
Database migration
```
python manage.py makemigrations

python manage.py migrate
```

To run the server
```
python manage.py runserver
```

For admin with required fields
```
python manage.py createsuperuser
```