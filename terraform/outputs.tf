output "ecr_repository_url" {
  description = "Amazon ECR repository URL for the API image."
  value       = aws_ecr_repository.api.repository_url
}
