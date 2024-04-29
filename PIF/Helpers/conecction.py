import pymysql


def conection()->pymysql.connections.Connection:
    return pymysql.connect(host='localhost',user='root', password='1234',db='FUTSTORE')


