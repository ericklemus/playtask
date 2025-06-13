# Decision Log – PlayTask 📝

This is a little log of the decisions I made while building PlayTask.  

---

## 1. ORM: SQLAlchemy

- **What I chose:** SQLAlchemy
- **Why:** It’s powerful, widely used, and integrates well with Alembic, and was a good time to learn how to use.
- **Outcome:** A bit of a learning curve.

---

## 2. Migrations: Alembic

- **What I chose:** Alembic for database migrations.
- **Why:** It works natively with SQLAlchemy and is pretty much the standard.
- **Outcome:** Confusing at first, but once I took the rythm, it saved a lot of headaches when evolving the DB schema.

---

## 3. Docker & Docker Compose

- **What I chose:** Dockerize the app and database.
- **Why:** Makes setup consistent and easy to run locally (and later, deploy).
- **Outcome:** Took a bit of tinkering to get the containers playing nicely, but worth it in the end.

---

## 4. Pydantic DTOs

- **What I chose:** Separate the Pydantic schemas (DTOs) from the ORM models.
- **Why:** Cleaner separation of concerns, more control over what goes in/out of the API.
- **Outcome:** More code to write, but way more maintainable and predictable.

---

## 5. Project Structure (Clean Architecture)

- **What I chose:** Separate layers: `presentation`, `usecases`, `domain`, `infrastructure`.
- **Why:** To avoid spaghetti and make the code easier to test and extend later.
- **Outcome:** Might be a bit overkill for a small app, but it helped me think more clearly about responsibilities.

---

## Final Notes

Many of these decisions were firsts for me. Some took trial and error, but each one helped me level up.  
I'm proud of how far this project came, and I hope future-me (or anyone reading this) finds this useful.