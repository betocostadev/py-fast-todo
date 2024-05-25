# from fastapi import FastAPI
# import psycopg2 as pg

# api = FastAPI()

# conn = pg.connect(
#     host="db",
#     port="5432",
#     user="postgres",
#     password="postgres",
#     database="postgres"
# )

# @api.get("/")
# def index():
#     print("Server is running")
#     cur = conn.cursor()
#     cur.execute("SELECT gen_random_uuid();")
#     uuid, *_ = cur.fetchone()
#     return f"UUID from Postgres: {uuid}"
