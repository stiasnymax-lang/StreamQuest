BEGIN TRANSACTION;
DELETE FROM group_members;
DELETE FROM groups;
DELETE FROM challenges;
DELETE FROM users;
DELETE FROM sqlite_sequence;
INSERT INTO users (username, password, email) VALUES
('alice', 'password123', 'alice#example.com'),
('bob', 'securepass', 'bob#example.com'),
('charlie', 'mypassword', 'charlie#example.com');
INSERT INTO challenges (title, description, difficulty, game_name, time_needed) VALUES
('Challenge 1', 'Complete level 1', 1, 'Game A', 30),
('Challenge 2', 'Defeat the boss', 3, 'Game B', 60),
('Challenge 3', 'Find the hidden item', 2, 'Game C', 45);
INSERT INTO groups (name, password, owner_id, challenge_id) VALUES
('gamers', 'gamerpass', 1, 1),
('developers', 'devpass', 2, 2),
('designers', 'designpass', 3, 3);
INSERT INTO group_members (user_id, group_id) VALUES
(1, 1),
(2, 1),
(2, 2),
(3, 3);
COMMIT;