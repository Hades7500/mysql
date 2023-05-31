CREATE TABLE `Teams` (
    `TID` char(4)  NOT NULL ,
    `TNAME` varchar(30)  NOT NULL ,
    PRIMARY KEY (
        `TID`
    )
) ENGINE = INNODB;

CREATE TABLE `Players` (
    `PID` char(4)  NOT NULL ,
    `PNAME` varchar(30)  NOT NULL ,
    `POSITION` varchar(30)  NOT NULL ,
    `MVP` int(2)  NOT NULL ,
    `RUNS` int(4)  NOT NULL ,
    `WICKETS` int(2)  NOT NULL ,
    `TID` char(4)  NOT NULL ,
    PRIMARY KEY (
        `PID`
    )
) ENGINE = INNODB;

CREATE TABLE `Matches` (
    `MID` CHAR(4)  NOT NULL ,
    `TeamA_ID` VARCHAR(30)  NOT NULL ,
    `TeamB_ID` VARCHAR(30)  NOT NULL ,
    `Date` DATE  NOT NULL ,
    `Time` TIME  NOT NULL ,
    `Venue` VARCHAR(50)  NOT NULL ,
    `TossWinner_TID` VARCHAR(30)  NOT NULL ,
    `Winner_TID` VARCHAR(30)  NOT NULL ,
    `MVP_PID` VARCHAR(30)  NOT NULL ,
    PRIMARY KEY (
        `MID`
    )
) ENGINE = INNODB;

CREATE TABLE `TeamA_Score` (
    `TeamA_Score` VARCHAR(6),  NOT NULL ,
    `TeamA_Overs` FLOAT(3,1),  NOT NULL ,
    `Batting` VARCHAR(30),  NOT NULL ,
    `batterA_Runs` INT(3),  NOT NULL ,
    `Balls` INT(3),  NOT NULL ,
    `Fours` INT(2),  NOT NULL ,
    `Sixes` INT(2),  NOT NULL ,
    `Strike_Rate` FLOAT(5,2),  NOT NULL ,
    `Extras` VARCHAR(30),  NOT NULL ,
    `Bowling` VARCHAR(30),  NOT NULL ,
    `Overs` INT(3),  NOT NULL ,
    `Maiden` INT(3),  NOT NULL ,
    `bowlerA_Runs` INT(3),  NOT NULL ,
    `Wickets` INT(3)  NOT NULL ,
    `Economy` FLOAT(4,2),  NOT NULL ,
    `MID` CHAR(4)  NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `TeamB_Score` (
    `TeamB_Score` VARCHAR(6),  NOT NULL ,
    `TeamB_Overs` FLOAT(3,1),  NOT NULL ,
    `Batting` VARCHAR(30),  NOT NULL ,
    `batterB_Runs` INT(3),  NOT NULL ,
    `Balls` INT(3),  NOT NULL ,
    `Fours` INT(2),  NOT NULL ,
    `Sixes` INT(2),  NOT NULL ,
    `Strike_Rate` FLOAT(5,2),  NOT NULL ,
    `Extras` VARCHAR(30),  NOT NULL ,
    `Bowling` VARCHAR(30),  NOT NULL ,
    `Overs` INT(3),  NOT NULL ,
    `Maiden` INT(3),  NOT NULL ,
    `bowlerB_Runs` INT(3),  NOT NULL ,
    `Wickets` INT(3)  NOT NULL ,
    `Economy` FLOAT(4,2),  NOT NULL ,
    `MID` CHAR(4)  NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `Stats` (
    `Runs` INT(4),  NOT NULL ,
    `Wickets` INT(2),  NOT NULL ,
    `Most_Hundreds` INT(2),  NOT NULL ,
    `Highest_Score` INT(3),  NOT NULL ,
    `Most_Fifties` INT(2),  NOT NULL ,
    `Sixes` INT(3),  NOT NULL ,
    `Fours` INT(3),  NOT NULL ,
    `Five_Wicket_Haul` INT(3),  NOT NULL ,
    `PID` CHAR(4)  NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `Points_Table` (
    `Matches` INT(2),  NOT NULL ,
    `Wins` INT(2),  NOT NULL ,
    `Losses` INT(2),  NOT NULL ,
    `Net_Run_Rate` FLOAT(5,3),  NOT NULL ,
    `Points` INT(2)  NOT NULL ,
    `TID` CHAR(4)  NOT NULL 
) ENGINE = INNODB;

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_MVP_PID` FOREIGN KEY(`MVP_PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Score` ADD CONSTRAINT `fk_TeamA_Score_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `TeamB_Score` ADD CONSTRAINT `fk_TeamB_Score_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `Stats` ADD CONSTRAINT `fk_Stats_PID` FOREIGN KEY(`PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `Points_Table` ADD CONSTRAINT `fk_Points_Table_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

