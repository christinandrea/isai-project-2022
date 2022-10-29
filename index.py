import boto
import boto3

bucket_name = "s3forkedaireka"

session = boto3.session.Session(profile_name="LabRole")
s3 = session.resource("s3")

