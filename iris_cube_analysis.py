from __future__ import print_function
import sys
import iris
import datetime
import logging
import boto3
import os
from operator import add
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *


def extract_dew_point(fname):
	# cube_1 = iris.load(fname,'dew_point_temperature')     -- returns cubeList
	try:
		dew_cube = iris.load_cube(fname,'dew_point_temperature') 
		return [mini_cube for mini_cube in (dew_cube.slices(['grid_longitude']))]
	except:
		logging.error('Did not find dew_point_temperature variable in Cube aborting ....')

def process_slice(cube_slice):
	return [mini_cube for mini_cube in (cube_slice.slices([]))]

def scalar_extract(scalar_cube):
	result=[]
	for i in range(len(scalar_cube)):
		time = scalar_cube[i].coords('time')[0]
		time_str = str(time.units.num2date(time.points[0]))
		lat = scalar_cube[i].coord('grid_latitude')[0].points[0].tolist()
		lon = scalar_cube[i].coord('grid_longitude')[0].points[0].tolist()
		realization = scalar_cube[i].coord('realization').points[0].tolist()
		forecast_period = scalar_cube[i].coord('forecast_period').points[0].tolist()
		forecast_reference_time = scalar_cube[i].coord('forecast_reference_time')
		forecast_reference_time_str = str(forecast_reference_time.units.num2date(forecast_reference_time.points[0]))
		result.append(Row(time_str, lat, lon, realization, forecast_period, forecast_reference_time_str))
	return result

def copy_to_local(s3_in, local_dir):
	s3 = boto3.client('s3')
	s3.download_file(s3_in.split("/")[2], s3_in.split("/")[3], local_dir+ 'copiedFromS3.nc')
	logging.info('Copying '+s3_in.split("/")[2]+'/'+s3_in.split("/")[3]+'to local'+local_dir+ 'copiedFromS3.nc')
	logging.info('list dir' +str(os.listdir(local_dir)))
	return local_dir+ 'copiedFromS3.nc'
	
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: s3://<nc_file> s3://<output> objectname", file=sys.stderr)
        sys.exit(-1)
    
    local_dir = '/mnt1/'
    sc =SparkContext()
    spark = SparkSession\
	        .builder\
	        .appName("Weather data analysis")\
	        .getOrCreate()	
    dew_temp_schema = StructType(\
	[StructField('recorded_time', StringType()),\
	StructField('grid_latitude',FloatType()),\
	StructField('grid_longitude',FloatType()),\
	StructField('realization',IntegerType()),\
	StructField('forecast_period',FloatType()),\
	StructField('forecast_reference_time_str',StringType())]\
	)
    
    #:local_file = copy_to_local(sys.argv[1], local_dir)
    dew_point_temp_rdd = sc.parallelize(extract_dew_point('/mnt1/'+sys.argv[1].split("/")[3]), 128)
    flatten_cubes = dew_point_temp_rdd.map(lambda cube_slice: process_slice(cube_slice)).flatMap(lambda mini_cubes:scalar_extract(mini_cubes))
    dew_temp_data_df = spark.createDataFrame(flatten_cubes, dew_temp_schema)
    dew_temp_data_df.write.parquet(sys.argv[2])
    spark.stop()
