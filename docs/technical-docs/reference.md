---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Max Stiasny]
[Lukas Hoppart]

{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Home

### `index()`

**Route:** `/`

**Methods:** `GET`

**Purpose:** Render the landing page.

**Sample output:** HTML page (`index.html`).

---

## Overlay

### `overlay(group_id)`

**Route:** `/overlay/<int:group_id>/`

**Methods:** `GET`

**Purpose:** Display an overlay view for a specific group. Supports returning either an HTML overlay page or a JSON payload for polling/stream overlays.

**Query parameters:**
- `json` (optional): if present (e.g. `?json=1`), the route returns a JSON response instead of HTML.

**Authentication:** Requires login (`login_required`).

**Behavior / Notes:**
- If the logged-in user is **not a member** of the group, they are redirected to `join_group(group_id)`.
- Returns `404` if the group does not exist.
- Calculates progress based on `done`, `active`, and `queued` challenges.

---

## Challenges

### `challenges()`

**Route:** `/challenges/`

**Methods:** `GET`

**Purpose:** List all challenges with optional title filtering.

**Query parameters:**
- `c` (optional): filter string matched against `title` via SQL `LIKE`.

---

### `challenge(challenge_id)`

**Route:** `/challenge/<int:challenge_id>/`

**Methods:** `GET`

**Purpose:** Show details for a single challenge.

**Errors:** `404` if the challenge does not exist.

---

## Static pages

### `support()`

**Route:** `/support/`

**Methods:** `GET`

**Purpose:** Render the support page.

---

### `guide()`

**Route:** `/guide/`

**Methods:** `GET`

**Purpose:** Render the guide page.

---

## Authentication

### `login()`

**Route:** `/login/`

**Methods:** `GET` `POST`

**Purpose:** Authenticate a user and create a session.

**Behavior / Notes:**
- `GET`: loads all users for selection/display in the UI.
- `POST`: validates credentials, sets `session['user_id']`, flashes success/error messages.

---

### `register()`

**Route:** `/register/`

**Methods:** `GET` `POST`

**Purpose:** Register a new user.

**Behavior / Notes:**
- `POST`: inserts user into `users(username, password, email)` and redirects to login on success.

---

## Profile

### `profile()`

**Route:** `/profile/`

**Methods:** `GET` `POST`

**Purpose:** Show the profile of the logged-in user and allow account actions (logout).

**Authentication:** Requires login (`login_required`).

**Behavior / Notes:**
- Loads user info from `users`.
- Loads the user’s groups via `group_members` and `groups`.
- On POST with logout action: clears session and redirects to `/`.

---

## Groups

### `groups()`

**Route:** `/groups/`

**Methods:** `GET`

**Purpose:** List groups with optional search.

**Query parameters:**
- `g` (optional): filter string matched against `groups.name` via SQL `LIKE`.

**Behavior / Notes:**
- Also returns `member_count` via `LEFT JOIN group_members` + `COUNT`.

---

### `join_group(group_id)`

**Route:** `/join/<int:group_id>/`

**Methods:** `GET` `POST`

**Purpose:** Join a group by providing the group password.

**Authentication:** Requires login (`login_required`).

**Behavior / Notes:**
- Returns `404` if the group does not exist.
- If the user is already a member, redirects to `group(group_id)`.
- On valid password: inserts membership into `group_members` and redirects to the group page.

---

### `group(group_id)`

**Route:** `/group/<int:group_id>/`

**Methods:** `GET` `POST`

**Purpose:** Display and manage a group and its challenges.

**Authentication:** Requires login (`login_required`).

**Behavior / Notes:**
- If the user is **not a member**, redirects to `join_group(group_id)`.
- Returns `404` if the group does not exist.
- Loads:
  - owner (`users`)
  - members (`group_members` + `users`, excluding owner)
  - active challenge (`group_challenges.status='active'`)
  - done challenges (incl. duration via `strftime` diff)
  - queued challenges
  - challenge search results excluding already assigned challenges for that group

**POST actions (via `GroupForm`):**
- Add challenge: insert into `group_challenges`
- Delete challenge: delete from `group_challenges`
- Set active challenge:
  - demote previous active to queued and clear `started_at`
  - set new active and set `started_at = CURRENT_TIMESTAMP`
- Complete active challenge: set status `done` and `finished_at = CURRENT_TIMESTAMP`
- Leave group:
  - blocked for owner
  - deletes membership for current user
- Delete group (owner only):
  - deletes related `group_challenges`, `group_members`, then `groups`
- Remove member (owner only):
  - deletes a member from `group_members` (owner cannot be removed)

---

## Create group

### `create_group()`

**Route:** `/create_group/`

**Methods:** `GET` `POST`

**Purpose:** Create a new group.

**Authentication:** Requires login (`login_required`).

**Behavior / Notes:**
- Inserts into `groups(name, password, owner_id)`
- Adds owner as a member in `group_members`
- Redirects to `group(group_id)` on success

---

## Utility / Sample data

### `run_insert_sample()`

**Route:** `/insert/sample/`

**Methods:** `GET`

**Purpose:** Insert a predefined sample dataset into the database.

---

## Internal helpers in `functions.py`

### `login_required()`

**Purpose:** Guard for protected routes. Redirects to login if user is not authenticated.
