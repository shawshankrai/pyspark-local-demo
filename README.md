# pyspark-local-demo

Add HADHOOP_HOME and %HADOOP_HOME%\bin with winutils.exe and hadoop.dll in windows system environment

Set Environment variables for:

export ENVIRON=PROD
export SRC_DIR=s3://emr-shashank-iam/prd/landing/ghactivity/
export SRC_FILE_FORMAT=json
export TGT_DIR=s3://emr-shashank-iam/prd/raw/ghactivity/
export SRC_FILE_PATTERN=2021-01-13

Run App.py main method

To Zip files in powershell use:
Compress-Archive -Path processor\process.py, reader\read.py, writer\write.py, util\util.py .\demo-pyspark-code

Save Zip and App in same folder on cluster for spark-submit

Configuration for cluster mode:
--conf "spark.yarn.appMasterEnv.ENVIRON=PROD"
--conf "spark.yarn.appMasterEnv.SRC_DIR=s3://emr-shashank-iam/prd/landing/ghactivity/"
--conf "spark.yarn.appMasterEnv.SRC_FILE_FORMAT=json"
--conf "spark.yarn.appMasterEnv.TGT_DIR=s3://emr-shashank-iam/prd/raw/ghactivity/"
--conf "spark.yarn.appMasterEnv.SRC_FILE_PATTERN=2021-01-13"
--py-files s3://emr-shashank-iam/zip/demo-pyspark-code.zip

![image](https://user-images.githubusercontent.com/96636835/177211067-0f19e793-b4f9-4454-8b5a-46d8855d26ae.png)


Spark Submit Cluster:
![image](https://user-images.githubusercontent.com/96636835/177211156-655f6526-2806-4387-8a82-320b160ee47b.png)

Spark Submit Client:
![image](https://user-images.githubusercontent.com/96636835/177211333-0a275626-f2ce-458a-bada-ffbc760bc21e.png)
