import os
# gen tables
sql = """
create database test;
use test;
"""

for i in range(3000):
    sql += "CREATE TABLE test.test_%d ( datadate Date,  datatime UInt32,  name String,  age UInt64) ENGINE = MergeTree(datadate, datatime, 8192);\n" % (i)

for i in range(3000):
    sql += "insert into test_1 (datadate,datatime,name,age) values ('2018-01-01',1234,'name%d',%d);\n" % (i, i)

with open("data.sql", "w") as f:
    f.write(sql)
    # os.write(f, sql)

# data