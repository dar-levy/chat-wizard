# ChatWizard REST API

This project is a Flask-based REST API that uses OpenAI to generate responses to questions. The API is containerized using Docker, with a PostgreSQL database for storing questions and answers.

## Features

- **POST /ask**: Accepts a JSON object with a question and returns an answer from OpenAI.
- **Database**: Uses PostgreSQL to store questions and answers.
- **DB Migration**: Managed with Flask-Migrate and Alembic.
- **Dockerized**: Includes Dockerfile for the backend server and uses the official PostgreSQL Docker image.
- **Swagger Documentation**: API documentation available via Swagger UI.
- **Environment Configuration**: Uses `.env` and `.flaskenv` files for configuration.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python and pip

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/dar-levy/chat-wizard.git
   cd chat-wizard
   ```

2. **Create and fill the environment files**:

   - **.env**: Create a file named `.env` in the project root with the following content:

     ```env
     DATABASE_URL=postgresql://postgres:password@db/chatwizard
     OPENAI_API_KEY=your_openai_api_key_here
     ```

   - **.flaskenv**: Create a file named `.flaskenv` in the project root with the following content:

     ```env
     FLASK_APP=app
     FLASK_DEBUG=True
     ```

3. **Install Python dependencies**:

   Run the following command to install the necessary Python packages:

   ```sh
   pip install -r requirements.txt
   ```

4. **Start the Docker containers**:

   Use Docker Compose to start the backend and database containers:

   ```sh
   docker compose up -d
   ```

   This command will build the Docker images for the backend server and start both the backend and PostgreSQL containers.

5. **Run database migrations**:

   You need to set up the database schema. Run the following commands:

   - Generate the initial database migration:

     ```sh
     docker compose exec backend flask db migrate
     ```

   - Apply the migration to the database:

     ```sh
     docker compose exec backend flask db upgrade
     ```

### API Endpoints

- **POST /ask**: This endpoint accepts a JSON object with a question and returns an answer from OpenAI. The request should look like this:

  ```json
  {
    "question": "What is the capital of Israel?"
  }
  ```

  The response will be a JSON object with the answer and an ID:

  ```json
  {
    "id": 1,
    "question": "What is the capital of Israel?",
    "answer": "The capital of Israel is Jerusalem."
  }
  ```

### Swagger Documentation

The API documentation is available via Swagger UI. Once the Docker containers are running, you can access the Swagger UI at:

```
http://localhost:5000/swagger-ui
```
