#!/usr/bin/env python3
"""
Author  : Prathima R
Title   : AWS S3 File Upload Script
Purpose : Upload a local file to an AWS S3 bucket using boto3.
Date    : 2025-11-03
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

# Function: Upload a file from local system (EC2 or local machine) to an AWS S3 bucket
def upload_to_aws(local_file, bucket, s3_file):
    """
    Uploads a file to AWS S3 bucket.
    Parameters:
        local_file (str): Path of the file to upload.
        bucket (str): Name of the target S3 bucket.
        s3_file (str): Key name (file name) for the uploaded object in S3.
    Returns:
        True if upload succeeded, False otherwise.
    """

    # Create an S3 client using boto3
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(local_file, bucket, s3_file)
        print(f"✅ Upload Successful: {local_file} → s3://{bucket}/{s3_file}")
        return True

    # Handle missing file error
    except FileNotFoundError:
        print(f"❌ The file '{local_file}' was not found.")
        return False

    # Handle missing AWS credentials
    except NoCredentialsError:
        print("❌ AWS credentials not available. Run 'aws configure' first.")
        return False

    # Handle any other AWS client errors
    except ClientError as e:
        print(f"❌ AWS Client Error: {e}")
        return False


# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":

    # Example local file to upload
    local_file = "demo.txt"

    # Example S3 bucket name (change to your own bucket)
    bucket_name = "prathima-upload-demo"

    # S3 key name (object name inside the bucket)
    s3_file_name = os.path.basename(local_file)

    # Check if file exists locally
    if os.path.exists(local_file):
        upload_to_aws(local_file, bucket_name, s3_file_name)
    else:
        print(f"❌ Local file not found: {local_file}")
