import sqlalchemy as sal
import pymysql
from sqlalchemy import create_engine, text

# Create engine
engine = create_engine('mysql+pymysql://admin:password@endpointhere/myflixdb')

# Create connection
connection = engine.connect()

# Execute query
query = text("select * from movies")
result_proxy = connection.execute(query)

# Fetch all rows
data = result_proxy.fetchall()

# Close connection
connection.close()

# Print fetched data
for item in data:
    print(item)

##ubuntu Installation##

install python 3
apt update && apt install python3-pip -y

pip install sqlalchemy
pip install pymysql


Data to insert in schemas

INSERT INTO `movies` VALUES (100,'Pirates of the Caribean 40',' Rob Marshall', 2022,1);
INSERT INTO `movies` VALUES (101,'Pirates of the Caribean 41',' Rob Marshall', 2022,1);
INSERT INTO `movies` VALUES (102,'Pirates of the Caribean 42',' Rob Marshall', 2022,1);
INSERT INTO `movies` VALUES (103,'Pirates of the Caribean 43',' Rob Marshall', 2022,1);
