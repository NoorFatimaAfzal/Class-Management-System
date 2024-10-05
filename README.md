# School Class Management System

## Overview
This project is a school class management system implemented in Python, which allows users to manage students, classrooms, and user credentials. The system consists of three main classes: `User`, `Student`, and `Classroom`, enabling different roles (students, Class Representatives, and teachers) to perform various operations while ensuring data security and integrity.

## Features
- **User Management**: 
  - Create users with different roles (student, Class Representative, teacher).
  - Securely access user credentials based on user type.
  
- **Student Management**:
  - Add and remove students from classrooms.
  - Update student details, including subjects registered and marks.

- **Classroom Management**:
  - Manage classroom attributes and user roles.
  - Class Representatives can access and manage all students’ data, while students can only access their own information.

## Classes

### 1. User
Represents a user in the system.
- **Attributes**:
  - `name`: Name of the user.
  - `email`: Email address of the user.
  - `password`: Password for the user account.
  - `type`: Type of user (student, CR, teacher).
  
- **Methods**:
  - `get_credentials(requester)`: Retrieves user credentials based on the requester's role.
  - `set_credentials(name, email, password, type)`: Updates user credentials.

### 2. Classroom
Represents a classroom containing students and managing user roles.
- **Attributes**:
  - `teacher`: Teacher assigned to the classroom.
  - `CR`: Class Representative.
  - `students`: List of students in the classroom.
  
- **Methods**:
  - `add_student(student, requester_email)`: Adds a student to the classroom.
  - `remove_student(student, requester_email)`: Removes a student from the classroom.
  - `get_students(requester)`: Retrieves the list of students, based on the requester's role.

### 3. Student
- Represents a student with details about their registration, subjects, and marks (to be defined as per your requirements).

## Getting Started

### Prerequisites
- Python 3.x
- MySQL Connector library
- A MySQL server running (local or remote)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Model-Tuning.git
   cd Model-Tuning
