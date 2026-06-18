variable "aws_region" {
  description = "AWS region used for ECR and EKS resources."
  type        = string
  default     = "ca-central-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster."
  type        = string
  default     = "bank-loan-propensity-eks"
}

variable "cluster_version" {
  description = "Kubernetes version for EKS."
  type        = string
  default     = "1.30"
}

variable "ecr_repository_name" {
  description = "ECR repository name for the Flask API Docker image."
  type        = string
  default     = "bank-loan-propensity-api"
}

variable "vpc_id" {
  description = "Existing VPC ID for the EKS cluster."
  type        = string
}

variable "subnet_ids" {
  description = "Private subnet IDs for the EKS worker nodes."
  type        = list(string)
}

variable "node_instance_type" {
  description = "EC2 instance type for EKS managed node group."
  type        = string
  default     = "t3.medium"
}
