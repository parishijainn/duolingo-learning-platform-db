DROP DATABASE IF EXISTS duolingo_project;
CREATE DATABASE duolingo_project;

\c duolingo_project

\i create.sql

\copy Users(userID, region, name, email, joinDate) FROM 'Users.csv' CSV HEADER;
\copy Learner(userID, currentStreak, lessonsCompleted, longestStreak) FROM 'Learner.csv' CSV HEADER;

\copy Course(courseTitle, description, proficiencyLevel) FROM 'Course.csv' CSV HEADER;
\copy Lesson(lessonTitle, difficulty, courseTitle) FROM 'Lesson.csv' CSV HEADER;

\copy Progress(userID, date, completionRate, lessonScore, lessonTitle) FROM 'Progress.csv' CSV HEADER;

\copy Leaderboard(leaderboardID, startDate, endDate, tierName) FROM 'Leaderboard.csv' CSV HEADER;
\copy Ranking(userID, leaderboardID, rankNumber, lessonsCompleted) FROM 'Ranking.csv' CSV HEADER;

\copy Subscription(subscriptionID, planType, startDate, endDate, userID) FROM 'Subscription.csv' CSV HEADER;

\copy plannedstudysession(plannedDate, userID, lessonTitle, plannedMinutes, completionStatus) FROM 'PlannedStudySession.csv' CSV HEADER;

\copy Messages(message, senderID, recieverID) FROM 'Messages.csv' CSV HEADER;

\copy Instructor(userID,institution, department) FROM 'Instructor.csv' CSV HEADER;

\copy Report(reportDate, progressSummary, LearnerID, InstructorID) FROM 'Report.csv' CSV HEADER;

