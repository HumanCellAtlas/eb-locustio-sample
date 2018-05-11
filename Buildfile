# Copyright 2015-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#    http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.

#buildvenv: python36 -m pip install --user -r requirements.txt
get_secrets: aws secretsmanager get-secret-value --secret-id ${DSS_SECRETS_STORE}/${DSS_DEPLOYMENT_STAGE}/gcp-credentials.json | jq -r .SecretString > ~/gcp-credentials.json
build: ./build.rb
