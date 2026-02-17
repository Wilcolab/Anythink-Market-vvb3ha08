# Express Server Project

This is a simple Express server project that listens on port 8001. The server is set up to automatically reload using Nodemon during development.

## Project Structure

```
express-server
├── src
│   └── index.js        # Entry point of the application
├── package.json        # Configuration file for npm
├── .gitignore          # Files and directories to be ignored by Git
├── Dockerfile          # Instructions for building a Docker image
└── README.md           # Documentation for the project
```

## Getting Started

To get started with this project, follow the instructions below:

### Prerequisites

Make sure you have Node.js and Yarn installed on your machine.

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd express-server
   ```

2. Install the dependencies:
   ```
   yarn install
   ```

### Running the Server

To start the server with automatic reloading, use the following command:

```
yarn start
```

The server will be running on [http://localhost:8001](http://localhost:8001).

### Docker

To build and run the Docker container, use the following commands:

1. Build the Docker image:
   ```
   docker build -t express-server .
   ```

2. Run the Docker container:
   ```
   docker run -p 8001:8001 express-server
   ```

Now the server should be accessible on [http://localhost:8001](http://localhost:8001) from your host machine.