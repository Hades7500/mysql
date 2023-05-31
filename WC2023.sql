CREATE TABLE `Matches` (
    `MatchID` CHAR(4)  NOT NULL ,
    `Team A` VARCHAR(30)  NOT NULL ,
    `Team B` VARCHAR(30)  NOT NULL ,
    `Date` DATE  NOT NULL ,
    `Time` TIME  NOT NULL ,
    `Venue` VARCHAR(50)  NOT NULL ,
    `TossWinner` VARCHAR(30)  NOT NULL ,
    `Winner` VARCHAR(30)  NOT NULL ,
    `MVP` VARCHAR (30) NOT NULL ,
    PRIMARY KEY (
        `MatchID`
    )
) ENGINE = INNODB;

CREATE TABLE `Teams` (
    `TeamID` CHAR(4)  NOT NULL ,
    `TeamName` VARCHAR(30)  NOT NULL ,
    PRIMARY KEY (
        `TeamID`
    )
) ENGINE = INNODB;

CREATE TABLE `Players` (
    `PlayerID` CHAR(4)  NOT NULL ,
    `PlayerName` VARCHAR(30)  NOT NULL ,
    `Position` VARCHAR(15)  NOT NULL ,
    `MVP` INT(2) NOT NULL,
    `Runs` INT(4) NOT NULL,
    `Wickets` INT(2) NOT NULL,
    `TeamID` CHAR(4)  NOT NULL ,
    PRIMARY KEY (
        `PlayerID`
    )
) ENGINE = INNODB;

CREATE TABLE `TeamA_Score` (
    `MatchID` CHAR(4)  NOT NULL ,
    `Team A Score` VARCHAR(6)  NOT NULL ,
    `Team A Overs` FLOAT(2,1)  NOT NULL ,
    `Batting` VARCHAR(30) NOT NULL ,
    `R` INT(3) NOT NULL ,
    `B` INT(3) NOT NULL ,
    `4s` INT(2) NOT NULL ,
    `6s` INT(2) NOT NULL ,
    `SR` FLOAT(3,2) NOT NULL ,
    `Extras` VARCHAR(30) NOT NULL ,
    `Bowling` VARCHAR(30) NOT NULL ,
    `O` INT(3) NOT NULL ,
    `M` INT(3) NOT NULL ,
    `R` INT(3) NOT NULL ,
    `W` INT(3) NOT NULL ,
    `Econ` FLOAT(2,2) NOT NULL ,
) ENGINE = INNODB;

CREATE TABLE `TeamB_Score` (
    `MatchID` CHAR(4)  NOT NULL ,
    `Team B Score` VARCHAR(6)  NOT NULL ,
    `Team B Overs` FLOAT(2,1)  NOT NULL ,
    `Batting` VARCHAR(30) NOT NULL ,
    `R` INT(3) NOT NULL ,
    `B` INT(3) NOT NULL ,
    `4s` INT(2) NOT NULL ,
    `6s` INT(2) NOT NULL ,
    `SR` FLOAT(3,2) NOT NULL ,
    `Extras` VARCHAR(30) NOT NULL ,
    `Bowling` VARCHAR(30) NOT NULL ,
    `O` INT(3) NOT NULL ,
    `M` INT(3) NOT NULL ,
    `R` INT(3) NOT NULL ,
    `W` INT(3) NOT NULL ,
    `Econ` FLOAT(2,2) NOT NULL ,
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
    `PlayerID` CHAR(4)  NOT NULL 
) ENGINE = INNODB;

CREATE TABLE `Table` (
    `TeamID` CHAR(4)  NOT NULL ,
    `M` INT(2)  NOT NULL ,
    `W` INT(2)  NOT NULL ,
    `L` INT(2)  NOT NULL ,
    `NRR` FLOAT(3,3)  NOT NULL ,
    `PTS` INT(2)  NOT NULL 
) ENGINE = INNODB;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Team A` FOREIGN KEY(`Team A`)
REFERENCES `Teams` (`TeamID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Team B` FOREIGN KEY(`Team B`)
REFERENCES `Teams` (`TeamID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TossWinner` FOREIGN KEY(`TossWinner`)
REFERENCES `Teams` (`TeamID`) ON DELETE CASCADE;

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Winner` FOREIGN KEY(`Winner`)
REFERENCES `Teams` (`TeamID`) ON DELETE CASCADE;

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TeamID` FOREIGN KEY(`TeamID`)
REFERENCES `Teams` (`TeamID`) ON DELETE CASCADE;

ALTER TABLE `Scoreboard` ADD CONSTRAINT `fk_Scoreboard_MatchID` FOREIGN KEY(`MatchID`)
REFERENCES `Matches` (`MatchID`) ON DELETE CASCADE;

ALTER TABLE `Scoreboard` ADD CONSTRAINT `fk_Scoreboard_MVP` FOREIGN KEY(`MVP`)
REFERENCES `Players` (`PlayerID`) ON DELETE CASCADE;

ALTER TABLE `Stats` ADD CONSTRAINT `fk_Stats_PlayerID` FOREIGN KEY(`PlayerID`)
REFERENCES `Players` (`PlayerID`) ON DELETE CASCADE;

ALTER TABLE `Table` ADD CONSTRAINT `fk_Table_TeamID` FOREIGN KEY(`TeamID`)
REFERENCES `Teams` (`TeamID`) ON DELETE CASCADE;

