Duolingo Learning Platform Database

A fully implemented relational database system for a Duolingo-style learning platform.
This project includes conceptual and relational modeling, BCNF normalization, SQL schema creation, CSV-based data ingestion, and Python scripts that interact with PostgreSQL to demonstrate both operational and analytical functionality.

Overview

This repository contains the complete lifecycle of a database development project. It models real platform features such as:

Learner progress tracking

Courses, lessons, and exercises

Study planning and adherence evaluation

Messaging between users

Leaderboards and ranking systems

Instructor reporting

Subscription tracking and automated deactivation

The project was developed for a database design course and demonstrates relational design, SQL programming, and Python-database integration.

Features
1. Relational Schema

The schema includes:

Users, Learners, Instructors, Administrators

Courses, Lessons, Exercises

Progress tracking across lessons and dates

Planned study sessions

Leaderboards and ranking

Messages

Subscriptions with automated deactivation trigger

Reports for instructors

All relations were derived from functional dependencies and normalized to BCNF.
Foreign key constraints enforce referential integrity.

2. SQL Implementation

This repository contains:

create.sql – table definitions and constraints

initialize.sql – automated database reset and CSV import

show_all.sql – script for inspecting database contents

CSV files for all relations, enabling reproducible dataset loading

3. Python User Story Implementations

Ten Python scripts (using psycopg2) demonstrate both operational and analytical tasks:

Tracking and analyzing learner progress

Displaying leaderboards and rankings

Evaluating planned study sessions

Generating instructor reports

Messaging functionality

Engagement analysis by region

Subscription growth analytics

Trigger-based subscription deactivation

Each script is standalone and prints executed SQL and results for clarity.

Repository Structure
/
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

Skills Demonstrated

Relational schema design

Functional dependency analysis

BCNF normalization

SQL schema creation and referential constraints

CSV and COPY-based data loading

Complex SQL (joins, aggregates, window functions)

Trigger and stored procedure development

Python–PostgreSQL integration
