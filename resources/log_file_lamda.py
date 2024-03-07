import json
import os
import boto3
from io import BytesIO
import gzip
from datetime import datetime
def handlerPost(event, context):
    bucket_name = os.environ.get('BUCKET')
    s3 = boto3.client('s3')

    file_name = 'log-file'+getMillisecondDate()+'.log'
    object_key = 'logs/'+file_name

    if 'body' in event:
        file_content = event['body']
        file_content_convert = json.dumps(file_content)
        try:
            s3.put_object(Body=file_content_convert,Bucket=bucket_name,Key=object_key)
            compressLogFileHanlder(event, context)
            return {
                    'statusCode': 200,
                    'body': json.dumps('Log file '+file_name+' processed and stored in bucket '+bucket_name)
            }
        except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    return {
                    'statusCode': 500,
                    'body': json.dumps('there is a problem in inserting the data to the bucket')
                    }

    else:
        return {
                'statusCode': 500,
                'body': json.dumps('There is no file in the body')
        }

def compressLogFileHanlder(event, context):
        bucket_name = os.environ.get('BUCKETCOMPRESS')
        file_name = 'log-file'+getMillisecondDate()+'.gz'
        compressed_file_key = 'logs/'+file_name
        s3 = boto3.client('s3')
        file_content = event['body']
        
        compressed = BytesIO()
        try:
            with gzip.GzipFile(fileobj=compressed, mode='w') as f:
                json_response = json.dumps(file_content)
                s3.put_object(Body=json_response.encode('utf-8'),Bucket=bucket_name,Key=compressed_file_key)

        except Exception as e:
           print(f"An error occurred while compressing the file: {str(e)}")
           
def getMillisecondDate():
    (dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
    dateMillisecond = "%s%03d" % (dt, int(micro) / 1000) 
    return dateMillisecond 