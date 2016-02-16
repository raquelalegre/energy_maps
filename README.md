
# Energy Maps
This Flask application presents several plots and maps with information
obtained from tweets from 18th January 2016 - 16th January 2016 about British
energy companies.

These tweets have been stored in a CartoDB account and georeferenced so that
they can be plotted in a map.

Energy Maps sends queries to CartoDB's PostGIS DB, elaborates and filters the
results, and plots in time series graphs filtered by area or company.

# Run the application
To obtain Energy Maps and run it:

```
git clone https://github.com/raquel-ucl/energy_maps.git
pip install -r energy_maps/requirements.txt
cd energy_maps/energy_app
python runapp.py
```

Then point your browser to http://localhost:5000.

Note that the time series plots won't work without my CartoDB API key (which is
used to query the PostGIS DB). If you want to use your own, place your key in
a `secrets.json` file in this format:

```json
{
    "api_key": "YOUR_KEY"
}
```

The `secrets.json` file must be placed as shown below:

```
├── README.md
├── energy_app
│   ├── energy_app
│   │   ├── CartodbClient.py
│   │   ├── DataPlotter.py
│   │   ├── DataProcessor.py
│   │   ├── __init__.py
│   │   ├── templates
│   │   ├── test
│   │   └── views.py
│   ├── runapp.py
│   └── secrets.json
└── requirements.txt
```


# Run tests
Only a couple tests have been configured for the connection to CartoDB and to
test the data retrieval. To run them:

```
cd energy_app/
py.test -v
```

# Future work
This is my first Flask application and I intend to improve this as I learn more.
The first intention when designing this application was to categorize tweets
by good, bad or neutral reviews about, but that functionality is not included
yet.
