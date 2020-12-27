#! /usr/bin/bash
/bin/sleep 5
psql postgresql://postgres:example@localhost:5432/postgres -c "CREATE TABLE IF NOT EXISTS TEST(txt VARCHAR, num INT)"
psql postgresql://postgres:example@localhost:5432/postgres -c "\copy TEST(txt, num) FROM '/usr/local/data/data.csv' DELIMITER ',' CSV"
psql postgresql://postgres:example@localhost:5432/postgres -c "SELECT * FROM TEST" && echo "Data inserted"
