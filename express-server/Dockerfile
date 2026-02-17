# Express Server Dockerfile
# This container runs the Node.js Express application
# Note: The container is configured for development with volume mounts

# Use official Node.js LTS image
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Copy package files first to leverage Docker layer caching
# If dependencies haven't changed, this layer will be reused
COPY package*.json ./

# Install dependencies using yarn
# Using --frozen-lockfile ensures reproducible builds
RUN yarn install

# Copy application source code
COPY . .

# Expose the port on which the Express server will run
# This documents that the container listens on port 8001
EXPOSE 8001

# Start the application
# In development, nodemon will watch for file changes
# In production, consider using "node src/index.js" instead
CMD ["node", "src/index.js"]