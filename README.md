# RestAPIExample

Wellcome to a simple API that makes querys to a local sqlite database to know exchange rates.

## Install the necessary dependencies

Create a virtual enviroment if necesary or just run the following command:

```bash
pip install -r requirements.txt
```

## Populating data

You have two options to populate the database:

- The first one is to use a json file on the root folder with the following format

```json
[
  {
    "quote": "USD",
    "base": "CLP",
    "rate": 0.001262,
    "date": "2020-06-13"
  },
  {
    "quote": "USD",
    "base": "CLP",
    "rate": 0.001262,
    "date": "2020-06-14"
  }
]
```

If you want to change the directory of the json file dont forget to change the config class value in the file /main/settings.py

```python
MOCK_DATA_JSON = os.path.join(BASE_DIR, 'mockDB.json')
```

Once you have the file, use the following command to populate with the MOCK file

```bash
python manage.py populate --data_source MOCK
```

- The next option is to use an external API to pull the values, to do that just use the following command

```bash
python manage.py populate --data_source API --base EUR --quote USD --start_date 2020-06-13 --end_date 2020-06-18
```

## Running the API

Once you have populate the database you can run the API with the following command

```bash
python manage.py run
```

## Getting data

There are two endpoints you can hit to get the information stored inside the database, you can use a query param to switch between data populated using the MOCK json file or the API

- To get data using a date or date range:

```http
http://127.0.0.1:5000/currency-exchange/range/?base=EUR&quote=USD&date=2020-06-14&end_date=2020-06-17&source=MOCK
```

```json
[
  {
    "base_currency": "EUR",
    "exchange_date": "2020-06-14",
    "exchange_rate": 1.125157,
    "quote_currency": "USD"
  },
  {
    "base_currency": "EUR",
    "exchange_date": "2020-06-15",
    "exchange_rate": 1.133742,
    "quote_currency": "USD"
  },
  {
    "base_currency": "EUR",
    "exchange_date": "2020-06-16",
    "exchange_rate": 1.126532,
    "quote_currency": "USD"
  },
  {
    "base_currency": "EUR",
    "exchange_date": "2020-06-17",
    "exchange_rate": 1.124252,
    "quote_currency": "USD"
  }
]
```

(If end_date is not provided then you will get the exchange for one particular date)

- To get the latest exchange

```http
http://127.0.0.1:5000/currency-exchange/latest/?base=EUR&quote=USD
```

```json
{
  "base_currency": "EUR",
  "exchange_date": "2020-06-18",
  "exchange_rate": 1.12095,
  "quote_currency": "USD"
}
```

(The default value for source is API, if you dont provide the parammeter)
