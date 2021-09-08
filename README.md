# Introduction

This project deploys a python data scraping application in minikube kubernetes cluster running on an amazon ubuntu ec2. This app will store its data in a postgres database running on the same minikube cluster.

# Directory Structure

```bash
├── README.md
├── ansible
│   ├── ansible.cfg
│   ├── inventory.ini
│   ├── playbook.yml
│   ├── roles
│   │   ├── deploy
│   │   │   ├── defaults
│   │   │   │   └── main.yml
│   │   │   ├── tasks
│   │   │   │   ├── build_db.yml
│   │   │   │   ├── build_scraper.yml
│   │   │   │   └── main.yml
│   │   │   └── templates
│   │   ├── docker
│   │   │   ├── defaults
│   │   │   │   └── main.yml
│   │   │   └── tasks
│   │   │       └── main.yml
│   │   ├── kubectl
│   │   │   ├── defaults
│   │   │   │   └── main.yml
│   │   │   ├── tasks
│   │   │   │   └── main.yml
│   │   │   └── vars
│   │   │       └── main.yml
│   │   └── minikube
│   │       ├── defaults
│   │       │   └── main.yml
│   │       ├── tasks
│   │       │   ├── install_minikube.yml
│   │       │   ├── install_pkg_ubuntu.yml
│   │       │   ├── main.yml
│   │       │   └── user_minikube.yml
│   │       └── templates
│   │           └── minikube.service.j2
│   └── terraform
│       ├── ec2.tf
│       └── provider.tf
├── db
│   ├── Dockerfile
│   ├── config_map.yml
│   ├── db_build.sh
│   └── db_deploy.yml
└── scraper
    ├── Dockerfile
    ├── requirements.txt
    ├── scraper.py
    ├── scraper_build.sh
    └── scraper_deploy.yml
    
   ```

# Requirements

   * Basic ubuntu linux, git & kubernetes knowledge
   * An existing AWS Account (edit ~/.aws/credentials with access key id and pass for default profile)
   * existing AWS Key Pair
   * Python3
   * Ansible
   * Git
   * Terraform

# Getting Started

## Clone Repo 
```git clone https://github.com/lseino/qwick.git```
```cd qwick```

  ## Setting up the instance with terraform

   * ```cd terraform``` 
   * Edit the ec2.tf file to add your keypair name
      *  ```key_name={keypair_name}``` 
   * RUN  ```terraform init && terraform plan```  This plan should bring up 1 ec2 instance
   * "```terraform apply```"  if all looks good
   * Once complete a ```public_ip``` of the ec2 instance will be printed om console, copy this as it will be needed in the ansible section

  ## Deploying the python Application with Ansible

   * cd into ansible directory
   * edit **inventory.ini** file with the public ip of the ec2 instance & path to aws key_pair
   
         *  ```ansible_host={{ terraform:public:ip }}```
         *  ``` ansible_ssh_private_key_file={{ path/ec2_key_pair/file}}```

   * **Make sure *port 22* is open on the security group attached to the instance**
   * run ```ansible-playbook -i ./inventory.ini playbook.yml``` takes about **5 mins** to run
   
# To verify application is running
   * SSH into the ec2 instance using the private key ``ssh -i "path/to/keyfile" ubuntu@{public_ip}``
   * switch to minikube user ``su minikube`` & enter minikube password(default="testqwick").
   * run ```kubectl get pods``` you should see 2 pods running (python_scraper & postgres)
      * The scraper is in crashloop mood because the application has completed & terminated
   * ```kubectl logs {scraper-py** pod_name}``` you should see 20 records inserted in database
  
   # To access postgres database to verify 
   * Run ```sudo apt install postgresql-client-*```
   * ```kubectl exec -it {postgre**pod_name} -- bash```  opens up postgres container
   * ```psql -U python scraper```  opens database
   * ```select * from scraper_data;``` should see all 20 records
   * quit ```ctrl+d```
   * ```exit```
 

# To Clean up 
* ```cd  /ansible/terraform```
* ```terraform destroy```
