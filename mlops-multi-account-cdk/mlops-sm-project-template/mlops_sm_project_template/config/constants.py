# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# SPDX-License-Identifier: MIT-0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

CODE_COMMIT_REPO_NAME = "mlops-sm-project-template"
PIPELINE_BRANCH = "main"

PIPELINE_ACCOUNT = "101186769107"  # account used to host the pipeline handling updates of this repository

DEV_ACCOUNT = "101186769107"  # account to host the service catalog template

PREPROD_ACCOUNT = ""  # account used to deploy the endpoint

PROD_ACCOUNT = ""  # account used to deploy the endpoint

DEFAULT_DEPLOYMENT_REGION = "us-east-1"
APP_PREFIX = "mlops-cdk"
