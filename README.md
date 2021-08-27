# THE FOLLOWING REPO

## DB Directory
 * The db directory contains a dockerfile to create a postgres instance which will be used to load scraped data.

## Scraper directory
 * The scraper directory contains a Dockerfile  that will build a python image. 
 * it also contains a python script that when runned will scrape some information from wikipedia about IFPA data. 
 * It will store that information in the postgres database running in the other docker container

## Ansible directory
* Contains YAML files required for deploying DB and python images
* Ansible playbook for installing Docker, Minikube, and kubectl that creates a deployment in minikube with all of the containers running

