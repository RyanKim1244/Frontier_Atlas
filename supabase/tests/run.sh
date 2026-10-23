#!/bin/sh
# Usage: PSQL="psql -h HOST -p PORT -U postgres" sh run.sh   (needs a scratch Postgres 15+)
set -e
P=${PSQL:-psql}
$P -q -c "drop database if exists atlas_rls_test" -c "create database atlas_rls_test"
$P -d atlas_rls_test -q -v ON_ERROR_STOP=1 -f stub.sql
$P -d atlas_rls_test -q -v ON_ERROR_STOP=1 -f ../migrations/20261023000000_init.sql
$P -d atlas_rls_test -f rls_test.sql 2>&1
