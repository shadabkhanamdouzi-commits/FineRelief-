#!/bin/bash

# FineRelief Quick Start Script

set -e

echo "🚀 FineRelief Quick Start"
echo "========================="

# Check requirements
echo ""
echo "📋 Checking requirements..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi
echo "✅ Docker found"

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi
echo "✅ Docker Compose found"

# Setup
echo ""
echo "📦 Setting up project..."

# Create .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env from template"
fi

# Build Docker images
echo ""
echo "🔨 Building Docker images..."
docker-compose build

# Start services
echo ""
echo "▶️ Starting services..."
docker-compose up -d

# Wait for services to be ready
echo ""
echo "⏳ Waiting for services to start..."
sleep 10

# Test backend
if curl -s http://localhost:8000/ > /dev/null; then
    echo "✅ Backend is running"
else
    echo "❌ Backend failed to start"
    docker-compose logs backend
    exit 1
fi

# Test frontend
if curl -s http://localhost:3000/ > /dev/null; then
    echo "✅ Frontend is running"
else
    echo "❌ Frontend failed to start"
    docker-compose logs frontend
    exit 1
fi

# Display info
echo ""
echo "🎉 FineRelief is ready!"
echo ""
echo "📍 Access points:"
echo "  Frontend: http://localhost:3000"
echo "  Backend:  http://localhost:8000"
echo "  API Docs: http://localhost:8000/docs"
echo ""
echo "📝 Useful commands:"
echo "  Logs:     docker-compose logs -f"
echo "  Stop:     docker-compose down"
echo "  Restart:  docker-compose restart"
echo ""
echo "📚 Documentation:"
echo "  Setup:     DEPLOYMENT.md"
echo "  API:       API_DOCS.md"
echo "  Troubleshoot: TROUBLESHOOTING.md"
echo ""
echo "Press Ctrl+C to stop services"
echo ""

# Show logs
docker-compose logs -f
