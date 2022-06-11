import os

from processor.process import transform
from util.util import get_spark_session
from reader.read import from_files
from writer.write import to_files


def main():
    env = os.environ.get("ENVIRON")
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-*'
    src_file_format = 'json'
    tgt_dir = os.environ.get('TGT_DIR')
    tgt_file_format = 'parquet'
    spark = get_spark_session(env, "pyspark_demo")

    dataframe = from_files(spark, src_dir, src_file_pattern, src_file_format)
    transformed_df = transform(dataframe).select('repo.*', 'year', 'month', 'day')

    to_files(transformed_df, tgt_dir, tgt_file_format)


if __name__ == '__main__':
    main()
