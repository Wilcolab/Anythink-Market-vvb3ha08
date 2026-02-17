# Anythink Market - System Architecture

## Overview

Anythink Market is a microservices-based application featuring two independent backend services that communicate via REST APIs. The architecture is designed for scalability, maintainability, and ease of development.

## System Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│             Docker Compose Network              │
│                                                 │
│  ┌────────────────────┐  ┌──────────────────┐ │
│  │  Python Server     │  │  Express Server  │ │
│  │  (FastAPI)         │  │  (Node.js)       │ │
│  │                    │  │                  │ │
│  │  Port: 8000        │  │  Port: 8001      │ │
│  │  Framework: FastAPI│  │  Framework: Express
│  │  Language: Python  │  │  Language: JS    │ │
│  │                    │  │                  │ │
│  │  Features:         │  │  Features:       │ │
│  │  - Task Management │  │  - Scaffold      │ │
│  │  - Auto Swagger    │  │  - Hot Reload    │ │
│  │  - Hot Reload      │  │  - Future APIs   │ │
│  └────────────────────┘  └──────────────────┘ │
│           ↑                       ↑            │
│           │                       │            │
└───────────┼───────────────────────┼────────────┘
            │                       │
            └───────────┬───────────┘
                        │
                  ┌─────▼─────┐
                  │   Client  │
                  │ Application│
                  └───────────┘
```

## Service Details

### Python Server (Port 8000)

**Purpose**: Task management API with CRUD operations

**Technology Stack**:
- **Framework**: FastAPI - Modern, high-performance Python web framework
- **Server**: Uvicorn - ASGI server with auto-reload
- **Validation**: Pydantic - Data validation using Python type hints
- **Documentation**: Auto-generated Swagger UI and ReDoc

**Key Features**:
- RESTful API endpoints for task management
- Automatic request/response validation
- Interactive API documentation at `/docs`
- Hot-reloading in development mode
- Type-safe operations with Python type hints

**Current Endpoints**:
- `GET /` - Health check endpoint
- `GET /tasks` - Retrieve all tasks
- `POST /tasks` - Create a new task

**Data Models**:
```python
class Task(BaseModel):
    text: str  # Task description
```

**Storage**: In-memory list (suitable for development; migrate to database for production)

### Express Server (Port 8001)

**Purpose**: Node.js backend scaffold for future API development

**Technology Stack**:
- **Framework**: Express.js - Minimal and flexible Node.js web framework
- **Runtime**: Node.js 18 (Alpine Linux container)
- **Dev Tool**: Nodemon - Auto-restart on file changes

**Key Features**:
- Lightweight and fast
- Ready for middleware integration
- Prepared for REST or GraphQL endpoints
- Hot-reloading with nodemon

**Future Enhancements**:
- Add body-parser middleware for JSON parsing
- Implement CORS for cross-origin requests
- Add authentication middleware
- Implement error handling middleware
- Define API routes and controllers

## Docker Architecture

### Container Configuration

Both services run in separate Docker containers orchestrated by Docker Compose:

**Python Server Container**:
- Base Image: `python:3.9-slim`
- Working Directory: `/app`
- Volume Mounts: `./python-server/src:/app/src` (for hot-reload)
- Port Mapping: `8000:8000`

**Express Server Container**:
- Base Image: `node:18-alpine`
- Working Directory: `/app`
- Volume Mounts: 
  - `./express-server/src:/app/src`
  - `./express-server/package.json:/app/package.json`
- Port Mapping: `8001:8001`

### Development Workflow

1. **Local Development**: Volume mounts enable live code changes without container rebuilds
2. **Automatic Reloading**:
   - Python: Uvicorn `--reload` flag watches for file changes
   - Node.js: Nodemon monitors source files
3. **Isolated Environments**: Each service runs in its own container with dedicated dependencies

## API Communication Patterns

### Inter-Service Communication (Future)

While currently independent, services can communicate via:
- REST APIs (recommended for loose coupling)
- Shared message queue (for async operations)
- Database sharing (not recommended; prefer API calls)

### Client Communication

Clients interact with services via HTTP/REST:
- Direct API calls to individual services
- Optional API Gateway (future enhancement)
- Load balancer for horizontal scaling (future enhancement)

## Data Flow

### Task Creation Flow (Python Server)

```
Client → POST /tasks → FastAPI → Pydantic Validation → Append to List → Response
```

### Task Retrieval Flow (Python Server)

```
Client → GET /tasks → FastAPI → Retrieve from List → JSON Response
```

## Development Guidelines

### Python Server Development

**Adding New Endpoints**:
```python
@app.get("/endpoint")
def endpoint_name():
    """Docstring for auto-generated docs"""
    # Implementation
    pass
