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

locust36: pip-3.6 install locustio==0.8.1 gevent>=1.2.2 pyzmq==16.0.3
hca: pip-3.6 install git+git://github.com/HumanCellAtlas/dcp-cli@tsmith-load-testing#egg=hca
pyjsongen: pip-3.6 install git+git://github.com/HumanCellAtlas/dcp-pyjsongen@master#egg=pyjsongen
set_secret: python36 ./set_secret.py
build: ./build.rb
