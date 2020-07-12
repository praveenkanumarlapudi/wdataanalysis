#!/bin/bash
# Bootstraps the EMR cluster 
# packages for use by PySpark.
set -e
cd /home/hadoop
aws s3 cp s3://pk-big-data-assessment/python/my-iris-env.zip /home/hadoop/my-iris-env.zip --region us-east-1
aws s3 cp s3://pk-big-data-assessment/config/spark-config.yml /home/hadoop/spark-config.yml --region us-east-1
unzip /home/hadoop/my-iris-env.zip
export PYSPARK_PYTHON=/home/hadoop/my-iris-env/bin/python
export PYSPARK_PYTHON_DRIVER=/home/hadoop/my-iris-env/bin/python
echo $PYSPARK_PYTHON
echo $PYSPARK_PYTHON_DRIVER
ls -lrt /home/hadoop/my-iris-env/bin/python
