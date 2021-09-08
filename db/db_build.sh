#!/bin/bash
cd "/home/minikube/postgres-dockerfile/db"
echo "changing image registry to minikube"

# changes build context to docker image registry
eval $(minikube docker-env)
echo "building postgres database"
docker build -t postgres-db:v1.0 .

echo "applying kubernetes manifest postgresdb"
kubectl apply -f ./config_map.yml
kubectl apply -f ./db_deploy.yml

echo "job completed"