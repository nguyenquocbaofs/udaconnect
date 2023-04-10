from typing import Dict

import psycopg2
from config import DB_USERNAME, DB_HOST, DB_NAME, DB_PORT, DB_PASSWORD


class LocationService:
    @staticmethod
    def create(location: Dict):
        print('Received a location: ', location)
        session = psycopg2.connect(
            dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)
        cursor = session.cursor()
        cursor.execute(
            'INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}));'.format(
                int(location["person_id"]),
                float(location["latitude"]),
                float(location["longitude"])))
        session.commit()
        cursor.close()
        session.close()

        return
