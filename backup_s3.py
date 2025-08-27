import boto3

s3=boto3.resource("s3")

bucket_name="adddddddddd-1245666"
region="ap-south-1"

def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


show_bucket(s3)



# create bucket

def create_bucket(s3  , bucket_name , region):
    s3.create_bucket(Bucket= bucket_name , 
                     CreateBucketConfiguration={'LocationConstraint':region}
     )
    print('Bucket created successfully')

create_bucket(s3 , bucket_name , region);
show_bucket(s3)


def upload_object(s3 , file_name , bucket_name , key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name , Body=data)
    print("backup uploaded successfully")


file_name= r"C:\Users\Megha.rawat\Downloads\MEGHA\PROJECT\PYTHON\backups\backup2025-08-27.zip"

upload_object(s3 , file_name, bucket_name , "my-object.zip")



# def delete_bucket (s3 , bucket_name):
#     Bucket=s3.Bucket(bucket_name)
#     Bucket.objects.all().delete()
#     Bucket.delete()
#     print("Bucket deleted successfully")


# delete_bucket(s3 , bucket_name)
