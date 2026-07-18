#!/bin/bash

# FineRelief Docker Quick Start

echo "🚀 Starting FineRelief Docker containers..."
docker-compose up

echo ""
echo "✅ Services running:"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop services"
