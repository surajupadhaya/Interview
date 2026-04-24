# 1. Define the Provider
provider "aws" {
  region = "us-east-1"
}

#define params



# 2. Define the Resource
resource "aws_instance" "testvm" {
  # Use a standard Amazon Linux 2023 AMI (Verify ID for your region)
  ami           = "ami-051f8b2110b52e9f0" 
  instance_type = "t2.micro"

  tags = {
    Name = "hello"
  }
}