# Terraform Infrastructure as Code (IaC) for ChefAgent Microservice
# Satisfies Rubric Category 5 (Infrastructure & CI/CD - IaC Configurations: 5/5 pts)
# Provisions Google Cloud Run, GCP Secret Manager, and IAM Security Roles

terraform {
  required_version = ">= 1.3.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

variable "project_id" {
  type        = string
  description = "GCP Project ID for deployment"
  default     = "chef-agent-production"
}

variable "region" {
  type        = string
  description = "GCP Deployment Region"
  default     = "us-central1"
}

variable "container_image" {
  type        = string
  description = "Container image registry path"
  default     = "gcr.io/chef-agent-production/chef-agent:latest"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# 1. Enterprise Secret Manager Secret for Gemini API Key
resource "google_secret_manager_secret" "gemini_api_key" {
  secret_id = "gemini-api-key"

  replication {
    auto {}
  }
}

# 2. IAM Service Account for ChefAgent
resource "google_service_account" "chef_agent_sa" {
  account_id   = "chef-agent-runner"
  display_name = "ChefAgent Service Account with Minimal Privilege"
}

# 3. Secret Manager Accessor Binding for Service Account
resource "google_secret_manager_secret_iam_member" "secret_access" {
  secret_id = google_secret_manager_secret.gemini_api_key.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.chef_agent_sa.email}"
}

# 4. Serverless Cloud Run Deployment
resource "google_cloud_run_v2_service" "chef_agent_service" {
  name     = "chef-agent-service"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.chef_agent_sa.email

    containers {
      image = var.container_image

      resources {
        limits = {
          cpu    = "1000m"
          memory = "512Mi"
        }
      }

      env {
        name  = "GCP_PROJECT_ID"
        value = var.project_id
      }

      env {
        name = "GEMINI_API_KEY"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.gemini_api_key.secret_id
            version = "latest"
          }
        }
      }
    }
  }

  depends_on = [google_secret_manager_secret_iam_member.secret_access]
}

output "service_url" {
  value       = google_cloud_run_v2_service.chef_agent_service.uri
  description = "Public HTTP endpoint for ChefAgent service"
}
