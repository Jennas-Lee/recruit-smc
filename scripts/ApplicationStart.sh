#!/bin/bash

docker run -itd -v /sock:/sock \
  -e PYTHONUNBUFFERED=$PYTHONUNBUFFERED \
  -e DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE \
  -e aws_s3_bucket=$aws_s3_bucket \
  -e static_cdn_link=$static_cdn_link \
  -e DJANGO_ENV=$DJANGO_ENV \
  -e DJANGO_READ_DATABASE_NAME=$DJANGO_READ_DATABASE_NAME \
  -e DJANGO_READ_DATABASE_USER=$DJANGO_READ_DATABASE_USER \
  -e DJANGO_READ_DATABASE_PASSWORD=$DJANGO_READ_DATABASE_PASSWORD \
  -e DJANGO_READ_DATABASE_HOST=$DJANGO_READ_DATABASE_HOST \
  -e DJANGO_READ_DATABASE_PORT=$DJANGO_READ_DATABASE_PORT \
  -e DJANGO_WRITE_DATABASE_NAME=$DJANGO_WRITE_DATABASE_NAME \
  -e DJANGO_WRITE_DATABASE_USER=$DJANGO_WRITE_DATABASE_USER \
  -e DJANGO_WRITE_DATABASE_PASSWORD=$DJANGO_WRITE_DATABASE_PASSWORD \
  -e DJANGO_WRITE_DATABASE_HOST=$DJANGO_WRITE_DATABASE_HOST \
  -e DJANGO_WRITE_DATABASE_PORT=$DJANGO_WRITE_DATABASE_PORT \
  -e AWS_ACCOUNT_ID=$AWS_ACCOUNT_ID \
  -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
  -e IMAGE_REPO_NAME=$IMAGE_REPO_NAME \
  --name django django:latest

docker run -itd -v /sock:/sock -p 80:80 --name nginx nginx:latest