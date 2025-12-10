\c duolingo_project

\echo '--- USERS ---'
SELECT * FROM Users ORDER BY userID;

\echo '--- LEARNER ---'
SELECT * FROM Learner ORDER BY userID;

\echo '--- LESSON ---'
SELECT * FROM Lesson ORDER BY lessonTitle;

\echo '--- PROGRESS ---'
SELECT * FROM Progress ORDER BY userID, date;

\echo '--- LEADERBOARD ---'
SELECT * FROM Leaderboard ORDER BY leaderboardID;

\echo '--- RANKING ---'
SELECT * FROM Ranking ORDER BY leaderboardID, rankNumber;

\echo '--- PlannedStudySession  ---'
SELECT * FROM plannedstudysession;

\echo '--- REPORT ---'
SELECT * FROM Report;

\echo '--- COURSE ---'
SELECT * FROM Course;

\echo '--- MESSAGES ---'
SELECT * FROM Messages;

\echo '--- INSTRUCTOR ---'
SELECT * FROM Instructor;

\echo '--- SUBSCRIPTION ---'
SELECT * FROM Subscription;
