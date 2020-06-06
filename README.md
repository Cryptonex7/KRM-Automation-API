# COVID19 Analytics India &middot; ![version](https://img.shields.io/github/v/release/Cryptonex7/covid19-analysis) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Open Source API

Flask Backend for COVID-19-React-App.

_This App focuses to show:_

1. Real time statistical figures of COVID-19 in India.
2. Analysis on COVID-19 Data.
3. Ways to flatten the COVID-19 spread and death curves through Analytical Models.

## Deploy

- Push to branch `dev`: [devapi.covidanalyticsindia.now.sh](https://devapi.covidanalyticsindia.now.sh)
- Push to branch `test`: [testapi.covidanalyticsindia.now.sh](https://testapi.covidanalyticsindia.now.sh)
- Push to branch `master`: [api.covidanalytics.live](https://api.covidanalytics.live)

## Setup

```
$ source 'env/Srcipts/activate'

$ python app.py
```

## To configure the studentdata table initially (if needed)

```
cat ~/Downloads/studentdata.csv | \psql `heroku config:get DATABASE_URL --app krmdatabase` -c "COPY studentdata FROM STDIN WITH (FORMAT CSV, HEADER);"
```

## To configure the companydata table initially (if needed)

```
cat ~/Downloads/companydata.csv | \psql `heroku config:get DATABASE_URL --app krmdatabase` -c "COPY companydata FROM STDIN WITH (FORMAT CSV, HEADER);"
```
