from os import listdir, path

from connection import connectToDB

from createTables import createTables
from land2dict import parseXML
from insert_into_table import insertIntoTable
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_SCHEMA

(connection, cursor) = connectToDB(
  DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)

#createTables(cursor, connection)

data_dir = 'R:\Тематические_карты_и_планы\Инвентаризация СХ земель\КПТ\Часть_3'

for dir in listdir(data_dir):
    for f in listdir(path.join(data_dir, dir)):
        ext = path.splitext(f)[1]
        if ext == '.xml':
          with open(path.join(data_dir, dir, f), encoding="utf8") as f:
              xml = parseXML(f)
              insertIntoTable(cursor, connection, xml)