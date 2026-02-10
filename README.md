# Duolingo Learning Platform Database

A fully implemented relational database system modeling a Duolingo-style language learning platform. This project includes conceptual design, BCNF normalization, SQL schema implementation, CSV-based data ingestion, and Python scripts that interact with PostgreSQL to demonstrate operational and analytical functionality.

---

## Overview

This project demonstrates the complete lifecycle of relational database development, including design, implementation, and analysis. It models real-world platform functionality such as:

- Learner progress tracking  
- Courses, lessons, and exercises  
- Study planning and adherence evaluation  
- Messaging between users  
- Leaderboards and ranking systems  
- Instructor reporting  
- Subscription tracking and automated deactivation  

The system was developed as part of a database design course and showcases relational modeling, SQL programming, and Python–PostgreSQL integration.

---

## Features

### Relational schema

The database includes entities such as:

- **Users:** Learners, Instructors, Administrators  
- **Learning structure:** Courses, Lessons, Exercises  
- **Progress tracking:** Lesson completion and timestamps  
- **Planning:** Planned study sessions and adherence evaluation  
- **Competition:** Leaderboards and rankings  
- **Communication:** Messaging between users  
- **Subscriptions:** Automated deactivation using triggers  
- **Reporting:** Instructor performance and learner analytics  

All relations were derived from functional dependencies and normalized to **BCNF**. Foreign key constraints enforce referential integrity.

---

### SQL implementation

The repository includes:

- `create.sql` — database schema definitions and constraints  
- `initialize.sql` — database reset and automated CSV data loading  
- `show_all.sql` — script to inspect database contents  
- CSV files for all relations, enabling reproducible dataset initialization  

This ensures the database can be recreated consistently.

---

### Python user story implementations

Ten standalone Python scripts (using `psycopg2`) demonstrate real application functionality:

**Operational functionality**

- Track learner progress  
- Display leaderboards and rankings  
- Review individual learner progress  
- Messaging between users  

**Analytical functionality**

- Analyze learner engagement  
- Evaluate study plan adherence  
- Generate instructor reports  
- Analyze subscription growth trends  
- Regional engagement analysis  

Each script prints executed SQL queries and results for clarity and transparency.

---

## Tech stack

**Database:** PostgreSQL  
**Query language:** SQL  
**Programming language:** Python  
**Database integration:** psycopg2  
**Data ingestion:** CSV using PostgreSQL COPY  

---

## Repository structure

```
DuolingoDatabase/
├── create.sql
├── initialize.sql
├── show_all.sql
├── Users.csv
├── Learner.csv
├── Lesson.csv
├── Course.csv
├── Progress.csv
├── Ranking.csv
├── Leaderboard.csv
├── Messages.csv
├── PlannedStudySession.csv
├── Subscription.csv
├── Report.csv
├── python/
│   ├── us1-track-progress-simple-operational.py
│   ├── us2-analyze-progress-complex-analytical.py
│   ├── us3-show-leaderboard-complex-operational.py
│   ├── us4-evaluate-study-plan-complex-analytical.py
│   ├── us5-review-progress-complex-operational.py
│   ├── us6-generate-report-complex-analytical.py
│   ├── us7-message-students-simple-operational.py
│   ├── us8-analyze-regional-learner-engagement.py
│   ├── us9-view-subscription-growth.py
│   └── us10-deactivate-accounts.py
└── Project_Report.pdf
```

---

## Getting started

### 1. Create the database

Open PostgreSQL and create a new database:

```sql
CREATE DATABASE duolingo_platform;
```

---

### 2. Initialize the schema

Run the schema creation script:

```bash
psql -d duolingo_platform -f create.sql
```

---

### 3. Load data

Run the initialization script:

```bash
psql -d duolingo_platform -f initialize.sql
```

This loads all CSV data into the database.

---

### 4. Run Python scripts

Install psycopg2:

```bash
pip install psycopg2-binary
```

Run a user story script:

```bash
python python/us1-track-progress-simple-operational.py
```

Each script connects to PostgreSQL and demonstrates database functionality.

---

## Concepts demonstrated

This project demonstrates core database engineering concepts:

- Relational schema design  
- Functional dependency analysis  
- BCNF normalization  
- Referential integrity enforcement  
- SQL joins, aggregates, and analytical queries  
- Trigger and stored procedure implementation  
- CSV-based data ingestion  
- Python–PostgreSQL integration  

---

## Academic context

Developed as part of a university database design course to demonstrate full-stack relational database development from conceptual design to implementation and analytics.

---

## Author

Parishi Jain  
Carnegie Mellon University  

---
