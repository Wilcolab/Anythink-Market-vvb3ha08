# Anythink Market - Multi-Server Architecture

This project contains a multi-server application with both Python (FastAPI) and Node.js (Express) backend services. The servers are containerized using Docker and orchestrated with Docker Compose.

## Architecture Overview

The application consists of two independent backend servers:

1. **Python Server** (FastAPI) - Port 8000
   - Task management API
   - Fast, modern Python web framework
   - Auto-reloading with Uvicorn

2. **Express Server** (Node.js) - Port 8001
   - JavaScript/Node.js backend
   - Scaffold for future API endpoints
   - Auto-reloading with nodemon

## Project Structure

```
Anythink-Market/
├── docker-compose.yml           # Orchestrates both servers
├── python-server/
│   ├── Dockerfile              # Python server container config
│   ├── requirements.txt        # Python dependencies
│   ├── README.md              # Python server documentation
│   └── src/
│       ├── __init__.py        # Python package marker
│       └── main.py            # FastAPI application & routes
└── express-server/
    ├── Dockerfile              # Express server container config
    ├── package.json           # Node.js dependencies & scripts
    ├── README.md              # Express server documentation
    └── src/
        └── index.js           # Express application
```

## Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Ports 8000 and 8001 available

### Running the Application

Build and start both servers with Docker Compose:

```shell
docker compose up
```

This command will:
- Build Docker images for both servers
- Start containers for Python and Express servers
- Enable hot-reloading for development

### Accessing the Services

Once running, the services are available at:

- **Python Server**: http://localhost:8000
- **Express Server**: http://localhost:8001

## Python Server API Routes

The FastAPI server provides the following endpoints:

### Health Check
- **GET** `/` - Returns "Hello World" to verify server is running

### Task Management
- **GET** `/tasks` - Retrieves all tasks from the task list
- **POST** `/tasks` - Adds a new task to the list
  - Request body: `{"text": "task description"}`
  - Response: `{"message": "Task added successfully"}`

### Interactive API Documentation
FastAPI provides automatic interactive documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Express Server

The Express server is currently a scaffold with no endpoints defined. It serves as a foundation for implementing additional Node.js-based API functionality.

## Development

### Python Server Development
The Python server uses Uvicorn with the `--reload` flag for automatic code reloading. Any changes to files in `python-server/src/` will trigger a server restart.

### Express Server Development
The Express server uses nodemon for automatic reloading. Changes to files in `express-server/src/` will automatically restart the server when using `yarn start`.

## Docker Configuration

Both servers are configured with volume mounts in `docker-compose.yml` to enable live code reloading during development without rebuilding containers.

## Tech Stack

### Python Server
- **FastAPI**: Modern, fast web framework for Python
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI web server

### Express Server
- **Express.js**: Minimal and flexible Node.js web framework
- **Nodemon**: Auto-restart utility for development
