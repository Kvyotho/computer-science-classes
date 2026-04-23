

#Matheus Braga Cetrangolo - CC3Mb - Banco de Dados II
# ----------------/Procedures/-----------------------------------------------------------------
#Procedures para popular o banco de dados
DROP PROCEDURE IF EXISTS PopulateAllData;
DROP PROCEDURE IF EXISTS CreatePlayers;
DROP PROCEDURE IF EXISTS CreateGames;
DROP PROCEDURE IF EXISTS CreateDevelopers;
DROP PROCEDURE IF EXISTS CreatePublishers;
DELIMITER $$

# 1. Procedure para criar os publishers
CREATE PROCEDURE CreatePublishers(IN num_publishers INT)
BEGIN
DECLARE i INT DEFAULT 1;
DELETE FROM publishers;
ALTER TABLE publishers AUTO_INCREMENT = 1;    
    WHILE i <= num_publishers DO
INSERT INTO publishers (name, country) VALUES (
CONCAT('Publisher ', i),
ELT(1 + FLOOR(RAND() * 5), 'USA', 'Japan', 'France', 'UK', 'Germany')
);
	SET i = i + 1;
END WHILE;
    
SELECT CONCAT('Created ', num_publishers, ' publishers') AS result;
END $$

# 2. Procedure para criar os developers
CREATE PROCEDURE CreateDevelopers(IN num_developers INT)
BEGIN
DECLARE i INT DEFAULT 1;
DECLARE pub_count INT;
DELETE FROM developers;
ALTER TABLE developers AUTO_INCREMENT = 1;

SELECT COUNT(*) INTO pub_count FROM publishers;
IF pub_count = 0 THEN
	CALL CreatePublishers(4);
SELECT COUNT(*) INTO pub_count FROM publishers;
END IF;

    WHILE i <= num_developers DO
INSERT INTO developers (name, publisherid) VALUES (
CONCAT('Dev Studio ', i),
1 + FLOOR(RAND() * pub_count)
);
SET i = i + 1;
END WHILE;
SELECT CONCAT('Created ', num_developers, ' developers') AS result;
END $$

# 3. Procedure para criar os jogos
CREATE PROCEDURE CreateGames(IN num_games INT)
BEGIN
DECLARE i INT DEFAULT 1;
DECLARE rand_limit INT;
DECLARE dev_count INT;
DELETE FROM games;
ALTER TABLE games AUTO_INCREMENT = 1;
DELETE FROM genres_has_games;
DELETE FROM platforms_has_games;
    
SELECT COUNT(*) INTO dev_count FROM developers;
IF dev_count = 0 THEN
	CALL CreateDevelopers(5);
	SELECT COUNT(*) INTO dev_count FROM developers;
END IF;
    WHILE i <= num_games DO
INSERT INTO games (title, developerid, reviewrating, release_date, price) VALUES (
CONCAT('Game ', i, ': ', 
ELT(1 + FLOOR(RAND() * 5), 'Adventure', 'Quest', 'Legends', 'Wars', 'Simulator')),
1 + FLOOR(RAND() * dev_count),
5 + ROUND(RAND() * 5, 1),
DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365*4) DAY),
10 + ROUND(RAND() * 60, 2)           
);
        
# Inserir 1-2 generos
INSERT INTO genres_has_games (genres_genreid, games_gameid)
SELECT genreid, LAST_INSERT_ID() FROM genres ORDER BY RAND() LIMIT 1;
        
# Inserir 1-3 plataformas
SET rand_limit := FLOOR(1 + RAND() * 3);
INSERT INTO platforms_has_games (platforms_platformid, games_gameid)
SELECT platformid, LAST_INSERT_ID() FROM platforms ORDER BY RAND() LIMIT rand_limit;
        
SET i = i + 1;
END WHILE;

SELECT CONCAT('Created ', num_games, ' games') AS result;
END $$

# 4. Procedure para criar os jogadores
CREATE PROCEDURE CreatePlayers(IN num_players INT)
BEGIN
DECLARE i INT DEFAULT 1;
DECLARE game_count INT;
DECLARE rand_limit INT;
DELETE FROM players;
ALTER TABLE players AUTO_INCREMENT = 1;
DELETE FROM players_has_games;
    
SELECT COUNT(*) INTO game_count FROM games;
    
IF game_count = 0 THEN
	CALL CreateGames(10);
	SELECT COUNT(*) INTO game_count FROM games;
END IF;
    
	WHILE i <= num_players DO
INSERT INTO players (username, joindate) VALUES (
CONCAT('player', i),
DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365*2) DAY)
);
        
