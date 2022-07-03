# pyspark-local-demo

Add HADHOOP_HOME and %HADOOP_HOME%\bin with winutils.exe and hadoop.dll in windows system environment

Set Environment variables for:

* $ export ENVIRON=PROD
* $ export SRC_DIR=s3://emr-shashank-iam/prd/landing/ghactivity/
* $ export SRC_FILE_FORMAT=json
* $ export TGT_DIR=s3://emr-shashank-iam/prd/raw/ghactivity/

Run App.py main method

To Zip files in powershell use:
Compress-Archive -Path processor\process.py, reader\read.py, writer\write.py, util\util.py .\demo-pyspark-code

Save Zip and App in same folder on cluster for spark-submit
