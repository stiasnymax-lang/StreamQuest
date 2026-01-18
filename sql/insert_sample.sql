BEGIN TRANSACTION;

DELETE FROM group_challenges;
DELETE FROM group_members;
DELETE FROM groups;
DELETE FROM challenges;
DELETE FROM users;

-- Autoincrement zurücksetzen
DELETE FROM sqlite_sequence;

-- Users
INSERT INTO users (username, password, email) VALUES
('alice', 'password123', 'alice@example.com'),
('bob', 'securepass', 'bob@example.com'),
('charlie', 'mypassword', 'charlie@example.com');

-- Challenges
INSERT INTO challenges (title, description, difficulty, game_name, time_needed) VALUES
('Challenge 1', 'Complete level 1', 1, 'Game A', 30),
('Challenge 2', 'Defeat the boss', 3, 'Game B', 60),
('Challenge 3', 'Find the hidden item', 2, 'Game C', 45);

-- Groups (ohne challenge_id)
INSERT INTO groups (name, password, owner_id) VALUES
('gamers', 'gamerpass', 1),
('developers', 'devpass', 2),
('designers', 'designpass', 3);

-- Group Members
INSERT INTO group_members (owner_id, user_id, group_id) VALUES
(1, 1, 1),
(2, 1, 2),
(2, 2, 2),
(3, 3, 3);

-- Group Challenges (Zuordnung + Status)
INSERT INTO group_challenges (group_id, challenge_id, status, started_at) VALUES
(1, 1, 'active', CURRENT_TIMESTAMP),
(1, 2, 'queued', CURRENT_TIMESTAMP),
(1, 3, 'done', CURRENT_TIMESTAMP),
(2, 2, 'active', CURRENT_TIMESTAMP),
(2, 3, 'queued', CURRENT_TIMESTAMP),
(2, 1, 'done', CURRENT_TIMESTAMP),
(3, 3, 'active', CURRENT_TIMESTAMP),
(3, 1, 'queued', CURRENT_TIMESTAMP),
(3, 2, 'done', CURRENT_TIMESTAMP);

COMMIT;
