# TODO_APP

# Getting-Started
To begin using this project, follow the steps below to configure the sensor simulation and monitoring environment.
## Prerequisites
1. To ensure proper functionality, it is required to use Docker Compose version 2.0 or a more recent version.
2. Add all required credentials in ```.env``` file.

## Installation and Running

Before you start, ensure you have Docker and Docker Compose installed on your system. If not, you can install them by following the official Docker documentation:

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Aritra0124/TODO_APP
cd your-repo
```

### Step 2: Setup .env file

```text
MYSQL_ROOT_PASSWORD=your-root-password
MYSQL_DATABASE=your-database-name
MYSQL_USER=your-username
MYSQL_PASSWORD=your-password
MYSQL_HOST= todo_db
MYSQL_PORT=3306

ASANA_TOKEN= asana-token
```
### Step 3: Build and Run the Services

```bash
docker-compose up --build
```


## File Structure

```
.env
.env.example
.gitignore
README.md
docker-compose.yml
docker
   |-- Dockerfile
   |-- entrypoint.sh
   |-- requirements.txt
todo_project
   |-- __init__.py
   |-- manage.py
   |-- todo_app
   |   |-- __init__.py
   |   |-- admin.py
   |   |-- apps.py
   |   |-- forms.py
   |   |-- migrations
   |   |   |-- __init__.py
   |   |-- models.py
   |   |-- static
   |   |   |-- js
   |   |   |   |-- basic.js
   |   |   |   |-- utility.js
   |   |-- templates
   |   |   |-- base.html
   |   |   |-- index.html
   |   |   |-- message.html
   |   |-- tests.py
   |   |-- urls.py
   |   |-- views
   |   |   |-- __init__.py
   |   |   |-- asana_connection.py
   |   |   |-- asana_response.py
   |   |   |-- login.py
   |   |   |-- register.py
   |   |   |-- signout.py
   |-- todo_project
   |   |-- __init__.py
   |   |-- asgi.py
   |   |-- settings.py
   |   |-- urls.py
   |   |-- wsgi.py
```


- **`.env`**: Configuration file for environment variables.
- **`.env.emaple`**: Example Configuration file for environment variables. Follow the file contents for .env file
- **`.gitignore`**: Specifies intentionally untracked files to ignore in Git.
- **`README.md`**: Documentation file (you are here!).
- **`docker-compose.yml`**: Configuration file for Docker Compose.
- **`docker/`**: Directory containing Docker-related files.
  - **`Dockerfile`**: Instructions for building a Docker image.
  - **`entrypoint.sh`**: Shell script to be run when the Docker container starts.
  - **`requirements.txt`**: List of Python dependencies for the project.
- **`todo_project/`**: Django project directory.
  - **`__init__.py`**: Python package initialization file.
  - **`manage.py`**: Django management script for running administrative tasks.
  - **`todo_app/`**: Django app directory containing application-specific files.
    - **`forms.py`**: Form definitions for the app.
    - **`migrations/`**: Directory containing database migration files.
    - **`models.py`**: Database models for the app.
    - **`static/`**: Directory for static files (CSS, JavaScript, etc.).
      - **`js/`**: JavaScript files for the app.
      - **`css/`**: Style files for the app.
    - **`templates/`**: Directory for HTML templates used by the app.
      - **`base.html`**: Base template file.
      - **`index.html`**: Main page template.
      - **`message.html`**: Template for displaying messages.
    - **`tests.py`**: Unit tests for the app.
    - **`urls.py`**: URL patterns for the app.
    - **`views/`**: Directory containing view functions for the app.
      - **`asana_connection.py`**: View for Asana API connection.
      - **`asana_response.py`**: View for handling Asana API responses.
      - **`login.py`**: View for user login functionality.
      - **`register.py`**: View for user registration functionality.
      - **`signout.py`**: View for user sign-out functionality.
  - **`todo_project/`**: Django project configurations.
    - **`settings.py`**: Django project settings.
    - **`urls.py`**: Project-level URL patterns.

## Docker Compose file Description

### Docker Compose Services

### `django_todo_app` Service

The `django_todo_app` service is responsible for running the Django ToDo application. It is configured as follows:

- **Container Name**: `django_todo_app`
- **Build**: Builds the Docker image using the Dockerfile located in the `docker` directory.
- **Volumes**: Mounts the local `todo_project` directory into the container at `/var/www/todo_project`. This allows real-time code changes without rebuilding the container.
- **Environment Variables**: Reads environment variables from the `.env` file.
- **Working Directory**: Sets the working directory inside the container to `/var/www/todo_project`.
- **Command**: Executes the `/entrypoint.sh` script inside the container.
- **Ports**: Maps port `8990` on the host to port `8000` inside the container.
- **Dependencies**: Depends on the `todo_db` service.

### `todo_db` Service

The `todo_db` service runs a MySQL database for the Django ToDo application. It is configured as follows:

- **Container Name**: `todo_db`
- **Image**: Uses the official MySQL image (`mysql:8.1`).
- **Restart Policy**: Restarts the container automatically unless stopped.
- **TTY**: Allocates a pseudo-TTY to the container.
- **Environment Variables**:
  - `MYSQL_ROOT_PASSWORD`: Password for the MySQL root user.
  - `MYSQL_DATABASE`: Name of the MySQL database.
  - `MYSQL_USER`: Username for accessing the MySQL database.
  - `MYSQL_PASSWORD`: Password for the MySQL user.
- **Ports**: Maps port `3307` on the host to port `3306` inside the container.
- **Volumes**: Mounts the `./db-data/local` directory into the container at `/var/lib/mysql` for persistent data storage.
- **Health Check**: Checks if the container is healthy by running `exit 0` as the health test.

### Networks

- **`todoapp-network`**: Custom bridge network for communication between the `django_todo_app` and `todo_db` services. Configured with the IP subnet `172.16.220.0/24` for internal container communication.

This configuration allows the Django ToDo application to run in one container and the MySQL database in another, ensuring modularity and separation of concerns.

