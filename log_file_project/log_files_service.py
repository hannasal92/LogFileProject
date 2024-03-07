import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)

class LogFileService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        bucket = s3.Bucket(self, "LogFileStore")

        handler = lambda_.Function(self, "LogFileHandler",
                    runtime=lambda_.Runtime.PYTHON_3_12,
                    code=lambda_.Code.from_asset("resources"),
                    handler="log_file_lamda.handlerPost",
                    environment=dict(
                    BUCKET=bucket.bucket_name)
                    )

        bucket.grant_read_write(handler)

        api = apigateway.RestApi(self, "logFile-api",
                  rest_api_name="LogFile Service",
                  description="This service serves logFile.")

        get_logfile_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("POST", get_logfile_integration)   # GET /