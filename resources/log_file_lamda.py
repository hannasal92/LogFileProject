import json
import os
import boto3
import gzip
from datetime import datetime
def handleLogFile(event, context):
    bucket_name = os.environ.get('BUCKET')
    s3 = boto3.client('s3')

    file_name = 'log-file'+getMillisecondDate()+'.log'
    object_key = 'logs/'+file_name

    if 'body' in event:
        file_content = event['body']
        file_content_convert = json.dumps(file_content)
        try:
            s3.put_object(Body=file_content_convert,Bucket=bucket_name,Key=object_key)
            compressResponse = compressLogFileHanlder(event, context)
            return {
                    'statusCode': 200,
                    'body': json.dumps('Log file '+file_name+' processed and stored in bucket '+bucket_name + " " + compressResponse)
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
    
    file_content = event['body']
    log_data = json.dumps(file_content)
    file_name = 'log-file'+getMillisecondDate()
    
    # Compress the log data using gzip
    compressed_data = gzip.compress(log_data.encode())
    
    # Define the file key for the compressed file
    compressed_file_key = f"{file_name}.gz"
    
    # Upload the compressed file to S3
    s3 = boto3.client('s3')
    try:
        s3.put_object(Body=compressed_data, Bucket=bucket_name, Key=compressed_file_key)
        return 'Log file '+compressed_file_key+' compressed and stored in bucket '+bucket_name
    except Exception as e:
        return f'Error compressing and uploading log file: {str(e)}'

           
def getMillisecondDate():
    (dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
    dateMillisecond = "%s%03d" % (dt, int(micro) / 1000) 
    return dateMillisecond 