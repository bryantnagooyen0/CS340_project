DELIMITER //

USE `cs340_nguyeb25`;

CREATE PROCEDURE reset_database()
BEGIN
    SET FOREIGN_KEY_CHECKS = 0;


    -- Creates Genres table structure
    CREATE OR REPLACE TABLE Genres(
    genre_id int AUTO_INCREMENT NOT NULL,
    genre_name varchar(50) NOT NULL UNIQUE,
    PRIMARY KEY (genre_id)
    );

    -- Creates Developers table structure
    CREATE OR REPLACE TABLE Developers(
    developer_id int AUTO_INCREMENT NOT NULL,
    developer_name varchar(100) NOT NULL UNIQUE,
    PRIMARY KEY (developer_id)
    );


    -- Creates Games table structure
    CREATE OR REPLACE TABLE Games(
    game_id int AUTO_INCREMENT NOT NULL,
    game_title varchar(100) NOT NULL UNIQUE,
    genre_id int,
    sales_count int NOT NULL,
    release_date date NOT NULL,
    developer_id int,
    PRIMARY KEY (game_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
    ON DELETE SET NULL,
    FOREIGN KEY (developer_id) REFERENCES Developers(developer_id)
    ON DELETE CASCADE
    );

    -- Create Reviewers table structure
    CREATE OR REPLACE TABLE Reviewers(
    reviewer_id int AUTO_INCREMENT NOT NULL,
    reviewer_company varchar(100) NOT NULL UNIQUE,
    PRIMARY KEY (reviewer_id)
    );

    -- Create Reviewers table structure
    CREATE OR REPLACE TABLE Reviews(
    review_id int AUTO_INCREMENT NOT NULL,
    game_id int NOT NULL,
    reviewer_id int NOT NULL,
    rating int(10) NOT NULL,
    comment TEXT,
    review_date date NOT NULL,
    PRIMARY KEY (review_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
    ON DELETE CASCADE,
    FOREIGN KEY (reviewer_id) REFERENCES Reviewers(reviewer_id)
    ON DELETE CASCADE
    );

    -- TRUNCATE tables
    TRUNCATE TABLE Reviews;
    TRUNCATE TABLE Games;
    TRUNCATE TABLE Genres;
    TRUNCATE TABLE Developers;
    TRUNCATE TABLE Reviewers;

    -- Insert seed data

    -- Inserts values into Genres table
    INSERT INTO Genres (genre_id, genre_name) VALUES
    (1, 'Action'),
    (2, 'Role-Playing'),
    (3, 'Sports'),
    (4, 'Adventure'),
    (5, 'Simulation');

    -- Inserts values into Developers table
    INSERT INTO Developers (developer_id, developer_name) VALUES
    (1, 'Ubisoft'),
    (2, 'Electronic Arts'),
    (3, 'Bethesda Game Studios'),
    (4, 'Nintendo'),
    (5, 'FromSoftware');
    

    -- Inserts values into Games table
    INSERT INTO Games (game_id, game_title, genre_id, sales_count, release_date, developer_id) VALUES
    (1, 'Assassins Creed', 1, 3000000, '2007-11-13', 1),
    (2, 'FIFA 23', 3, 5000000, '2022-09-27', 2),
    (3, 'The Elder Scrolls V: Skyrim', 2, 10000000, '2011-11-11', 3),
    (4, 'The Legend of Zelda: Breath of the Wild', 4, 28000000, '2017-03-03', 4),
    (5, 'Elden Ring', 2, 20000000, '2022-02-25', 5);

    -- Inserts values into Reviewers table
    INSERT INTO Reviewers (reviewer_id, reviewer_company) VALUES
    (1, 'IGN'),
    (2, 'GameSpot'),
    (3, 'Metacritic'),
    (4, 'Polygon'),
    (5, 'Eurogamer');

    -- Inserts values into Reviews table
    INSERT INTO Reviews (review_id, game_id, reviewer_id, rating, comment, review_date) VALUES
    (1, 1, 1, 9, 'A thrilling start to a legendary series.', '2007-11-20'),
    (2, 2, 2, 8, 'Solid sports gameplay with great realism.', '2022-10-01'),
    (3, 3, 3, 10, 'A genre-defining RPG with endless replay value.', '2011-11-20'),
    (4, 4, 4, 10, 'An unforgettable open-world masterpiece.', '2017-03-05'),
    (5, 5, 5, 9, 'Challenging yet deeply rewarding gameplay.', '2022-03-01'),
    (6, 1, 2, 8, 'Fun parkour and interesting story.', '2007-11-25'),
    (7, 5, 1, 10, 'Dark fantasy perfection from FromSoftware.', '2022-03-02');

    SET FOREIGN_KEY_CHECKS = 1;

    SELECT 'Database reset successfully' AS status;
END//

DELIMITER ;