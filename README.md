# Eval-Campus 🎓

A Student Feedback Evaluation System built with **PHP, MySQL, HTML, CSS, and JavaScript**. This project allows students to submit feedback on courses and instructors, while administrators can analyze and manage the feedback efficiently.

---

## 🚀 Features

### 👨‍🎓 Student

* Register and login
* Submit feedback for courses
* Rate instructors (1–5 scale)
* Leave comments
* Restriction: One feedback per course

### 👨‍💼 Admin

* Login dashboard
* View all feedback
* Filter by course or instructor
* View average ratings
* Manage users, courses, and instructors

### 👨‍🏫 Instructor (Optional)

* View feedback summary
* See ratings and comments

---

## 🧱 Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** PHP
* **Database:** MySQL
* **Charts (Optional):** Chart.js

---

## 📁 Project Structure

```
/eval-campus
│
├── /config          # Database configuration
├── /includes        # Reusable PHP components
├── /auth            # Login & registration
├── /student         # Student dashboard & feedback
├── /admin           # Admin dashboard
├── /instructor      # Instructor view (optional)
├── /assets
│   ├── /css
│   ├── /js
│   └── /images
├── index.php        # Landing page
└── README.md
```

---

## 🗃️ Database Schema

### Users Table

| Column   | Type                              |
| -------- | --------------------------------- |
| id       | INT (PK)                          |
| name     | VARCHAR                           |
| email    | VARCHAR                           |
| password | VARCHAR                           |
| role     | ENUM (student, admin, instructor) |

### Courses Table

| Column      | Type     |
| ----------- | -------- |
| id          | INT (PK) |
| course_name | VARCHAR  |

### Instructors Table

| Column | Type     |
| ------ | -------- |
| id     | INT (PK) |
| name   | VARCHAR  |

### Feedback Table

| Column        | Type      |
| ------------- | --------- |
| id            | INT (PK)  |
| student_id    | INT       |
| course_id     | INT       |
| instructor_id | INT       |
| rating        | INT       |
| comment       | TEXT      |
| created_at    | TIMESTAMP |

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/your-username/eval-campus.git
```

2. Move project to your server directory (e.g., XAMPP `htdocs`)

3. Create MySQL database:

```
CREATE DATABASE eval_campus;
```

4. Import database schema (create tables manually or via SQL file)

5. Configure database connection:

Edit `/config/db.php`

```php
<?php
$conn = new mysqli("localhost", "root", "", "eval_campus");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

6. Start Apache & MySQL (XAMPP/WAMP)

7. Open in browser:

```
http://localhost/eval-campus
```

---

## 🔐 Security Considerations

* Use `password_hash()` and `password_verify()`
* Validate and sanitize all inputs
* Use prepared statements (PDO or MySQLi)
* Protect routes using sessions

---

## 🧭 Development Roadmap

### Phase 1 (Core)

* [ ] Setup project structure
* [ ] Database connection
* [ ] Authentication system

### Phase 2 (Features)

* [ ] Feedback form
* [ ] Store feedback in DB
* [ ] Admin dashboard

### Phase 3 (Enhancements)

* [ ] Filtering & search
* [ ] Charts & analytics
* [ ] UI improvements

---

## 💡 Future Improvements

* REST API backend
* React frontend
* JWT authentication
* Sentiment analysis on feedback

---

## 📌 License

This project is open-source and free to use for educational purposes.

---

## ✨ Author

Your Name

---

## 📣 Contribution

Feel free to fork and improve this project.
