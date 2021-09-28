if [ ! -e '/check' ]; then
    touch /check
    psql -U root -d <POSTGRES_DB> -c "
        CREATE EXTENSION IF NOT EXISTS postgis;
        CREATE EXTENSION IF NOT EXISTS postgis_topology;
        CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
        CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;
    "
else
    echo "OK"
fi