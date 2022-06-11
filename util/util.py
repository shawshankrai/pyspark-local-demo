from pyspark.sql import SparkSession


def get_spark_session(env, app_name):
    if env == "DEV":
        spark = SparkSession.builder \
            .master('local') \
            .appName(app_name). \
            getOrCreate()
        spark_context = spark.sparkContext
        spark_context.setLogLevel("WARN")
        return spark
    elif env == 'PROD':
        spark = SparkSession.builder \
            .master('yarn') \
            .appName(app_name). \
            getOrCreate()
        spark_context = spark.sparkContext
        spark_context.setLogLevel("WARN")
        return spark

