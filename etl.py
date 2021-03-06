from datetime import datetime # The datetime module supplies classes for manipulating dates and times
from pyspark.sql import SparkSession # The entry point into all functionality in Spark
from pyspark.sql.functions import udf, col # To use user define function
from pyspark.sql.functions import hour, dayofmonth, weekofyear, month, year, dayofweek # To manipulate date
import pyspark.sql.types # Import type

# The following code come from the original Udacity framework
# But we don't need these lines, as we'll launch our ETL directly from our EMR
#config = configparser.ConfigParser()
#config.read('dl.cfg')

#os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
#os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    '''
    Create a Spark session
    '''
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = 
    
    # read song data file
    df = 

    # extract columns to create songs table
    songs_table = 
    
    # write songs table to parquet files partitioned by year and artist
    songs_table

    # extract columns to create artists table
    artists_table = 
    
    # write artists table to parquet files
    artists_table


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data =

    # read log data file
    df = 
    
    # filter by actions for song plays
    df = 

    # extract columns for users table    
    artists_table = 
    
    # write users table to parquet files
    artists_table

    # create timestamp column from original timestamp column
    get_timestamp = udf()
    df = 
    
    # create datetime column from original timestamp column
    get_datetime = udf()
    df = 
    
    # extract columns to create time table
    time_table = 
    
    # write time table to parquet files partitioned by year and month
    time_table

    # read in song data to use for songplays table
    song_df = 

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = 

    # write songplays table to parquet files partitioned by year and month
    songplays_table


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = ""
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
