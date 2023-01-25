import psycopg2
from dotenv import load_dotenv
from dotenv import dotenv_values
import os

#Python way of getting the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__name__))

#Loading the environment variables
load_dotenv(os.path.join(basedir, 'dev.env'))
# config = dotenv_values('dev.env')
# print(os.environ.get('DB_USER'))
# print(os.environ['DB_PORT'])
# print(os.getenv('DB_PASSWORD'))
#print(config.get('DB_USER))


conn = psycopg2.connect(f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')}  host={os.getenv('DB_HOST')}  port={os.getenv('DB_PORT')}")
cur = conn.cursor()

cur.execute('SELECT * FROM "public"."post" ')

posts = cur.fetchall()
print(posts)

conn.commit()

cur.close()
conn.close()
