def createTables(cur, conn, schema, tableName):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS {schema}.{table}
                (
                uid uuid NOT NULL DEFAULT uuid_generate_v1(),
                geom geometry(MultiPolygon,4326),
                cadastral_number character varying(40),
                CONSTRAINT {table}_pkey PRIMARY KEY (uid),
                CONSTRAINT {table}_cn_key UNIQUE (cadastral_number)
                )TABLESPACE pg_default;""".format(
                    schema = schema,
                    table = tableName
                )
    )


    conn.commit()


if __name__ == "__main__":
    from connection import connectToDB
    from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_SCHEMA, DB_TABLE

    (connection, cursor) = connectToDB(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)

    createTables(cursor, connection, DB_SCHEMA, DB_TABLE)