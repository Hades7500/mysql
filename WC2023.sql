CREATE TABLE `Matches` (
    `MID` CHAR(4)  NOT NULL ,
    `TeamA_TID` VARCHAR(30)  NOT NULL ,
    `TeamB_TID` VARCHAR(30)  NOT NULL ,
    `Date` DATE  NOT NULL ,
    `Time` TIME  NOT NULL ,
    `Venue` VARCHAR(50)  NOT NULL ,
    `TossWinner_TID` VARCHAR(30)  NOT NULL ,
    `Winner_TID` VARCHAR(30)  NOT NULL ,
    `MVP_PID` VARCHAR (30) NOT NULL ,
    PRIMARY KEY (
        `MID`
    )
) ENGINE = INNODB;

CREATE TABLE `Teams` (
    `TID` CHAR(4)  NOT NULL ,
    `TName` VARCHAR(30)  NOT NULL ,
    PRIMARY KEY (
        `TID`
    )
) ENGINE = INNODB;

CREATE TABLE `Players` (
    `PID` CHAR(4)  NOT NULL ,
    `PName` VARCHAR(30)  NOT NULL ,
    `Position` VARCHAR(15)  NOT NULL ,
    `NO_of_MVP` INT(2) NOT NULL DEFAULT 0,
    `Runs` INT(4) NOT NULL,
    `Wickets` INT(2) NOT NULL,
    `TID` CHAR(4)  NOT NULL ,
    PRIMARY KEY (
        `PID`
    )
) ENGINE = INNODB;

CREATE TABLE `TeamA_Score` (
    `MID` CHAR(4)  NOT NULL ,
    `Team A Score` VARCHAR(6)  NOT NULL ,
    `Team A Overs` FLOAT(3,1)  NOT NULL ,
    `Batting` VARCHAR(30) NOT NULL ,
    `BatterA_Runs` INT(3) NOT NULL ,
    `Balls` INT(3) NOT NULL ,
    `Fours` INT(2) NOT NULL ,
    `Sixes` INT(2) NOT NULL ,
    `Strike_Rate` FLOAT(5,2) NOT NULL ,
    `Extras` VARCHAR(30) NOT NULL ,
    `Bowling` VARCHAR(30) NOT NULL ,
    `Overs` INT(3) NOT NULL ,
    `Maiden` INT(3) NOT NULL ,
    `BowlerA_Runs` INT(3) NOT NULL ,
    `Wickets` INT(3) NOT NULL ,
    `Economy` FLOAT(4,2) NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `TeamB_Score` (
    `MID` CHAR(4)  NOT NULL ,
    `Team B Score` VARCHAR(6)  NOT NULL ,
    `Team B Overs` FLOAT(3,1)  NOT NULL ,
    `Batting` VARCHAR(30) NOT NULL ,
    `BatterB_Runs` INT(3) NOT NULL ,
    `Balls` INT(3) NOT NULL ,
    `Fours` INT(2) NOT NULL ,
    `Sixes` INT(2) NOT NULL ,
    `Strike_Rate` FLOAT(5,2) NOT NULL ,
    `Extras` VARCHAR(30) NOT NULL ,
    `Bowling` VARCHAR(30) NOT NULL ,
    `Overs` INT(3) NOT NULL ,
    `Maiden` INT(3) NOT NULL ,
    `BowlerB_Runs` INT(3) NOT NULL ,
    `Wickets` INT(3) NOT NULL ,
    `Economy` FLOAT(4,2) NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `Stats` (
    `Runs` INT(4)  NOT NULL ,
    `Wickets` INT(2)  NOT NULL ,
    `Most Hundreds` INT(2)  NOT NULL ,
    `Highest Score` INT(3)  NOT NULL ,
    `Most Fifties` INT(2)  NOT NULL ,
    `Sixes` INT(3)  NOT NULL ,
    `Fours` INT(3)  NOT NULL ,
    `Five Wicket Haul` INT(3)  NOT NULL ,
    `PID` CHAR(4)  NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `Points_Table` (
        `TID` CHAR(4)  NOT NULL ,
        `Matches` INT(2)  NOT NULL ,
        `Wins` INT(2)  NOT NULL ,
        `Losses` INT(2)  NOT NULL ,
        `Net Run-Rate` FLOAT(5,3)  NOT NULL ,
        `Points` INT(2)  NOT NULL 
) ENGINE = INNODB;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TeamA_TID` FOREIGN KEY(`TeamA_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TeamB_TID` FOREIGN KEY(`TeamB_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TossWinner_TID` FOREIGN KEY(`TossWinner_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Winner_TID` FOREIGN KEY(`Winner_TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `TeamA_Score` ADD CONSTRAINT `fk_TeamA_Score_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `TeamB_Score` ADD CONSTRAINT `fk_TeamB_Score_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `Stats` ADD CONSTRAINT `fk_Stats_PlayerID` FOREIGN KEY(`PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `Points_Table` ADD CONSTRAINT `fk_Table_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

