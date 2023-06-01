CREATE TABLE `Matches` (
    `MID` CHAR(4)  NOT NULL ,
    `TeamA_ID` VARCHAR(30)  NOT NULL ,
    `TeamB_ID` VARCHAR(30)  NOT NULL ,
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
    `MVP` INT(2) NOT NULL,
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

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Team A` FOREIGN KEY(`Team A`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Team B` FOREIGN KEY(`Team B`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TossWinner` FOREIGN KEY(`TossWinner`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Winner` FOREIGN KEY(`Winner`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

ALTER TABLE `Team A` ADD CONSTRAINT `fk_Team A_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `Team A` ADD CONSTRAINT `fk_Team A_MVP` FOREIGN KEY(`MVP`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `Team B` ADD CONSTRAINT `fk_TeamB_MID` FOREIGN KEY(`MID`)
REFERENCES `Matches` (`MID`) ON DELETE CASCADE;

ALTER TABLE `Team B` ADD CONSTRAINT `fk_TeamB_MVP` FOREIGN KEY(`MVP`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `Stats` ADD CONSTRAINT `fk_Stats_PlayerID` FOREIGN KEY(`PID`)
REFERENCES `Players` (`PID`) ON DELETE CASCADE;

ALTER TABLE `Table` ADD CONSTRAINT `fk_Table_TID` FOREIGN KEY(`TID`)
REFERENCES `Teams` (`TID`) ON DELETE CASCADE;

