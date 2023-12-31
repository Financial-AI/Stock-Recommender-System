# Getting Started with H2O Wave

This project was bootstrapped with `wave init` command.

## Creating the database

1. Install mysql

2. Start mysql on `localhost` port `3306` (this should be the default port)

3. Create a user in mysql with the username: user and password: password

## Seeding the database

Place the following files in the "myStock-wave-app/database/seed" directory:

1. metadata csv file
2. recommender dataframe result CSVs of companies
   
Then run the script  "myStock-wave-app/seed_database_tables.py"

## Running the app

Make sure you have activated a Python virtual environment with `h2o-wave` installed.

If you haven't created a python env yet, simply run the following command (assuming Python 3.7 is installed properly).

For MacOS / Linux:

```sh
python3 -m venv venv
source venv/bin/activate
pip install h2o-wave
```

For Windows:

```sh
python3 -m venv venv
venv\Scripts\activate
pip install h2o-wave
```

Once the virtual environment is setup and active, run:

```sh
wave run app.py
```

Which will start a Wave app at <http://localhost:10101>.

## Interactive examples

If you prefer learning by doing, you can run `wave fetch` command that will download all the existing small Python examples that show Wave in action. The best part is that all these examples are interactive, meaning you can edit their code directly within the browser and observe the changes.

## Learn More

To learn more about H2O Wave, check out the [docs](https://wave.h2o.ai/).
