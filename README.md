# pyspark-local-demo

Add HADHOOP_HOME and %HADOOP_HOME%\bin with winutils.exe and hadoop.dll in windows system environment

Set Environment variables for:
src_dir = os.environ.get('SRC_DIR')
src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-*'
tgt_dir = os.environ.get('TGT_DIR')

Run App.py main method

To Zip files in powershell use:
Compress-Archive -Path processor\process.py, reader\read.py, writer\write.py, util\util.py .\demo-pyspark-code

Save Zip and App in same folder on cluster for spark-submit