# Inserindo 1-5 jogos de forma aleatoria para cada jogador
SET rand_limit := FLOOR(1 + RAND() * 5); 
INSERT INTO players_has_games (players_playerid, games_gameid, hoursplayed, last_played, purchase_date)
SELECT 
LAST_INSERT_ID(), 
gameid, 
1 + FLOOR(RAND() * 100),
DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365*2) DAY),
DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365*2) DAY)
FROM games ORDER BY RAND() LIMIT rand_limit;
        
SET i = i + 1;
END WHILE;

SELECT CONCAT('Created ', num_players, ' players') AS result;
END $$

# 5. Procedure geral para popular o banco todo
CREATE PROCEDURE PopulateAllData(
IN num_publishers INT,
IN num_developers INT,
IN num_games INT,
IN num_players INT
)
BEGIN
SET FOREIGN_KEY_CHECKS = 0;
#Setup de dados estaticos
INSERT IGNORE INTO genres (name) VALUES 
('Action'), ('Adventure'), ('Sports'), ('RPG'), ('FPS');
INSERT IGNORE INTO platforms (name) VALUES 
('PC'), ('PlayStation'), ('Xbox'), ('Switch');
    
#Setup de dados dinamicos
CALL CreatePublishers(num_publishers);
CALL CreateDevelopers(num_developers);
CALL CreateGames(num_games);
CALL CreatePlayers(num_players);
SET FOREIGN_KEY_CHECKS = 1;
SELECT 'Database population complete!' AS result;
END $$
DELIMITER ;
CALL PopulateAllData(30, 50, 5500, 2500);
#EXPLAIN FORMAT=JSON (o sql no meu computador pessoal se recusava a mostrar o visual explain das consultas, tive que usar isso pra ver o query cost)

# ----------------/Consultas/-----------------------------------------------------------------
#Consulta 1 - Jogadores (+nome do jogo) com 50 ou mais horas registradas
EXPLAIN FORMAT=JSON SELECT p.username Username, g.title Game, pg.hoursplayed Hours_Registered
FROM players_has_games pg
JOIN games g ON pg.games_gameid = g.gameid
JOIN players p ON pg.players_playerid = p.playerid
WHERE pg.hoursplayed >= 50
ORDER BY hoursplayed DESC;

#Consulta 2 - Média de preços, reviews e numeros de jogos produzidos pra cada Desenvolvedora
EXPLAIN FORMAT=JSON SELECT d.name dev, round(avg(g.price)) avg_price, round(avg(g.reviewrating)) avg_Rating, count(g.gameid) game_count 
FROM developers d
JOIN games g on d.developerid = g.developerid
GROUP BY d.name
ORDER BY AVG_rating DESC;

#Consulta 3 Analise dos Estudios de Desenvolvimento de Jogos
EXPLAIN FORMAT=JSON SELECT d.name developer, p.name publisher,
ROUND(AVG(g.price), 2) avg_price,
ROUND(AVG(g.reviewrating), 1) avg_rating,
COUNT(g.gameid) game_count,
MIN(YEAR(g.release_date)) first_release,
MAX(YEAR(g.release_date)) latest_release
FROM developers d
JOIN games g ON d.developerid = g.developerid
LEFT JOIN publishers p ON d.publisherid = p.publisherid
GROUP BY d.name, p.name 
ORDER BY Avg_Rating DESC, Game_Count DESC;

#Consulta 4 - Jogos com ultimo sessão registrada antes da compra 
#(Caso de demonstrações e reembolsos de jogos que posteriormente 
#foram comprados pelo jogador, mas ainda não foram acessados novamente)
EXPLAIN FORMAT=JSON SELECT p.username, g.title, pg.last_played, pg.purchase_date
FROM players_has_games pg
JOIN games g ON pg.games_gameid = g.gameid
JOIN players p ON pg.players_playerid = p.playerid
WHERE pg.last_played < pg.purchase_date;

#Consulta 5 - Quantas horas o jogador possui em cada genero de jogo
EXPLAIN FORMAT=JSON SELECT p.username, gen.name favorite_genre, SUM(pg.hoursplayed) total_hours
FROM players p
JOIN players_has_games pg ON p.playerid = pg.players_playerid
JOIN games g ON pg.games_gameid = g.gameid
JOIN genres_has_games gg ON g.gameid = gg.games_gameid
JOIN genres gen ON gg.genres_genreid = gen.genreid
GROUP BY p.playerid, gen.name
ORDER BY p.username, total_hours DESC;



