import pyspark
import pandas as pd
from pyspark.sql import SparkSession

pd.read_csv('name_age.csv')
spark = SparkSession.builder.appName('Practice').getOrCreate()

df_pyspark = spark.read.csv('name_age.csv')
