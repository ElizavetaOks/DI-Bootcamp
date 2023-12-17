import psycopg2
import requests
import random

def random_countries():
    api_url = "https://restcountries.com/v3.1/all"
    response = requests.get(api_url)
    countries = response.json()
    return random.sample(countries, 10)

def create_database():
    conn = psycopg2.connect(
        dbname = 'itrzdeez',
        user = 'itrzdeez',
        password ='oUFkjGyhLsRvLsIdu1bjzsmmGYKiajnY',
        host = 'flora.db.elephantsql.com',
        port = '5432'
)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name TEXT,
            capital TEXT,
            flag TEXT,
            subregion TEXT,
            population INTEGER
        )
    ''')

    random_countries = random_countries()

    for country in random_countries:
        name = country.get("name", {}).get("common", "")
        capital = country.get("capital", [])[0] if country.get("capital") else ""
        flag = country.get("flags", {}).get("png", "")
        subregion = country.get("subregion", "")
        population = country.get("population", 0)

        cursor.execute('''
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, capital, flag, subregion, population))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
