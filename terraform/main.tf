terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
  }
}

provider "docker" {
  registry_auth {
    address  = "registry-1.docker.io"
    username = var.docker_username
    password = var.docker_password
  }
}

variable "docker_username" {
  type      = string
  sensitive = true
  default   = "" # Leave empty here and set using TF_VAR_* env vars or tfvars file
}

variable "docker_password" {
  type      = string
  sensitive = true
  default   = ""
}

resource "docker_image" "app" {
  name         = "balqueez/simple-note-app:latest"
  keep_locally = true
  build {
    context    = "F:/Noteapp"
    dockerfile = "Dockerfile"
  
  }
}

resource "null_resource" "push_image" {
  depends_on = [docker_image.app]

  provisioner "local-exec" {
    command = "docker push balqueez/simple-note-app:latest"
}
}

resource "docker_container" "app_container" {
  name  = "simple-note-app"
  image = docker_image.app.name
  ports {
    internal = 5000
    external = 5000
  }
}
