BEGIN TRANSACTION;
DELETE from users;
DELETE from groups;
DELETE from group_members;
DELETE from challenges;
DELETE from sqlite_sequence;
INSERT INTO users (username, password, email) VALUES
('alice', 'password123', 'asdSAda#example.com'),
('bob', 'securepass', 'sadasdASD#example.com'),
('charlie', 'mypassword', 'asdasdASD#example.com');
INSERT INTO groups (name, password) VALUES
('gamers', 'gamerpass'),
('developers', 'devpass'),
('designers', 'designpass');
INSERT INTO group_members (user_id, group_id) VALUES
(1, 1),
(2, 1),
(2, 2),
(3, 3);
INSERT INTO challenges (title, description, difficulty, game_name, time_needed) VALUES
('Challenge 1', 'Complete level 1', 1, 'Game A', 30),
('Challenge 2', 'Defeat the boss', 3, 'Game B', 60),
('Challenge 3', 'Find the hidden item', 2, 'Game C', 45);
COMMIT;