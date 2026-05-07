# API Contract

## Authentication

### Obtain Token
- **POST** `/api/account/login`
  - Request: `{ "username": "string", "password": "string" }`
  - Response: `{ "refresh": "string", "access": "string" }`

### Refresh Token
- **POST** `/api/token/refresh/`
  - Request: `{ "refresh": "string" }`
  - Response: `{ "access": "string" }`


### Login

## Register




---

## Feedback

### List Feedbacks
- **GET** `/api/feedbacks/`
  - Response: `[{ ...feedback fields... }]`

### Create Feedback
- **POST** `/api/feedbacks/`
  - Request:
    - Named feedback: `{ "subject": "string", "description": "string", "image": "file or null", "category": "string", "target": "string", "anonymous": false }`
    - Anonymous feedback: `{ "subject": "string", "description": "string", "image": "file or null", "category": "string", "target": "string", "anonymous": true }`
  - Response: `{ ...created feedback... }`

### Feedback Details
- **GET** `/api/feedbacks/{id}/`
  - Response: `{ ...feedback fields... }`

### Update Feedback
- **PUT/PATCH** `/api/feedbacks/{id}/`
  - Request: `{ ...fields to update... }`
    - Only admin, department, or student_affairs can update the `status` field.
    - Example: `{ "status": "resolved" }`
  - Response: `{ ...updated feedback... }`

### Delete Feedback
- **DELETE** `/api/feedbacks/{id}/`
  - Response: `204 No Content`

---

## Notifications

### List Notifications
- **GET** `/api/notifications/`
  - Response: `[{ ...notification fields... }]`

### Create Notification
- **POST** `/api/notifications/`
  - Request: `{ "message": "string", "is_read": false }`
  - Response: `{ ...created notification... }`

### Notification Details
- **GET** `/api/notifications/{id}/`
  - Response: `{ ...notification fields... }`

### Update Notification
- **PUT/PATCH** `/api/notifications/{id}/`
  - Request: `{ ...fields to update... }`
  - Response: `{ ...updated notification... }`

### Delete Notification
- **DELETE** `/api/notifications/{id}/`
  - Response: `204 No Content`

---

## Departments

### List Departments
- **GET** `/api/departments/`
  - Response: `[{ ...department fields... }]`

### Create Department
- **POST** `/api/departments/`
  - Request: `{ "name": "string", "description": "string" }`
  - Response: `{ ...created department... }`

### Department Details
- **GET** `/api/departments/{id}/`
  - Response: `{ ...department fields... }`

### Update Department
- **PUT/PATCH** `/api/departments/{id}/`
  - Request: `{ ...fields to update... }`
  - Response: `{ ...updated department... }`

### Delete Department
- **DELETE** `/api/departments/{id}/`
  - Response: `204 No Content`

---

## User Management

### List Users (admin, department, student_affairs only)
- **GET** `/api/users/`
  - Optional query param: `?role=student|admin|department|student_affairs`
  - Response:
    ```json
    [
      {
        "id": 1,
        "username": "user1",
        "email": "user1@email.com",
        "role": "student",
        "user_id": "S12345"
      },
      ...
    ]
    ```
- **403 Forbidden** if not admin/department/student_affairs

---

## Common Response Fields
- All endpoints return standard DRF error responses for invalid requests.
- All endpoints require authentication except for department list/details.
