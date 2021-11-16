#!/bin/bash

bash /etc/profile.d/codedeploy.sh
docker login -u AWS -p $(aws ecr get-login-password --region $AWS_DEFAULT_REGION) $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com