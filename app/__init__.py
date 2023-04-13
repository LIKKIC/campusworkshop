"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="@dpg-cgrq5c1mbg5e4khqpd90-a.oregon-postgres.render.com",
        database="todoapp_57z4",
        user="root",
        password="IvjrLrQjQ46plRwCrlt5mZWkPaUxipg5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
