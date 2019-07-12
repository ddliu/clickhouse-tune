# How to Reproduce

1. Create docker containers with two different versions of clickhouse

```
docker-compose up -d
```

2. Load test data and run query(latest)

Load data

```
docker exec -it clickhouse1 bash
cat /data/data.sql | clickhouse-client -mn
```

```
clickhouse-client

62d7565cd7ca :) select * from system.tables where name='test_997'

SELECT *
FROM system.tables
WHERE name = 'test_997'

┌─database─┬─name─────┬─engine────┬─is_temporary─┬─data_path───────────────────────────────┬─metadata_path──────────────────────────────────┬─metadata_modification_time─┬─dependencies_database─┬─dependencies_table─┬─create_table_query────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬─engine_full─────────────────────────┬─partition_key──────┬─sorting_key─┬─primary_key─┬─sampling_key─┐
│ test     │ test_997 │ MergeTree │            0 │ /var/lib/clickhouse/data/test/test_997/ │ /var/lib/clickhouse/metadata/test/test_997.sql │        2019-07-12 10:49:09 │ []                    │ []                 │ CREATE TABLE test.test_997 (`datadate` Date, `datatime` UInt32, `name` String, `age` UInt64) ENGINE = MergeTree(datadate, datatime, 8192) │ MergeTree(datadate, datatime, 8192) │ toYYYYMM(datadate) │ datatime    │ datatime    │              │
└──────────┴──────────┴───────────┴──────────────┴─────────────────────────────────────────┴────────────────────────────────────────────────┴────────────────────────────┴───────────────────────┴────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴─────────────────────────────────────┴────────────────────┴─────────────┴─────────────┴──────────────┘

1 rows in set. Elapsed: 0.255 sec. Processed 3.03 thousand rows, 1.31 MB (11.90 thousand rows/s., 5.14 MB/s.)
```

3. Load test data and run query(1.1.54380)

```
docker exec -it clickhouse2 bash
cat /data/data.sql | clickhouse client -mn
```

```
clickhouse client

8c5932181439 :) select * from system.tables where name='test_997'

SELECT *
FROM system.tables
WHERE name = 'test_997'

┌─database─┬─name─────┬─engine────┬─is_temporary─┬─data_path───────────────────────────────┬─metadata_path──────────────────────────────────┐
│ test     │ test_997 │ MergeTree │            0 │ /var/lib/clickhouse/data/test/test_997/ │ /var/lib/clickhouse/metadata/test/test_997.sql │
└──────────┴──────────┴───────────┴──────────────┴─────────────────────────────────────────┴────────────────────────────────────────────────┘

1 rows in set. Elapsed: 0.005 sec. Processed 3.02 thousand rows, 464.55 KB (562.75 thousand rows/s., 86.48 MB/s.)

8c5932181439 :)
```