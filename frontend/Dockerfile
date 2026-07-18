FROM node:20-alpine

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy application
COPY . .

# Build application
RUN npm run build

# Serve with lightweight server
FROM node:20-alpine
RUN npm install -g serve
WORKDIR /app
COPY --from=0 /app/dist ./dist

EXPOSE 3000

CMD ["serve", "-s", "dist", "-l", "3000"]
