import psycopg2
import config
import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import configparser

def retrieve_list():
    #Go to webpage and scrape data
    html = urlopen('https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets')
    bsobj = soup(html.read())
    tbody = bsobj('table',{'class':'wikitable plainrowheaders sortable'})[9].findAll('tr')
    xl = []
    for row in tbody:
        cols = row.findChildren(recursive = False)
        cols = tuple(element.text.strip().replace('%','') for element in cols)
        xl.append(cols)
    xl = xl[1:-1]
    return xl

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    config = configparser.RawConfigParser()
    config.read(filenames = 'database.ini')
    print(config.sections())

    h = config.get('postgresql','host')
    u = config.get('postgresql','user')
    p = config.get('postgresql','pwd')
    db = config.get('postgresql','db')
    try:

        # connect to the PostgreSQL server

        print('Connecting to the PostgreSQL database...')
        #conn = psycopg2.connect(host=h,database=db,user=u,password=pwd)
        conn = psycopg2.connect(database=db)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        # Drop table if it already exist using execute() method.
        cur.execute("DROP TABLE IF EXISTS scraper_data ")

        # Create table as per requirement
        sql = """CREATE TABLE scraper_data(
            RANKING integer PRIMARY KEY,
            MARKET text,
            RETAIL_VALUE text,
            CHANGE   text,
            PHYSICAL integer,
            DIGITAL text,
            PERFORMANCE_RIGHTS integer,
            SYNCHRONIZATION integer
            )"""

        cur.execute(sql)
        #Save data to the table
        conn.commit()
        sql_insert_query = """INSERT INTO scraper_data(RANKING, MARKET, RETAIL_VALUE, CHANGE, PHYSICAL, DIGITAL, PERFORMANCE_RIGHTS, SYNCHRONIZATION) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        records_to_insert = retrieve_list()
        cur.executemany(sql_insert_query, records_to_insert)
        #Save data to the table
        conn.commit()
        print(cur.rowcount, "Record inserted successfully into scraper_data table")

        # display the PostgreSQL scraped data
        db_data = cur.fetchall()
        print(db_data)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

connect()