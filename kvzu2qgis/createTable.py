from config import DB_SCHEMA

land_table_name = 'wow_polygon'
constr_table_name = 'wow_line'

def createTable(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS {0}.{1} \
    (\
        uid uuid NOT NULL DEFAULT uuid_generate_v1(),\
        geom geometry(MultiPolygon,4326), \
        type text,\
        cadastral_number character varying(40),\
        subtype text,\
        common_land_cad_num character varying(40),\
        cat text,\
        permitted_use text,\
        area real,\
        region text,\
        district text,\
        full_address text,\
        cost real,\
        CONSTRAINT {1}_pkey PRIMARY KEY (uid),\
        CONSTRAINT {1}_cn_key UNIQUE (cadastral_number)\
    )\
    TABLESPACE pg_default;\
    ALTER TABLE IF EXISTS {0}.{1} OWNER to kotelevsky;\
    GRANT ALL ON TABLE {0}.{1} TO gisadmins;\
    GRANT ALL ON TABLE {0}.{1} TO gisusers;\
    GRANT ALL ON TABLE {0}.{1} TO kotelevsky;".format(DB_SCHEMA, land_table_name))

    cur.execute("CREATE TABLE IF NOT EXISTS {0}.{1} \
    (\
        uid uuid NOT NULL DEFAULT uuid_generate_v1(),\
        geom geometry(MultiLine,4326), \
        type text,\
        cadastral_number character varying(40),\
        subtype text,\
        common_land_cad_num character varying(40),\
        cat text,\
        permitted_use text,\
        area real,\
        region text,\
        district text,\
        full_address text,\
        cost real,\
        CONSTRAINT {1}_pkey PRIMARY KEY (uid),\
        CONSTRAINT {1}_cn_key UNIQUE (cadastral_number)\
    )\
    TABLESPACE pg_default;\
    ALTER TABLE IF EXISTS {0}.{1} OWNER to kotelevsky;\
    GRANT ALL ON TABLE {0}.{1} TO gisadmins;\
    GRANT ALL ON TABLE {0}.{1} TO gisusers;\
    GRANT ALL ON TABLE {0}.{1} TO kotelevsky;".format(DB_SCHEMA, constr_table_name))
    conn.commit()