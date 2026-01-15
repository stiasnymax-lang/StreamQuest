BEGIN TRANSACTION;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    abonoment INTEGER DEFAULT 0
);

CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    owner_id INTEGER NOT NULL,
    challenge_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES users(id),
    FOREIGN KEY (challenge_id) REFERENCES challenges(id)
);

CREATE TABLE group_members (
    user_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    PRIMARY KEY (user_id, group_id)
);

CREATE TABLE challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    game_name TEXT NOT NULL,
    time_needed INTEGER NOT NULL
    -- optional: ,user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(id)
);

COMMIT;
