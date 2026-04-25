variable "projectID" {
  type        = string
  description = "The project ID"

  validation {
    condition     = contains(["suruterraformproj"], var.projectID)
    error_message = "Not the correct ID"
  }
}
variable "machine_type" {
  type    = string
  default = "e2-micro"
}

variable "region" {
  type        = string
  description = "in which region "
}
variable "location" {
  type        = string
  description = "in which zone"
}
variable "env" {
  type        = string
  default     = "development"
  description = "Which Environment"

  validation {
    condition     = contains(["development", "SIT", "DT", "Prod"], var.env)
    error_message = "Enter correct setup type"
  }
}
