#!/bin/bash

# This script builds and pushes postgres scraper image into minikube docker registry
echo "changing image registry to minikube"
cd "/home/minikube/scraper-dockerfile/scraper"

# changing build environment to minikube registry
eval $(minikube docker-env)

echo "building python scraper application"
docker build -t python-scraper:v1.0 .

kubectl apply -f ./scraper_deploy.yml
echo "job completed"