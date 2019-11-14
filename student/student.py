import sys
import pymysql
# rds settings
rds_host  = 'lit-db.cpjm9tkjf479.us-east-1.rds.amazonaws.com'
name = 'admin'
password = 'password'
db_name = 'project'


try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    print("ERROR: Unexpected error: Could not connect to MySQL instance.")
    print(e)
    sys.exit()

def handler(event, context):

    student_name = 'test'
    """
    This function fetches content from MySQL RDS instance
    """
    cursor = conn.cursor()
    # ok do connection stuff

    query = 'SELECT p FROM People WHERE p.name = ' + student_name
    cursor.execute(query)
    result = cursor.fetchone()

    return makeJsonResult(result)



def makeJsonResult(result):
    # TODO: json stuff
    return result

# print(handler())