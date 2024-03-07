import aws_cdk as core
import aws_cdk.assertions as assertions

from log_file_project.log_file_project_stack import LogFileProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in log_file_project/log_file_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LogFileProjectStack(app, "log-file-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
