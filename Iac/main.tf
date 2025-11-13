# main.tf

provider "aws" {
  region = "us-east-1"
}

# HIGH #2: SSH open to the world
resource "aws_security_group" "demo_sg" {
  name        = "demo-sg"
  description = "Security group with wide-open SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # HIGH: SSH open to the world
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# LOW #2: Publicly readable S3 bucket
resource "aws_s3_bucket" "demo_bucket" {
  bucket = "my-demo-bucket-123456"

  # LOW: public-read is usually flagged as weak / misconfigured
  acl = "public-read"
}
