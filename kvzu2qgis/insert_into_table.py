from psycopg2 import sql

def insertIntoTable(cur, conn, schemaName, tableName, data):
    query = sql.SQL(
            """
            INSERT INTO {schema} ({fields}) VALUES ({cad_num}, {geom}) ON CONFLICT ({cad_num_f}) DO UPDATE SET {geom_f}= {geom};
            """
        ).format(
            schema = sql.Identifier(schemaName, tableName),
            fields = sql.SQL(', ').join(map(sql.Identifier, ['cadastral_number', 'geom'])),
            cad_num = sql.Literal(data['cad_number']),
            geom = sql.SQL('ST_GeomFromText(\'' + data['geom'] + '\')'),
            cad_num_f = sql.Identifier('cadastral_number'),
            geom_f = sql.Identifier('geom')
        )
    #print(query.as_string(conn))
    cur.execute(query)
    conn.commit()