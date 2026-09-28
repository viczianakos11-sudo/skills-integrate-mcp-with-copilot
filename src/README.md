# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for and unregister students (teacher login required)
- View activities and participant rosters without logging in

## Teacher Access

Teacher passwords are hashed and stored locally in `teachers.json`, which is ignored by Git. From the `src` directory, create a teacher account with:

```
python create_teacher.py
```

The script prompts for a username and password and can be run again to add or replace an account. Keep `teachers.json` private and provision it separately on each deployment. The app does not provide a public account-management page.

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   uvicorn app:app --reload
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/auth/login`                                                     | Authenticate a teacher and create a session                         |
| POST   | `/auth/logout`                                                    | Revoke the current teacher session                                  |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister a student from an activity                               |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

Activities and login sessions are stored in memory and reset when the server restarts. Teacher password hashes are stored in the local `teachers.json` file.
