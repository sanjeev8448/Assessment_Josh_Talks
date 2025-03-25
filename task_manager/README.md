# Task Management API

##  Overview
This is a Django REST API for a **Task Management System**, allowing users to:
- Create tasks
- Assign tasks to users
- Retrieve tasks assigned to specific users

##  Project Structure
```
project-root/
│── task_manager/        # Django Project
│   ├── settings.py      # Django Settings
│   ├── urls.py          # Project-level URLs
│   ├── wsgi.py          # WSGI Configuration
│── tasks/               # Django App
│   ├── models.py        # Database Models
│   ├── views.py         # API Views
│   ├── serializers.py   # DRF Serializers
│   ├── urls.py          # App-level URLs
│   ├── admin.py         # Admin Panel Configuration
│── db.sqlite3           # Database
│── requirements.txt     # Dependencies
│── README.md            # Documentation File ✅
│── manage.py            # Django CLI Utility
```

---

## 🚀 Setup Instructions
### 1️ Clone the Repository
```bash
git clone https://github.com/sanjeev8448/Assessment_Josh_Talks.git
cd task_manager
```

### 2️ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️ Apply Database Migrations
```bash
python manage.py makemigrations tasks
python manage.py migrate
```

### 5️ Create a Superuser for Admin Access
```bash
python manage.py createsuperuser
```
Enter the following credentials:
- **Username:** `pathak`
- **Password:** `admin`

### 6️ Run the Server
```bash
python manage.py runserver
```

---

## 📡 API Endpoints

### **1️ Create a Task** (POST `/api/tasks/create/`)
#### URL:
```
http://127.0.0.1:8000/api/tasks/create/
```
#### Request Body:
```json
{
    "name": "Fix Login Issue",
    "description": "Resolve login failure",
    "task_type": "bug",
    "status": "pending",
    "assigned_users": [1, 2]
}
```
#### Response:
```json
{
    "id": 1,
    "name": "Fix Login Issue",
    "description": "Resolve login failure",
    "task_type": "bug",
    "status": "pending",
    "assigned_users": [1, 2],
    "created_at": "2025-03-25T12:00:00Z"
}
```

### **2️ Assign Task to Users** (POST `/api/tasks/{task_id}/assign/`)
#### URL:
```
http://127.0.0.1:8000/api/tasks/1/assign/
```
#### Request Body:
```json
{
    "assigned_users": [1, 2]
}
```
#### Response:
```json
{
    "message": "Task assigned successfully",
    "task_id": 1,
    "assigned_users": [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "mobile": "9876543210"
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "email": "jane@example.com",
            "mobile": "9876543211"
        }
    ]
}
```

### **3️ Get Tasks Assigned to a User** (GET `/api/users/{user_id}/tasks/`)
#### URL:
```
http://127.0.0.1:8000/api/users/1/tasks/
```
#### Response:
```json
[
    {
        "id": 1,
        "name": "Fix Login Issue",
        "description": "Resolve login failure",
        "task_type": "bug",
        "status": "pending",
        "created_at": "2025-03-25T12:00:00Z"
    }
]
```

---

##  Django Admin Panel
To access the **Django Admin Panel**, go to:
```
http://127.0.0.1:8000/admin/
```
### **Admin Credentials:**
- **Username:** `pathak`
- **Password:** `admin`

---

## Testing
1. **Postman**: Import API requests and test the endpoints.
2. **cURL**:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/users/1/tasks/
   ```
3. **Django Shell**:
   ```python
   from tasks.models import Task
   Task.objects.all()
   ```

---

##  Adding Users via Django Shell
Follow these step-by-step instructions to add users manually using Django shell:

### **Step 1: Open the Django Shell**
```bash
python manage.py shell
```

### **Step 2: Import the User Model**
```python
from tasks.models import User
```

### **Step 3: Create a New User**
```python
user = User.objects.create(name="John Doe", email="john@example.com", mobile="9876543210")
```

### **Step 4: Verify the Created User**
```python
User.objects.all().values('id', 'name', 'email', 'mobile')
```
This will return a list of users in the database:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "mobile": "9876543210"
    }
]
```

### **Step 5: Exit the Django Shell**
```python
exit()
```

---


