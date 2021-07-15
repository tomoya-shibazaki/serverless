import os
import sys
import logging
import pymysql


def handler(event, context):
    name = os.environ.get('USER_NAME')   
    password = os.environ.get('PASSWORD')
    db_name = os.environ.get('DB_NAME')
    rds_host = os.environ.get('RDS_HOST')


    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except pymysql.MySQLError as e:
        logger.info(name)
        logger.info(password)
        logger.info(db_name)
        logger.info(rds_host)
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()

    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
    
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        'body': '{"message": "Connection to RDS MySQL instance succeeded"}'
    }