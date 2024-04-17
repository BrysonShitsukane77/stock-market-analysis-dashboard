variable "credentials" {
  description = "My Credentials"
  default     = "~/.config/gcloud/application_default_credentials.json"
  #default     = "~/.gc/my-creds.json"
  #default     = "<Path to your Service Account json file>"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "verdant-legacy-414217"
}

variable "region" {
  description = "Region for GCP resources"
  #Update the below to your desired region
  default = "EU"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default = "stock_prices_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "verdant-legacy-414217-stock-prices-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}