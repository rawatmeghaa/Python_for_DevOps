# Python DevOps Learning Repository

A comprehensive collection of Python scripts and tools for DevOps automation, system monitoring, cloud operations, and infrastructure management.


## 🚀 Features

### System Monitoring & Utilities
- **Cross-platform system information** - CPU, memory, disk usage monitoring
- **Automated backup system** - Local file backup with timestamp
- **Date/time utilities** - System date and time operations

### Cloud Operations (AWS)
- **S3 Bucket Management** - Create, list, and delete S3 buckets
- **File Upload/Backup** - Automated backup to AWS S3
- **Resource Cleanup** - Automated bucket and object deletion

### Infrastructure as Code
- **Terraform Automation** - Python wrapper for Terraform operations
- **EC2 Instance Provisioning** - Automated AWS EC2 deployment
- **Security Group Configuration** - Network security automation

### Web Application
- **Real-time System Monitoring** - Flask web app for system metrics
- **CPU & Memory Alerts** - Threshold-based alerting system
- **Containerized Deployment** - Docker and Kubernetes ready

## 🛠️ Prerequisites

### Python Dependencies
```bash
pip install boto3 psutil flask


## AWS S3 Operations
import boto3
from backup_s3 import create_bucket, upload_object

s3 = boto3.resource("s3")
create_bucket(s3, "my-backup-bucket", "us-east-1")





