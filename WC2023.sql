
CREATE TABLE `Teams` (
    `TID` char(4),  NOT NULL ,
    `TNAME` varchar(30)  NOT NULL ,
    PRIMARY KEY (
        `TID`
    )
);

CREATE TABLE `Players` (
    `PID` char(4),  NOT NULL ,
    `PNAME` varchar(30),  NOT NULL ,
    `POSITION` varchar(30),  NOT NULL ,
    `RUNS` int(4),  NOT NULL ,
    `WICKETS` int(2),  NOT NULL ,
    `HUNDREDS` int(2),  NOT NULL ,
    `FIFTIES` int(2),  NOT NULL ,
    `HIGHEST_SCORE` int(3),  NOT NULL ,
    `FIVE_WICKET_HAULS` int(2),  NOT NULL ,
    `NO_OF_MVP` int(2),  NOT NULL ,
    `TID` char(4)  NOT NULL ,
    PRIMARY KEY (
        `PID`
    )
);

CREATE TABLE `Matches` (
    `MID` CHAR(4),  NOT NULL ,
    `TeamA_TID` CHAR(4)  NOT NULL ,
    `TeamB_TID` CHAR(4)  NOT NULL ,
    `TeamA_Score` int(3),  NOT NULL ,
    `TeamB_Score` int(3),  NOT NULL ,
    `TeamA_Wickets` int(2),  NOT NULL ,
    `TeamB_Wickets` int(2),  NOT NULL ,
    `TeamA_Extras` int(3),  NOT NULL ,
    `TeamB_Extras` int(3),  NOT NULL ,
    `LOSER_TID` char(4)  NOT NULL ,
    `WINNER_TID` char(4)  NOT NULL ,
    `MVP_TID` char(4)  NOT NULL ,
    `Date` DATE,  NOT NULL ,
    `Time` TIME,  NOT NULL ,
    `Venue` VARCHAR(50),  NOT NULL ,
    `TeamA_Overs` float,  NOT NULL ,
    `TeamB_Overs` float,  NOT NULL ,
    PRIMARY KEY (
        `MID`
    )
);

CREATE TABLE `TeamA_Details` (
    `TID` CHAR(4)  NOT NULL ,
    `MID` CHAR(4)  NOT NULL ,
    `PID` CHAR(4)  NOT NULL ,
    `Runs_Made` int(3),  NOT NULL ,
    `Balls_Played` INT(3),  NOT NULL ,
    `Fours` INT(2),  NOT NULL ,
    `Sixes` INT(2),  NOT NULL ,
    `Strike_Rate` FLOAT(5,2),  NOT NULL ,
    `Overs_Bowled` INT(3),  NOT NULL ,
    `Maiden` INT(2),  NOT NULL ,
    `Runs_Conceded` int(3),  NOT NULL ,
    `Wickets_Taken` INT(3),  NOT NULL ,
    `Economy` FLOAT(4,2)  NOT NULL 
);

CREATE TABLE `TeamB_Details` (
    `TID` CHAR(4)  NOT NULL ,
    `MID` CHAR(4)  NOT NULL ,
    `PID` CHAR(4)  NOT NULL ,
    `Runs_Made` int(3),  NOT NULL ,
    `Balls_Played` INT(3),  NOT NULL ,
    `Fours` INT(2),  NOT NULL ,
    `Sixes` INT(2),  NOT NULL ,
    `Strike_Rate` FLOAT(5,2),  NOT NULL ,
    `Overs_Bowled` INT(3),  NOT NULL ,
    `Maiden` INT(2),  NOT NULL ,
    `Runs_Conceded` int(3),  NOT NULL ,
    `Wickets_Taken` INT(3),  NOT NULL ,
    `Economy` FLOAT(4,2)  NOT NULL 
);

CREATE TABLE `Points_Table` (
    `Matches` INT(2),  NOT NULL ,
    `Wins` INT(2),  NOT NULL ,
    `Losses` INT(2),  NOT NULL ,
    `Net_Run_Rate` FLOAT(5,3),  NOT NULL ,
    `Points` INT(2)  NOT NULL ,
    `TID` CHAR(4)  NOT NULL 
);

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TeamA_TID` FOREIGN KEY(`TeamA_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TeamB_TID` FOREIGN KEY(`TeamB_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_LOSER_TID` FOREIGN KEY(`LOSER_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_WINNER_TID` FOREIGN KEY(`WINNER_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_MVP_TID` FOREIGN KEY(`MVP_TID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Details` ADD CONSTRAINT `fk_TeamA_Details_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Details` ADD CONSTRAINT `fk_TeamA_Details_MID` FOREIGN KEY(`MID`)
    
ALTER TABLE `TeamA_Score` ADD CONSTRAINT `fk_TeamA_Score_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Details` ADD CONSTRAINT `fk_TeamA_Details_PID` FOREIGN KEY(`PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `TeamB_Details` ADD CONSTRAINT `fk_TeamB_Details_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `TeamB_Details` ADD CONSTRAINT `fk_TeamB_Details_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `TeamB_Details` ADD CONSTRAINT `fk_TeamB_Details_PID` FOREIGN KEY(`PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `Points_Table` ADD CONSTRAINT `fk_Points_Table_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