```

**Data Models**:
- Use Pydantic models for request/response validation
- Add type hints for IDE support and validation
- Include docstrings for API documentation

### Express Server Development

**Adding New Endpoints**:
```javascript
/**
 * Endpoint description for documentation
 */
app.get('/endpoint', (req, res) => {
    // Implementation
    res.json({ data: 'response' });
});
```

**Middleware Pattern**:
```javascript
// Add before route definitions
app.use(express.json());
app.use(cors());
```

## Security Considerations

### Current State
- No authentication implemented
- No CORS configuration
- No rate limiting
- No input sanitization beyond type validation

### Recommended Enhancements
1. Add JWT authentication
2. Implement CORS with whitelist
3. Add rate limiting middleware
4. Enable HTTPS in production
5. Sanitize user inputs
6. Add request validation middleware
7. Implement API versioning

## Scalability Considerations

### Current Architecture Supports:
- Horizontal scaling (multiple container instances)
- Independent service scaling
- Stateless operation (in-memory storage is temporary)

### Future Enhancements:
1. **Database Integration**: Replace in-memory storage with PostgreSQL/MongoDB
2. **Caching Layer**: Add Redis for frequently accessed data
3. **Load Balancer**: Distribute requests across instances
4. **Service Discovery**: Implement for dynamic service location
5. **Message Queue**: Add RabbitMQ/Kafka for async operations
6. **API Gateway**: Centralized entry point with rate limiting

## Monitoring & Logging

### Current State
- Basic console logging
- Docker Compose logs via `docker compose logs`

### Recommended Additions
1. **Structured Logging**: JSON format for log aggregation
2. **Application Metrics**: Prometheus + Grafana
3. **Health Checks**: Docker health check endpoints
4. **Error Tracking**: Sentry or similar service
5. **Performance Monitoring**: APM tools (New Relic, DataDog)

## Testing Strategy

### Unit Testing
- Python: pytest for FastAPI endpoints
- Node.js: Jest for Express routes

### Integration Testing
- Test API contracts between services
- Database integration tests

### E2E Testing
- Postman collections
- Automated API testing with Newman

## Deployment

### Development
- Local Docker Compose deployment
- Volume mounts for hot-reloading

### Production
- Remove volume mounts
- Use production-grade WSGI/ASGI servers
- Enable health checks
- Set up monitoring and logging
- Use environment variables for configuration
- Implement CI/CD pipeline

## Environment Variables

### Python Server
- `PORT`: Server port (default: 8000)
- `RELOAD`: Enable auto-reload (development only)
- `DATABASE_URL`: Database connection string (future)

### Express Server
- `PORT`: Server port (default: 8001)
- `NODE_ENV`: Environment (development/production)
- `DATABASE_URL`: Database connection string (future)

## File Organization Best Practices

### Python Server Structure
```
python-server/
├── src/
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── models/           # Pydantic models (future)
│   ├── routes/           # API routes (future)
│   ├── services/         # Business logic (future)
│   └── utils/            # Helper functions (future)
├── tests/                # Test files (future)
├── requirements.txt
└── Dockerfile
```

### Express Server Structure
```
express-server/
├── src/
│   ├── index.js          # Application entry point
│   ├── routes/           # API routes (future)
│   ├── controllers/      # Request handlers (future)
│   ├── middleware/       # Custom middleware (future)
│   ├── models/           # Data models (future)
│   └── utils/            # Helper functions (future)
├── tests/                # Test files (future)
├── package.json
└── Dockerfile
```

## Glossary

- **FastAPI**: Modern Python web framework with automatic API documentation
- **Express.js**: Minimal Node.js web application framework
- **Uvicorn**: ASGI server for Python async frameworks
- **Pydantic**: Data validation library using Python type hints
- **Nodemon**: Utility for auto-restarting Node.js applications
- **Docker Compose**: Tool for defining multi-container applications
- **Hot-reload**: Automatic server restart on code changes
- **ASGI**: Asynchronous Server Gateway Interface for Python
- **REST**: Representational State Transfer (API architecture style)

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Express.js Documentation](https://expressjs.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
