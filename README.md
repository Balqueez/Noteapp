# Simple Note App Deployment using Docker and Terraform

This project demonstrates how to containerize a Python Flask app and manage its lifecycle using Docker and Terraform.

## Prerequisites

- Docker installed and configured
- Terraform installed
- A Docker Hub account
- A Python Flask application (e.g., `app.py`) and a `Dockerfile`

---

### Terraform Workflow:

## Initialize Terraform

    terraform init 
## Define Resources (main.tf)

 - docker_image: Builds the Docker image
 - docker_container: Runs the container
 - null_resource: Pushes image

## Apply the Infrastructure

   terraform apply
   
## Destroy the Infrastructure

  terraform destroy




