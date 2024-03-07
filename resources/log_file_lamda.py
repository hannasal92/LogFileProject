import json
import os
import boto3

def handlerPost(event, context):
    bucket_name = os.environ.get('BUCKET')
    object_key = 'logs/log-file.txt'
    s3 = boto3.client('s3')

    if 'body' in event:
        file_content = event['body']
        file_content_convert = json.dumps(file_content)
        try:
            s3.put_object(Body=file_content_convert,Bucket=bucket_name,Key=object_key)
            return {
                    'statusCode': 200,
                    'body': json.dumps('Log file processed and stored in bucket .'+bucket_name)
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