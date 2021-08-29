# Directory Description

## DB Directory
 * The db directory contains a dockerfile to create a postgres instance which will be used to load scraped data.

## Scraper directory
 * The scraper directory contains a Dockerfile  that will build a python image. 
 * it also contains a python script that when runned will scrape some information from wikipedia about IFPA data. 
 * It will store that information in the postgres database running in the other docker container

## Ansible directory
* Contains the following roles that will handle the install of each service
### build_images
   * build postgres & python dockerfiles into respective images
### deploy images
   * contains ansible roles for deploying postgres & python images to minikube
   #### The template folder contains 
   * scraper_deploy.yml 
   * db_deploy.yml statefulset file
   * config maps with db credentials
### docker
   * contains ansible role for deploying docker to local machine
### kubectl
   * contains ansible role for deploying kubectl to local machine
### minikube
   * contains ansible role for deploying minikube to local machine

## k8 Files directory
 * Contains config_map yaml deploy file
 * postgres db statefulset yaml deploy file
 * python web scraper yaml deploy file


# How to run this Repo
## todo
