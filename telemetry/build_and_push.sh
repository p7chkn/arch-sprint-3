#!/bin/bash

# Ensure required environment variables are set
if [ -z "$GITHUB_USERNAME" ] || [ -z "$GITHUB_PAT" ]; then
  echo "Error: GITHUB_USERNAME and GITHUB_PAT environment variables must be set."
  exit 1
fi

# Set variables
USERNAME="$GITHUB_USERNAME"
IMAGE_NAME="telemetry-service"
TAG="latest"

# Login to GitHub Container Registry
echo $GITHUB_PAT | docker login ghcr.io -u $USERNAME --password-stdin

# Build the Docker image
docker build -t ghcr.io/$USERNAME/$IMAGE_NAME:$TAG .

# Push the Docker image to GitHub Container Registry
docker push ghcr.io/$USERNAME/$IMAGE_NAME:$TAG