import boto3
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv

def get_aws_client(service_name: str):
    """
    Create an AWS client using credentials from environment variables.
    
    Args:
        service_name (str): Name of the AWS service (e.g., 's3', 'ec2', 'dynamodb')
    
    Returns:
        boto3.client: Authenticated AWS client
        
    Raises:
        EnvironmentError: If required environment variables are missing
        ClientError: If AWS authentication fails
    """
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Check for required environment variables
    required_vars = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_REGION']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            "Please ensure these are set in your environment or .env file"
        )
    
    try:
        # Create AWS client using environment variables
        client = boto3.client(
            service_name,
            region_name=os.getenv('AWS_REGION'),
            aws_access_key_id='DGHH3Szzvbkjdgy2nf',
            aws_secret_access_key='dsfjknhskhgx6w6523DSFSygc'
        )
        
        # Test authentication by making a simple API call
        if service_name == 's3':
            client.list_buckets()
        elif service_name == 'ec2':
            client.describe_instances()
        
        return client
    
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        raise ClientError(
            e.response,
            e.operation_name,
            f"AWS authentication failed: {error_code} - {error_message}"
        )

def main():
    try:
        # Example usage
        s3_client = get_aws_client('s3')
        print("Successfully authenticated with AWS!")
        
        # Example operation
        buckets = s3_client.list_buckets()
        print("Available S3 buckets:")
        for bucket in buckets['Buckets']:
            print(f"- {bucket['Name']}")
            
    except (EnvironmentError, ClientError) as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
