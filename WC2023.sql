-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/RYqJBP
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `Matches` (
    `MatchID` CHAR(4)  NOT NULL ,
    `Home Team` VARCHAR(30)  NOT NULL ,
    `Away Team` VARCHAR(30)  NOT NULL ,
    `Date` DATE  NOT NULL ,
    `Time` TIME  NOT NULL ,
    `Venue` VARCHAR(50)  NOT NULL ,
    `TossWinner` VARCHAR(30)  NOT NULL ,
    `Winner` VARCHAR(30)  NOT NULL ,
    PRIMARY KEY (
        `MatchID`
    )
);

CREATE TABLE `Teams` (
    `TeamID` CHAR(4)  NOT NULL ,
    `TeamName` VARCHAR(30)  NOT NULL ,
    PRIMARY KEY (
        `TeamID`
    )
);

CREATE TABLE `Players` (
    `PlayerID` CHAR(4)  NOT NULL ,
    `PlayerName` VARCHAR(30)  NOT NULL ,
    `Position` VARCHAR(15)  NOT NULL ,
    `TeamID` CHAR(4)  NOT NULL ,
    PRIMARY KEY (
        `PlayerID`
    )
);

CREATE TABLE `Scoreboard` (
    `MatchID` CHAR(4)  NOT NULL ,
    `Home Team Runs` INT(3)  NOT NULL ,
    `Home Team Wickets` INT(2)  NOT NULL ,
    `Home Team Overs` FLOAT(2,1)  NOT NULL ,
    `Away Team Runs` INT(3)  NOT NULL ,
    `Away Team Wickets` INT(2)  NOT NULL ,
    `Away Team Overs` FLOAT(2,1)  NOT NULL ,
    `MVP` CHAR(4)  NOT NULL 
);

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
);

CREATE TABLE `Table` (
    `TeamID` CHAR(4)  NOT NULL ,
    `M` INT(2)  NOT NULL ,
    `W` INT(2)  NOT NULL ,
    `L` INT(2)  NOT NULL ,
    `NRR` FLOAT(1,3)  NOT NULL ,
    `PTS` INT(2)  NOT NULL 
);

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Home Team` FOREIGN KEY(`Home Team`)
REFERENCES `Teams` (`TeamID`);

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Away Team` FOREIGN KEY(`Away Team`)
REFERENCES `Teams` (`TeamID`);

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_TossWinner` FOREIGN KEY(`TossWinner`)
REFERENCES `Teams` (`TeamID`);

ALTER TABLE `Matches` ADD CONSTRAINT `fk_Matches_Winner` FOREIGN KEY(`Winner`)
REFERENCES `Teams` (`TeamID`);

ALTER TABLE `Players` ADD CONSTRAINT `fk_Players_TeamID` FOREIGN KEY(`TeamID`)
REFERENCES `Teams` (`TeamID`);

ALTER TABLE `Scoreboard` ADD CONSTRAINT `fk_Scoreboard_MatchID` FOREIGN KEY(`MatchID`)
REFERENCES `Matches` (`MatchID`);

ALTER TABLE `Scoreboard` ADD CONSTRAINT `fk_Scoreboard_MVP` FOREIGN KEY(`MVP`)
REFERENCES `Players` (`PlayerID`);

ALTER TABLE `Stats` ADD CONSTRAINT `fk_Stats_PlayerID` FOREIGN KEY(`PlayerID`)
REFERENCES `Players` (`PlayerID`);

ALTER TABLE `Table` ADD CONSTRAINT `fk_Table_TeamID` FOREIGN KEY(`TeamID`)
REFERENCES `Teams` (`TeamID`);

