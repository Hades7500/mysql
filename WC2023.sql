CREATE TABLE `Matches` (
    `MID` CHAR(4) NOT NULL,
    `TeamA_TID` CHAR(3) NOT NULL,
    `TeamB_TID` CHAR(3) NOT NULL,
    `TeamA_Score` INT(3) NOT NULL,
    `TeamA_Wickets` INT(2) NOT NULL,
    `TeamA_Extras` INT(3) NOT NULL,
    `TeamB_Score` INT(3) NOT NULL,
    `TeamB_Wickets` INT(2) NOT NULL,
    `TeamB_Extras` INT(3) NOT NULL,
    `WINNER_TID` CHAR(3) NOT NULL,
    `LOSER_TID` CHAR(3) NOT NULL,
    `MVP_PID` CHAR(3) NOT NULL,
    `Date` DATE NOT NULL,
    `Time` TIME NOT NULL,
    `Venue` VARCHAR(50) NOT NULL,
    `TeamA_Overs` FLOAT NOT NULL,
    `TeamB_Overs` FLOAT NOT NULL,
    PRIMARY KEY (
        `MID`
    )
) ENGINE = INNODB;

CREATE TABLE `Teams` (
    `TID` CHAR(3) NOT NULL,
    `TNAME` VARCHAR(30) NOT NULL,
    PRIMARY KEY (
        `TID`
    )
) ENGINE = INNODB;

CREATE TABLE `Players` (
    `PID` CHAR(4) NOT NULL,
    `PNAME` VARCHAR(30) NOT NULL,
    `POSITION` VARCHAR(30) NOT NULL,
    `RUNS` INT(4) NOT NULL,
    `WICKETS` INT(2) NOT NULL,
    `HUNDREDS` INT(2) NOT NULL,
    `FIFTIES` INT(2) NOT NULL,
    `FOURS` INT(3) NOT NULL,
    `SIXES` INT(3) NOT NULL,
    `HIGHEST_SCORE` INT(3) NOT NULL,
    `FIVE_WICKET_HAULS` INT(2) NOT NULL,
    `NO_OF_MVP` INT(2) NOT NULL,
    `TID` CHAR(3) NOT NULL,
    PRIMARY KEY (
        `PID`
    )
) ENGINE = INNODB;

CREATE TABLE `TeamA_Details` (
    `TID` CHAR(3)  NOT NULL,
    `MID` CHAR(4)  NOT NULL,
    `PID` CHAR(4)  NOT NULL,
    `Runs_Made` INT(3) NOT NULL,
    `Balls_Played` INT(3) NOT NULL,
    `Fours` INT(2) NOT NULL,
    `Sixes` INT(2) NOT NULL,
    `Strike_Rate` FLOAT(5,2) NOT NULL,
    `Overs_Bowled` INT(3) NOT NULL,
    `Maiden` INT(2) NOT NULL,
    `Runs_Conceded` INT(3) NOT NULL,
    `Wickets_Taken` INT(3) NOT NULL,
    `Economy` FLOAT(4,2)  NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `TeamB_Details` (
    `TID` CHAR(3) NOT NULL,
    `MID` CHAR(4) NOT NULL,
    `PID` CHAR(4) NOT NULL,
    `Runs_Made` INT(3) NOT NULL,
    `Balls_Played` INT(3) NOT NULL,
    `Fours` INT(2) NOT NULL,
    `Sixes` INT(2) NOT NULL,
    `Strike_Rate` FLOAT(5,2) NOT NULL,
    `Overs_Bowled` INT(3) NOT NULL,
    `Maiden` INT(2) NOT NULL,
    `Runs_Conceded` INT(3) NOT NULL,
    `Wickets_Taken` INT(3) NOT NULL,
    `Economy` FLOAT(4,2) NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `Points_Table` (
    `Matches` INT(2) NOT NULL,
    `Wins` INT(2) NOT NULL,
    `Losses` INT(2) NOT NULL,
    `Net_Run_Rate` FLOAT(5,3) NOT NULL,
    `Points` INT(2) NOT NULL,
    `TID` CHAR(3) NOT NULL 
) ENGINE = INNODB;

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams`(`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TeamA_TID` FOREIGN KEY(`TeamA_TID`)
REFERENCES `Teams`(`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TeamB_TID` FOREIGN KEY(`TeamB_TID`)
REFERENCES `Teams`(`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_LOSER_TID` FOREIGN KEY(`LOSER_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_WINNER_TID` FOREIGN KEY(`WINNER_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_MVP_PID` FOREIGN KEY(`MVP_PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Details` ADD CONSTRAINT `fk_TeamA_Details_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Details` ADD CONSTRAINT `fk_TeamA_Details_MID` FOREIGN KEY(`MID`)
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