import boto3

s3 = boto3.resource("s3")

def bucket_list(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


bucket_list(s3)

def create_bucket(s3,bucket_name):
    s3.create_bucket(Bucket = bucket_name,
                     CreateBucketConfiguration={
                    'LocationConstraint':'ap-south-1'
                     },)
    print("Bucket created successfully")


# create_bucket(s3 , "mmznxs-122222222")
bucket_list(s3);

def delete_bucket(s3 , bucket_name):
    bucket=s3.Bucket(bucket_name)
    bucket.objects.all().delete()
    bucket.delete()

# delete_bucket(s3 , "mmznxs-122222222")
bucket_list(s3)