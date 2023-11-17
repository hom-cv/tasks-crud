# tasks-crud
Task CRUD App, mini-project from Strike Social Interview
This mini-app uses `Flask` and `SQLAlchemy` to perform basic CRUD operations on a PostgreSQL database. It is also dockerized via `Docker Compose` for ease and consitency in setting up on other machines.

## Prompt
> You are tasked with designing and implementing an API for a Task Management System that allows users to create, update, delete, and view tasks. Your goal is to design the API and provide a functional implementation of the system.

## Setup
### Initial setup
Since at Strike Social, the backend is already in Python, I will assume that anyone testing this will also have Python installed (3.10+)
- ### (Mac Only)
  Install `postgre` on Mac via
```
brew install postgre
```

### Installing Docker
Sign up and install [Docker Desktop](https://www.docker.com/products/personal/) to set up containers on your local machine. It should be fine to use the latest available version.

### Local setup
After pulling the repository, open a terminal and naviagte to the directory.

Ensure that Docker Desktop is running and then start the server using the command:
```
docker-compose up --build
```

In the Docker Desktop UI, you should have the following containers running.

![Screenshot 2566-11-17 at 15 09 36](https://github.com/hom-cv/tasks-crud/assets/82633920/9571427e-6897-4547-bab1-2cfe3884db37)

## Using the API
The web server is hosted on localhost port 5000, so the base URL for all endpoint calls will be
```
http://localhost:5000
```

### Endpoints
```
/users GET
```
- Gets all available users in the database.
  - The database is initialized with a single Default User, with a corresponding `id` of `c449c8d9-32cc-470c-b479-c63add1efb88`

```
/task GET
```
- Gets all available tasks.
- Optional URL parameters: `status`, `created_by`, `updated_by`, `due_at`

```
/task/<uuid:task_id> GET
```
- Gets the task associated with the `task_id`

```
/task POST
```
- Creates a new task using passed data
- Request body must be in format:
```
{
  title: string,
  description: string,
  due_at: date string in MM/DD/YYYY format,
  status: one of ['pending','completed','in_progress'],
  user_id: any valid user_id (c449c8d9-32cc-470c-b479-c63add1efb88)
}
```

```
/task/<uuid:task_id> PUT
```
- Updates the task with id=`task_id` with data in request body
-  Request body must be in format:
```
{
  title: string,
  description: string,
  due_at: date string in MM/DD/YYYY format,
  status: one of ['pending','completed','in_progress'],
  user_id: any valid user_id (c449c8d9-32cc-470c-b479-c63add1efb88)
}
```

```
/task/<uuid:task_id> DELETE
```
- Deletes task with the given `task_id`

## Troubleshooting

If the web server is not running but the database is running, simply click the play button next to the web container to start running the web service. This can happen when postgres is not finished setting up before docker attempts to run the web container. Usually there will be a script that waits for postgres to finish initializing before running the web server.

If any issues arise with using the API, I have some tests set up to show examples of the API in use:

https://www.postman.com/cryosat-cosmologist-2945682/workspace/task-crud-strike-social/overview
