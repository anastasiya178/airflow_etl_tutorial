from decouple import config
from requests.auth import HTTPBasicAuth

# URL to the data resource
URL = "https://api.census.gov/data/timeseries/poverty/saipe"

# Set up auth if it's required. Edit API KEY and SECRET in your .env file
AUTH = HTTPBasicAuth(config("API_KEY", ""), config("SECRET", ""))

# specify required data parameters
STATE_CODE = 48  # Texas
COUNTRY_CODE = 201  # Harris County
YEAR = 2018

INDICATORS = [
    "SAEPOV0_17_PT",  # Ages 0-17 in Poverty, Count Estimate
    "SAEPOVALL_PT",  # All ages in Poverty, Count Estimate
    "SAEMHI_PT",  # Median Household Income Estimate
]

# build URL params
URL_PARAMS = {
    "get": ",".join(INDICATORS),
    "for": f"county:{COUNTRY_CODE}",
    "in": f"state:{STATE_CODE}",
    "time": YEAR,
}

# specify CSV header and filename to save data
CSV_HEADER = [
    "Estimate poverty under 18",
    "Estimate poverty any age",
    "Estimate median household income",
]

CSV_FILENAME = "poverty_2018_Harris_TX_.csv"