# ----------------/INDEX/-----------------------------------------------------------------
#/*
DROP INDEX idx_games_title ON games;
DROP INDEX idx_pg_hours ON players_has_games;
DROP INDEX idx_pg_composite ON players_has_games;
DROP INDEX idx_games_dev ON games;
DROP INDEX idx_games_rating ON games;
DROP INDEX idx_devpub ON developers;
DROP INDEX idx_games_stats ON games;
DROP INDEX idx_pg_dates ON players_has_games;
DROP INDEX idx_pg_player ON players_has_games;
DROP INDEX idx_gg_game ON genres_has_games;
DROP INDEX idx_games_gameid ON games;
DROP INDEX idx_players_playerid ON players;
#*/
CREATE INDEX idx_games_title ON games(title);
CREATE INDEX idx_pg_hours ON players_has_games(hoursplayed);
CREATE INDEX idx_pg_composite ON players_has_games(games_gameid, players_playerid);

CREATE INDEX idx_games_dev ON games(developerid);
CREATE INDEX idx_games_rating ON games(reviewrating);

CREATE INDEX idx_devpub ON developers(developerid, name, publisherid);
CREATE INDEX idx_games_stats ON games(developerid, price, reviewrating, release_date);

CREATE INDEX idx_pg_dates ON players_has_games(purchase_date, last_played);

CREATE INDEX idx_pg_player ON players_has_games(players_playerid);
CREATE INDEX idx_gg_game ON genres_has_games(games_gameid);

# ----------------/Triggers/-----------------------------------------------------------------
DELIMITER $$
CREATE TRIGGER update_last_login
BEFORE UPDATE ON players
FOR EACH ROW
BEGIN
IF NEW.account_status = 'active' AND OLD.account_status != 'active' THEN
	SET NEW.last_login = NOW();
END IF;
END $$

CREATE TRIGGER validate_release_date
BEFORE INSERT ON games
FOR EACH ROW
BEGIN
IF NEW.release_date > CURDATE() THEN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Invalid Release Date.';
END IF;
END $$

CREATE TRIGGER prevent_duplicate_purchase
BEFORE INSERT ON players_has_games
FOR EACH ROW
BEGIN
DECLARE game_count INT;
    
SELECT COUNT(*) INTO game_count
FROM players_has_games
WHERE players_playerid = NEW.players_playerid
AND games_gameid = NEW.games_gameid;
    
IF game_count > 0 THEN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Invalid Purchase. Account already owns this game.';
END IF;
END $$

# ----------------/UDFs/-----------------------------------------------------------------
CREATE FUNCTION game_age(game_id INT) 
RETURNS INT
DETERMINISTIC
BEGIN
DECLARE release_year YEAR;
DECLARE age INT;

SELECT YEAR(release_date) INTO release_year
FROM games WHERE gameid = game_id;
SET age = YEAR(CURDATE()) - release_year;
RETURN age;
END  $$

CREATE FUNCTION rating_category(rating DECIMAL(3,1))
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE category VARCHAR(20);
IF rating >= 9.0 THEN
	SET category = 'Very High Positive rating';
ELSEIF rating >= 8.0 THEN
	SET category = 'High Positive rating';
ELSEIF rating >= 7.0 THEN
	SET category = 'Good rating';
ELSEIF rating >= 6.0 THEN
	SET category = 'Average rating';
ELSE
	SET category = 'Poor rating';
END IF;
RETURN category;
END $$

CREATE FUNCTION calc_discount(original_price DECIMAL(10,2), discount_percent INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
DECLARE discounted_price DECIMAL(10,2);
SET discounted_price = original_price * (1 - discount_percent/100);
RETURN ROUND(discounted_price, 2);
END $$

DELIMITER ;

# -----------------------------/Testing Triggers/---------------------------------------------------------
# 1 TRIGGER
UPDATE players 
SET account_status = 'inactive', last_login = NULL 
WHERE playerid = 1;

UPDATE players 
SET account_status = 'active' 
WHERE playerid = 1 AND account_status != 'active';

# Verificando
SELECT playerid, username, account_status, last_login 
FROM players 
WHERE playerid = 1;

# 2 TRIGGER
INSERT INTO games (title, developerid, release_date) 
VALUES ('Invalid game testing', 1, DATE_ADD(CURDATE(), INTERVAL 1 MONTH));

INSERT INTO games (title, developerid, release_date) 
VALUES ('Valid game testing', 1, CURDATE());

SELECT gameid, title, release_date FROM games WHERE title = 'Valid game testing';

# 3 TRIGGER
SELECT * from players_has_games;
INSERT INTO players_has_games (players_playerid, games_gameid) 
VALUES (1, 1);

# -----------------------------/Testing UDFs/---------------------------------------------------------

SELECT * FROM games WHERE gameid = 25;
SELECT game_age(25);

SELECT rating_category(8.2);
SELECT rating_category(2.2);
SELECT rating_category(7.5);

SELECT calc_discount(100.00, 20);
SELECT calc_discount(200.00, 10);
SELECT calc_discount(100.00, 50);
SELECT calc_discount(300.00, 25);


