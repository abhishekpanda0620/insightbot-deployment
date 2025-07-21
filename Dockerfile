# === Stage 1: Build stage ===
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /install

# Install pip dependencies system-wide
COPY app/requirements.txt .

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential curl && \
    pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# === Stage 2: Runtime stage ===
FROM python:3.12-slim

# Create non-root user
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup insightbot

WORKDIR /app

# Install curl for in-container testing
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY app/ .

# Set permissions
RUN chown -R insightbot:appgroup /app

# Switch to non-root user
USER insightbot

# Expose port
EXPOSE 8080

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
