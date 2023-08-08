
pip install Flask

from flask import Flask, render_template, request
import sqlite3


#### Initialization

app = Flask(__name__)


### Define the database

def create_db():
    conn = sqlite3.connect('config_generator.db')
    c = conn.cursor()
    # Create the 'cities' table
    c.execute('''CREATE TABLE IF NOT EXISTS cities (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 description TEXT NOT NULL,
                 ebas TEXT NOT NULL,
                 mean_cost INTEGER NOT NULL,
                 currency TEXT NOT NULL,
                 location TEXT NOT NULL,
                 budget INTEGER NOT NULL
                 )''')
    # Create the 'ebas' table
    c.execute('''CREATE TABLE IF NOT EXISTS ebas (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 description TEXT NOT NULL,
                 icon TEXT NOT NULL,
                 cost INTEGER NOT NULL
                 )''')
    conn.commit()
    conn.close()


#### Initial EBAs

def insert_initial_ebas():
    conn = sqlite3.connect('config_generator.db')
    c = conn.cursor()
    # Insert sample EBA data
    ebas_data = [
        ('6c3c338f-5587-4d93-8e6c-a0b23cc78989', 'Dune Stabilization', 'Dune stabilization refers to the process of managing and preserving sand dunes to prevent erosion and maintain their ecological and environmental functions. ...', 'Dune', 70000),
        ('6c3c338f-5587-4d93-8e6c-a0b23cc78989', 'Tree plantation', 'Tree plantation is the process of planting and establishing trees in various locations, including forests, urban areas, and agricultural lands, with the aim of improving the environment and achieving multiple benefits. ...', 'Green', 70000),
        # Add more EBA data as needed
    ]
    c.executemany('''INSERT INTO ebas (id, name, description, icon, cost)
                     VALUES (?, ?, ?, ?, ?)''', ebas_data)
    conn.commit()
    conn.close()


### Create the route

@app.route('/generate_config', methods=['POST'])
def generate_config():
    # Retrieve form data
    city_name = request.form['city-name']
    city_description = request.form['city-description']
    selected_ebas = request.form.getlist('selected-ebas')
    mean_cost = int(request.form['mean-cost'])
    currency = request.form['currency']
    map_center = request.form['map-center']
    city_budget = int(request.form['city-budget'])

    # Convert the list of selected ebas to a string for storage in the database
    ebas_str = ','.join(selected_ebas)

    # Insert data into the database
    conn = sqlite3.connect('config_generator.db')
    c = conn.cursor()
    c.execute('''INSERT INTO cities (name, description, ebas, mean_cost, currency, location, budget)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (city_name, city_description, ebas_str, mean_cost, currency, map_center, city_budget))
    conn.commit()
    conn.close()

    # Return a response or redirect to another page
    return 'Config generated successfully!'


#### Running the app

if __name__ == '__main__':
    create_db()  # Create the database and tables when the app starts
    insert_initial_ebas()  # Insert initial EBA data
    app.run(debug=True)

