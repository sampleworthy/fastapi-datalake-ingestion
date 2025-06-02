variable "resource_group_name" {
  type    = string
  default = "rg-fastapi-datalake"
}

variable "location" {
  type    = string
  default = "East US"
}

variable "storage_account_name" {
  type    = string
  default = "fastapidatalake01"
}

variable "file_system_name" {
  type    = string
  default = "raw-data"
}

variable "environment" {
  type    = string
  default = "dev"
}
