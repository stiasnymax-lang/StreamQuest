---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation


<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Routes

### `index()`

**Route:** `/`

**Methods:** `GET`

**Purpose:** Render the landing page.

**Sample output:** HTML page (`index.html`).

---

### `overlay(group_id)`

**Route:** `/overlay/<int:group_id>/`

**Methods:** `GET`

**Purpose:** Display an overlay view for a specific group. Supports returning either an HTML overlay page or a JSON payload for polling/stream overlays.

**Query parameters:**
- `json` (optional): if present (e.g. `?json=1`), the route returns a JSON response instead of HTML.

**Authentication:** Requires login (`logincheck()`).

**Sample output:**

- **HTML mode (default):** renders `overlay.html`
- **JSON mode (`?json=1`):**
```json
{
  "group_name": "My Group",
  "active_challenge": {"id": 1, "title": "Example", "status": "active"},
  "queued_challenges": [{"id": 2, "title": "Next challenge", "status": "queued"}]
}
```

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

### `pricing()`

**Route:** `/pricing/`

**Methods:** `GET`

**Purpose:** Render the pricing page.

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

---

### `register()`

**Route:** `/register/`

**Methods:** `GET` `POST`

**Purpose:** Register a new user.

---

## Profile

### `profile()`

**Route:** `/profile/`

**Methods:** `GET`

**Purpose:** Show the profile of the logged-in user.

---

## Groups

### `groups()`

**Route:** `/groups/`

**Methods:** `GET`

**Purpose:** List groups with optional search.

---

### `join_group(group_id)`

**Route:** `/join/<int:group_id>/`

**Methods:** `GET` `POST`

**Purpose:** Join a group by providing the group password.

---

### `group(group_id)`

**Route:** `/group/<int:group_id>/`

**Methods:** `GET` `POST`

**Purpose:** Display and manage a group and its challenges.

---

## Create group

### `create_group()`

**Route:** `/create_group/`

**Methods:** `GET` `POST`

**Purpose:** Create a new group.

---

## Utility / Sample data

### `run_insert_sample()`

**Route:** `/insert/sample/`

**Methods:** `GET`

**Purpose:** Insert a predefined sample dataset into the database.

---

## Internal helpers

### `logincheck()`

**Purpose:** Guard for protected routes. Redirects to login if user is not authenticated.

