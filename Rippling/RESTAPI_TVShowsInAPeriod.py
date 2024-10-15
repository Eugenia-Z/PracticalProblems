import requests

def fetch_series_data():
    base_url = "https://jsonmock.hackerrank.com/api/tvseries"
    page = 1
    series_data = []
    
    while True:
        # Fetch data for the current page
        response = requests.get(f"{base_url}?page={page}")
        json_data = response.json()
        
        # Append the current page's data to the series_data list
        series_data.extend(json_data["data"])
        
        # If we have fetched all pages, break the loop
        if page >= json_data["total_pages"]:
            break
        
        page += 1
    
    return series_data

def parse_runtime_of_series(runtime):
    """
    Parses the runtime_of_series string to extract the start year and end year.
    Handles cases like "2011-2019", "2015-", etc.
    """
    runtime = runtime.replace("(I)", "").replace("(II)", "").strip()
    
    if "-" in runtime:
        start_year, end_year = runtime.split("-")
        start_year = int(start_year)
        # Handle "present" as a special case
        if end_year == "":
            end_year = -1
        else:
            end_year = int(end_year)
        return start_year, end_year
    return None, None

def showsInProduction(startYear, endYear):
    series_data = fetch_series_data()
    result = []
    
    for series in series_data:
        runtime = series["runtime_of_series"]
        start, end = parse_runtime_of_series(runtime)
        
        # If the runtime couldn't be parsed, skip the series
        if start is None or end is None:
            continue
        
        # Check if the series fits within the provided years
        if start >= startYear and (end <= endYear or endYear == -1 or end == -1):
            result.append(series["name"])
    
    # Return the sorted list of show names
    return sorted(result)

# Example usage
print(showsInProduction(2000, 2020))
        