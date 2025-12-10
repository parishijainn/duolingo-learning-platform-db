-- Created by Redgate Data Modeler (https://datamodeler.redgate-platform.com)
-- Last modification date: 2025-12-10 04:14:40.411

-- tables
-- Table: Account
CREATE TABLE Account (
    accountStatus text  NOT NULL,
    lastActiveDate date  NOT NULL,
    userID text  NOT NULL,
    CONSTRAINT Account_pk PRIMARY KEY (userID)
);

-- Table: Administrator
CREATE TABLE Administrator (
    userID text  NOT NULL,
    adminLevel text  NOT NULL,
    department text  NOT NULL,
    CONSTRAINT Administrator_pk PRIMARY KEY (userID)
);

-- Table: Course
CREATE TABLE Course (
    courseTitle text  NOT NULL,
    description text  NOT NULL,
    proficiencyLevel int  NOT NULL,
    CONSTRAINT Course_pk PRIMARY KEY (courseTitle)
);

-- Table: Exercise
CREATE TABLE Exercise (
    promptText text  NOT NULL,
    difficultyLevel int  NOT NULL,
    lessonTitle text  NOT NULL,
    CONSTRAINT Exercise_pk PRIMARY KEY (promptText)
);

-- Table: Goal
CREATE TABLE Goal (
    goalType text  NOT NULL,
    targetDate date  NOT NULL,
    targetLanguage text  NOT NULL,
    weeklyTargetMinutes int  NOT NULL,
    userID text  NOT NULL,
    CONSTRAINT Goal_pk PRIMARY KEY (userID,targetDate)
);

-- Table: Instructor
CREATE TABLE Instructor (
    userID text  NOT NULL,
    institution text  NOT NULL,
    department text  NOT NULL,
    CONSTRAINT Instructor_pk PRIMARY KEY (userID)
);

-- Table: Leaderboard
CREATE TABLE Leaderboard (
    leaderboardID int  NOT NULL,
    startDate date  NOT NULL,
    endDate date  NOT NULL,
    tierName int  NOT NULL,
    CONSTRAINT Leaderboard_pk PRIMARY KEY (leaderboardID)
);

-- Table: Learner
CREATE TABLE Learner (
    currentStreak int  NOT NULL,
    lessonsCompleted int  NOT NULL,
    longestStreak int  NOT NULL,
    userID text  NOT NULL,
    CONSTRAINT Learner_pk PRIMARY KEY (userID)
);

-- Table: Lesson
CREATE TABLE Lesson (
    lessonTitle text  NOT NULL,
    difficulty int  NOT NULL,
    courseTitle text  NOT NULL,
    CONSTRAINT Lesson_pk PRIMARY KEY (lessonTitle)
);

-- Table: Messages
CREATE TABLE Messages (
    message text  NOT NULL,
    senderID text  NOT NULL,
    recieverID text  NOT NULL,
    CONSTRAINT Messages_pk PRIMARY KEY (message)
);

-- Table: Progress
CREATE TABLE Progress (
    userID text  NOT NULL,
    date date  NOT NULL,
    completionRate int  NOT NULL,
    lessonScore int  NOT NULL,
    lessonTitle text  NOT NULL,
    CONSTRAINT Progress_pk PRIMARY KEY (userID,date,lessonTitle)
);

-- Table: Ranking
CREATE TABLE Ranking (
    userID text  NOT NULL,
    rankNumber int  NOT NULL,
    leaderboardID int  NOT NULL,
    lessonsCompleted int  NOT NULL,
    CONSTRAINT Ranking_pk PRIMARY KEY (userID,leaderboardID)
);

-- Table: Report
CREATE TABLE Report (
    reportDate date  NOT NULL,
    progressSummary text  NOT NULL,
    LearnerID text  NOT NULL,
    InstructorID text  NOT NULL,
    CONSTRAINT Report_pk PRIMARY KEY (reportDate)
);

-- Table: Subscription
CREATE TABLE Subscription (
    planType text  NOT NULL,
    startDate date  NOT NULL,
    endDate date  NOT NULL,
    userID text  NOT NULL,
    subscriptionID int  NOT NULL,
    CONSTRAINT Subscription_pk PRIMARY KEY (subscriptionID)
);

-- Table: Users
CREATE TABLE Users (
    userID text  NOT NULL,
    region text  NOT NULL,
    name text  NOT NULL,
    email text  NOT NULL,
    joinDate date  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (userID)
);

-- Table: plannedstudysession
CREATE TABLE plannedstudysession (
    plannedDate date  NOT NULL,
    userID text  NOT NULL,
    lessonTitle text  NOT NULL,
    plannedMinutes int  NOT NULL,
    completionStatus text  NOT NULL,
    CONSTRAINT plannedstudysession_pk PRIMARY KEY (plannedDate,userID,lessonTitle)
);

-- foreign keys
-- Reference: Account_Users (table: Account)
ALTER TABLE Account ADD CONSTRAINT Account_Users
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Administrator_Users (table: Administrator)
ALTER TABLE Administrator ADD CONSTRAINT Administrator_Users
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Exercise_Lesson (table: Exercise)
ALTER TABLE Exercise ADD CONSTRAINT Exercise_Lesson
    FOREIGN KEY (lessonTitle)
    REFERENCES Lesson (lessonTitle)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Goal_Learner (table: Goal)
ALTER TABLE Goal ADD CONSTRAINT Goal_Learner
    FOREIGN KEY (userID)
    REFERENCES Learner (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Instructor_Users (table: Instructor)
ALTER TABLE Instructor ADD CONSTRAINT Instructor_Users
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Learner_Users (table: Learner)
ALTER TABLE Learner ADD CONSTRAINT Learner_Users
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Lesson_Course (table: Lesson)
ALTER TABLE Lesson ADD CONSTRAINT Lesson_Course
    FOREIGN KEY (courseTitle)
    REFERENCES Course (courseTitle)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_Users (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_Users
    FOREIGN KEY (senderID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_Users1 (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_Users1
    FOREIGN KEY (recieverID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: PlannedStudySession_Learner (table: plannedstudysession)
ALTER TABLE plannedstudysession ADD CONSTRAINT PlannedStudySession_Learner
    FOREIGN KEY (userID)
    REFERENCES Learner (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: PlannedStudySession_Lesson (table: plannedstudysession)
ALTER TABLE plannedstudysession ADD CONSTRAINT PlannedStudySession_Lesson
    FOREIGN KEY (lessonTitle)
    REFERENCES Lesson (lessonTitle)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Progress_Learner (table: Progress)
ALTER TABLE Progress ADD CONSTRAINT Progress_Learner
    FOREIGN KEY (userID)
    REFERENCES Learner (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Progress_Lesson (table: Progress)
ALTER TABLE Progress ADD CONSTRAINT Progress_Lesson
    FOREIGN KEY (lessonTitle)
    REFERENCES Lesson (lessonTitle)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Ranking_Leaderboard (table: Ranking)
ALTER TABLE Ranking ADD CONSTRAINT Ranking_Leaderboard
    FOREIGN KEY (leaderboardID)
    REFERENCES Leaderboard (leaderboardID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Ranking_Learner (table: Ranking)
ALTER TABLE Ranking ADD CONSTRAINT Ranking_Learner
    FOREIGN KEY (userID)
    REFERENCES Learner (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Report_Instructor (table: Report)
ALTER TABLE Report ADD CONSTRAINT Report_Instructor
    FOREIGN KEY (InstructorID)
    REFERENCES Instructor (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Report_Learner (table: Report)
ALTER TABLE Report ADD CONSTRAINT Report_Learner
    FOREIGN KEY (LearnerID)
    REFERENCES Learner (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Subscription_Users (table: Subscription)
ALTER TABLE Subscription ADD CONSTRAINT Subscription_Users
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

