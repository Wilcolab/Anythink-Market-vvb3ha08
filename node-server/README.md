# Anythink Market Node.js Server

This project is a simple Node.js server built with Express. It listens on port 8001 and is set up to automatically restart on code changes using Nodemon.

## Project Structure

```
node-server
├── src
│   ├── app.js          # Entry point of the application
│   └── types
│       └── index.js    # Type definitions (currently empty)
├── package.json         # Project configuration and dependencies
├── Dockerfile           # Instructions to build the Docker image
├── nodemon.json         # Configuration for Nodemon
└── README.md            # Project documentation
```

## Getting Started

### Prerequisites

- Node.js and npm installed on your machine.
- Yarn package manager installed.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Wilcolab/Anythink-Market-vvb3ha08.git
   cd Anythink-Market-vvb3ha08/node-server
   ```

2. Install dependencies:
   ```
   yarn install
   ```

### Running the Server

To start the server, use the following command:

```
yarn start
```

The server will be running on `http://localhost:8001`.

### Docker

To build and run the server using Docker, use the following commands:

1. Build the Docker image:
   ```
   docker build -t anythink-market .
   ```

2. Run the Docker container:
   ```
   docker run -p 8001:8001 anythink-market
   ```

The server will be accessible at `http://localhost:8001` from your host machine.

### License

This project is licensed under the MIT License. See the LICENSE file for details.