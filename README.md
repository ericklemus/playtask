# PlayTask

First of all, this was a really fun test
It was my first time developing an application using **FastAPI**, **Alembic**, and **SQLAlchemy**, and I learned a lot throughout the process.

Reading and understanding the documentation was a challenge for me at times, and I know there were many things I didn’t fully implement, but I'm very happy with the progress I made and what I’ve learned.

## Stack

- **FastAPI** – For the web framework and API layer
- **SQLAlchemy (2.0 style)** – For ORM and database interaction
- **Alembic** – For handling database migrations
- **PostgreSQL** – As the relational database
- **Docker & Docker Compose** – To containerize the app and manage dependencies
- **Pydantic v2** – For data validation

## How to Run Locally

You can easily spin up the entire project with Docker and Docker Compose.

### Prerequisites

- Docker installed
- Docker Compose installed

### 1. Clone the repository

```bash
git clone https://github.com/your-user/playtask.git
cd playtask
```

### 2. Start the containers
```bash
docker-compose up --build
```
This will:

Build the Python web app (from the Dockerfile)

Start the FastAPI server on http://localhost:8000

Start the PostgreSQL container on port 5432

### 3. Apply Migrations with Alembic
In another terminal (with containers running):

```bash
docker-compose exec web alembic upgrade head
```
This will apply all database migrations defined in your Alembic migrations folder.

### 4. Access the API
Go to http://localhost:8000/docs for the interactive Swagger UI

## Notes
The application uses SQLAlchemy 2.0 declarative style

Alembic was used for generating and applying database migrations

DTOs (Pydantic models) were used to separate input/output schemas cleanly

Routes follow RESTful conventions and include filters, toggles, and nested resources

## What’s Missing or Could Be Improved
- Full test coverage with pytest and a test database
- Authentication and user management
- More detailed error handling
- Pagination and sorting in list endpoints

## Final Thoughts
This was an incredible learning opportunity, and I’m proud of how far the project came. FastAPI is powerful and enjoyable to use — I’ll definitely keep building with it.

Thanks for reviewing this project!
