BEGIN TRANSACTION;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
);

CREATE TABLE challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    game_name TEXT NOT NULL,
    time_needed INTEGER NOT NULL
);

CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    owner_id INTEGER,
    session_start DATETIME,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE TABLE group_members (
    owner_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (owner_id) REFERENCES users(id),
    PRIMARY KEY (user_id, group_id)
);
CREATE TABLE group_challenges (
    group_id INTEGER NOT NULL,
    challenge_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'queued', -- queued | active | done
    assigned_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    started_at DATETIME,
    finished_at DATETIME,
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (challenge_id) REFERENCES challenges(id),
    PRIMARY KEY (group_id, challenge_id)
);
COMMIT;
