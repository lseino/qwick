# Introduction
This project will deploy a python data scraping application ontop of minikube kubernetes cluster running on an amazon ec2 ubuntu instance. This app will store its data into a postgres database running on the same minikube cluster.

# Directory Structure
* ansible 
      * roles
         * deploy
         * docker
         * kubectl
         * minikube
      * terraform
      * ansible.cfg # config file
      * inventory.ini # inventory file
      * playbook.yml
* db
* scraper
* README.md

# Requirements
   * An existing AWS Account (edit ~/.aws/credentials with access key id and pass for default profile)
   * existing AWS Key Pair
   * Python3
   * Ansible
   * Git
   * Terraform

# Getting Started

clone repo "https://github.com/lseino/qwick.git" & cd qwick

  ## Setting up the instance with terraform
   * cd into the terraform directory
   * edit the ec2.tf file and add your keypair name ~ key_name={keypair_name}
   RUN 
   * "terraform init && terraform plan" .. this plan should bring up 1 ec2 instance
   * "terraform apply"  if all looks good
   * This should OUTPUT the public_ip of the ec2 instance created, copy this as it will be needed in the ansible section

  ## Deploying the python Application with Ansible
   * cd into the ansible directory
   * edit the inventory.ini file with the public ip of the ec2 instance & location of your aws key_pair
        * ansible_host={{ public_ip from terrafrom here}}
        * ansible_ssh_private_key_file={{ here enter path to ec2 key_pair file}}
   * make sure port 22 is open on the security group attached to the instance
   * run "ansible-playbook -i ./inventory.ini playbook.yml"
   
# To verify application is running
   * SSH into the ec2 instance using the private key file. "ssh -i "path/to/keyfile" ubuntu@{public_ip}"
   * "su minikube" & enter minikube password
   * "kubectl get pods" you should see 2 pods running (python_scraper & postgres)
   * "kubectl logs {scraper-py** pod_name} "you should see 20 records inserted in the logs
  
   # To access postgres database to verify 
   * Run "sudo apt install postgresql-client-*"
   * "kubectl exec -it {postgre**pod_name} -- bash "  opens up postgres container
   * "psql -U python scraper"  opens database
   * "select * from scraper_data;" should see all 20 records
 

# To Clean up 
cd into /ansible/terraform and run "terraform destroy"
