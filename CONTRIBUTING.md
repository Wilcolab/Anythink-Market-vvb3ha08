# Contributing to Anythink Market

This guide will help you understand the codebase and contribute effectively using GitHub Copilot.

## Getting Started with GitHub Copilot

GitHub Copilot works best when it has proper context about your codebase. This project is structured with detailed documentation to maximize Copilot's effectiveness.

### Key Context Files

Before coding, ensure you're familiar with:
- **ARCHITECTURE.md** - System design and component overview
- **README.md** - Quick start and basic usage
- **docker-compose.yml** - Service orchestration
- Individual server README files

### Using Copilot Effectively

1. **Open Relevant Files**: Keep related files open in VS Code tabs
2. **Read Comments**: Inline comments guide Copilot's suggestions
3. **Use Descriptive Names**: Function and variable names help Copilot understand intent
4. **Write Clear Comments**: Describe what you want before writing code

## Development Setup

### Initial Setup

1. Clone the repository
2. Ensure Docker and Docker Compose are installed
3. Start the services:
   ```bash
   docker compose up
   ```

### Development Workflow

#### Python Server Development

1. Navigate to `python-server/src/`
2. Make changes to Python files
3. Uvicorn automatically reloads on file changes
4. Test endpoints at http://localhost:8000
5. View API docs at http://localhost:8000/docs

**Adding a New Endpoint**:
```python
@app.get("/new-endpoint")
def new_endpoint():
    """
    Clear description for Copilot and API docs.
    Copilot will suggest implementation based on this.
    """
    # Start typing and let Copilot suggest
    pass
```

**Adding a Data Model**:
```python
class NewModel(BaseModel):
    """Model description for Copilot"""
    field_name: str  # Copilot understands type hints
    # Add more fields, Copilot will suggest similar patterns
```

#### Express Server Development

1. Navigate to `express-server/src/`
2. Make changes to JavaScript files
3. Watch the console for automatic restart messages
4. Test endpoints at http://localhost:8001

**Adding a New Route**:
```javascript
/**
 * Description of what this route does.
 * Copilot uses JSDoc comments for context.
 */
app.get('/new-route', (req, res) => {
    // Copilot will suggest implementation
});
```

**Adding Middleware**:
```javascript
/**
 * Middleware description
 * @param {Request} req - Express request
 * @param {Response} res - Express response
 * @param {NextFunction} next - Next middleware
 */
const customMiddleware = (req, res, next) => {
    // Copilot suggests middleware logic
};
```

## Code Style Guidelines

### Python (FastAPI)

- Use type hints for all function parameters and returns
- Follow PEP 8 style guide
- Add docstrings to all functions
- Use Pydantic models for data validation
- Keep routes thin, move logic to service functions

**Example**:
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    """User data model."""
    name: str
    email: str

@app.post("/users")
def create_user(user: User) -> dict:
    """
    Create a new user.
    
    Args:
        user: User object with name and email
        
    Returns:
        dict: Success message with user data
    """
    # Implementation
    return {"message": "User created", "data": user}
```

### JavaScript (Express)

- Use const/let instead of var
- Add JSDoc comments for functions
- Use async/await for asynchronous operations
- Follow Airbnb JavaScript Style Guide
- Use meaningful variable names

**Example**:
```javascript
/**
 * Create a new user
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 * @returns {Promise<void>}
 */
const createUser = async (req, res) => {
    try {
        const { name, email } = req.body;
        // Implementation
        res.json({ message: 'User created', data: { name, email } });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};
```

## Testing

### Python Tests

Use pytest for testing FastAPI endpoints:

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_endpoint():
    """Test description for Copilot."""
    response = client.get("/endpoint")
    assert response.status_code == 200
    # Copilot suggests more assertions
```

### JavaScript Tests

Use Jest for testing Express routes:

```javascript
const request = require('supertest');
const app = require('../src/index');

describe('GET /endpoint', () => {
    it('should return 200', async () => {
        const response = await request(app).get('/endpoint');
        expect(response.status).toBe(200);
        // Copilot suggests more expectations
    });
});
```

## Docker and Containerization

### Modifying Dockerfiles

When changing Docker configuration:

1. Update the relevant Dockerfile
2. Rebuild the container:
   ```bash
   docker compose up --build
   ```

### Adding New Dependencies

**Python**:
1. Add to `requirements.txt`
2. Rebuild container

**Node.js**:
1. Update `package.json`:
   ```bash
   cd express-server
   yarn add package-name
   ```
2. Rebuild container

## Common Patterns

### Error Handling (Python)

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Get item by ID with error handling."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

### Error Handling (Express)

```javascript
/**
 * Error handling middleware
 */
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});
```

### Async Operations (Python)

```python
@app.get("/async-endpoint")
async def async_operation():
    """Async endpoint for I/O operations."""
    result = await some_async_function()
    return result
```

### Async Operations (Express)

```javascript
/**
 * Async route handler
 */
app.get('/async-route', async (req, res, next) => {
    try {
        const result = await someAsyncOperation();
        res.json(result);
    } catch (error) {
        next(error);
    }
});
```

## Debugging

### Python Server

View logs:
```bash
docker compose logs -f python-server
```

Access container:
```bash
docker compose exec python-server /bin/bash
```

### Express Server

View logs:
```bash
docker compose logs -f express-server
```

Access container:
```bash
docker compose exec express-server /bin/sh
```

## GitHub Copilot Tips

### Write Better Comments

**Good**:
```python
# Create a function that calculates the average of a list of numbers,
# handling empty lists by returning 0
```

**Better**:
```python
# Calculate average of numbers in list
# Args: numbers (list of floats)
# Returns: float (average) or 0 if list is empty
# Example: calculate_average([1, 2, 3]) -> 2.0
```

### Use Descriptive Function Names

Copilot understands intent better with clear names:

```python
# Good
def get_user_by_email(email: str):
    pass

# Copilot will suggest appropriate implementation
```

### Leverage Context from Open Files

Keep related files open in tabs:
- Models when writing routes
- Tests when implementing features
- Related endpoints for consistent patterns

### Use Copilot Chat

Ask Copilot for help:
- "How do I add CORS to this Express server?"
- "Write tests for this FastAPI endpoint"
- "Explain this function"

## Pull Request Guidelines

1. **Branch Naming**: `feature/description` or `fix/description`
2. **Commit Messages**: Clear and descriptive
3. **Testing**: Include tests for new features
4. **Documentation**: Update relevant docs
5. **Comments**: Add comments for complex logic

## Resources

- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/)
- [Express.js Guide](https://expressjs.com/en/guide/routing.html)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Pydantic Models](https://docs.pydantic.dev/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## Getting Help

- Check existing documentation first
- Use Copilot Chat for quick questions
- Review ARCHITECTURE.md for system design
- Look at existing code patterns for examples
