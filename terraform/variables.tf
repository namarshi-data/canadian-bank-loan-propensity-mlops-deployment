variable "aws_region" {
  description = "AWS region for the container registry."
  type        = string
  default     = "ca-central-1"
}

variable "repository_name" {
  description = "ECR repository name for the Flask API image."
  type        = string
  default     = "bank-loan-propensity-api"
}
