
# Welcome to your CDK Python project!

we should install npm , pip and aws cli 

to install aws cli => npm install -g aws-cdk

first step 
Create an AWS CDK app
mkdir LogFileProject
cd LogFileProject
cdk init --language python
source .venv/bin/activate
pip install -r requirements.txt

creating resource folder and add log_file_lamda.py to add all the lamda function inside it by running mkdir resources

we should install boto3 by pip install boto3 so we can access s3 (buckets)

adding log_files_service.py to create the buckets and the api gateway and handling the lamda functions 

after we finishing everything we should export the AWS_ACCESS_KEY_ID , AWS_SECRET_ACCESS_KEY , AWS_DEFAULT_REGION by these commands 

export AWS_ACCESS_KEY_ID=XXXXXXXXXXXX
export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXX
export AWS_DEFAULT_REGION=xxxxxx

we get the values in the aws account security credentials

run cdk synth to be sure the app runs and synthesizes a stack

Deploy and test the app
cdk bootstrap aws://ACCOUNT-NUMBER/REGION -> this creates a staging bucket that the AWS CDK uses to deploy stacks containing assets
cdk deploy

If the deployment succeeds the url appears  -> https://GUID.execute-api-REGION.amazonaws.com/prod/ ;  -> https://meen9hbh0b.execute-api.eu-west-3.amazonaws.com/prod/



This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
