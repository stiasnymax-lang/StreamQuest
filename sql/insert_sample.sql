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
('First Blood', 'Defeat your first enemy without taking damage', 1, 'Any Action Game', 10),
('Speedrunner', 'Complete a level in under half the expected time', 2, 'Platformer', 20),
('Sharpshooter', 'Achieve 80% accuracy in a single mission', 3, 'FPS Game', 30),
('Survivor', 'Survive 10 minutes without dying', 2, 'Survival Game', 15),
('Boss Slayer', 'Defeat a boss without using healing items', 4, 'RPG', 45),
('Explorer', 'Discover all hidden areas in one map', 2, 'Open World Game', 30),
('Pacifist', 'Complete a level without killing any enemies', 4, 'Stealth Game', 25),
('Resource Manager', 'Finish a mission using only starting resources', 3, 'Strategy Game', 40),
('Combo Master', 'Perform a combo of 20 hits or more', 3, 'Fighting Game', 15),
('Untouchable', 'Complete a stage without taking any damage', 5, 'Action Game', 35),
('Collector', 'Collect all optional items in a level', 2, 'Adventure Game', 20),
('Nightmare Mode', 'Complete a mission on the highest difficulty', 5, 'Any Game', 60),
('Stealth Assassin', 'Eliminate all targets without being detected', 4, 'Stealth Game', 40),
('No HUD', 'Complete a level with the HUD disabled', 4, 'FPS Game', 30),
('Speed Builder', 'Build a functional base in under 10 minutes', 2, 'Simulation Game', 20),
('Ironman', 'Finish a mission without reloading a save', 5, 'RPG', 60),
('Sniper Elite', 'Get 5 headshots in a row without missing', 3, 'Shooter Game', 15),
('Minimalist', 'Win a match using only basic equipment', 3, 'Multiplayer Game', 25),
('Marathon', 'Play continuously for 2 hours without losing', 4, 'Arcade Game', 120),
('Tactician', 'Win a battle without losing any units', 4, 'Strategy Game', 45),
('Hardcore Start', 'Complete the tutorial on hardest difficulty', 2, 'Any Game', 15),
('Puzzle Genius', 'Solve a complex puzzle without hints', 3, 'Puzzle Game', 20),
('Economist', 'Finish a mission with maximum currency left', 3, 'RPG', 35),
('Environmental Kill', 'Defeat an enemy using the environment', 2, 'Action Game', 10),
('One Weapon Only', 'Complete a level using only one weapon', 3, 'Shooter Game', 30),
('Blind Run', 'Complete a level without using the map', 4, 'Adventure Game', 25),
('Flawless Victory', 'Win a fight without taking any hits', 4, 'Fighting Game', 10),
('Speed Healer', 'Revive a teammate within 3 seconds', 2, 'Multiplayer Game', 5),
('Last Stand', 'Win with less than 10% health remaining', 3, 'Action Game', 15),
('Completionist', 'Achieve 100% completion in a chapter', 5, 'Story Game', 90);

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
