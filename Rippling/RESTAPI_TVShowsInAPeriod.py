import requests

def fetch_series_data():
    base_url = "https://jsonmock.hackerrank.com/api/tvseries"
    page = 1
    series_data = []
    
    while True:
        # Fetch data for the current page
        response = requests.get(f"{base_url}?page={page}")
        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code}")
            break
        
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
    runtime = runtime.replace("(I)", "").replace("(II)", "").strip('(').strip(')')
    runtime_split = runtime.split("-")  # Dash is sometimes different, using the right symbol here
    
    try:
        start_year = int(runtime_split[0].strip())  # Extract the start year
    except ValueError:
        print(f"Error parsing start year from: {runtime}")
        return None, None  # Handle the error if start year is not valid
    
    # Extract the end year or handle ongoing series
    if len(runtime_split) > 1 and runtime_split[1].strip():
        try:
            end_year = int(runtime_split[1].strip())
        except ValueError:
            print(f"Error parsing end year from: {runtime}")
            end_year = -1  # If no valid end year, treat it as ongoing (-1)
    else:
        end_year = -1  # Ongoing series
    
    return start_year, end_year

def showsInProduction(startYear, endYear):
    series_data = fetch_series_data()
    result = []
    
    for series in series_data:
        start, end = parse_runtime_of_series(series['runtime_of_series'])
        
        # If parsing failed, skip the series
        if start is None or end is None:
            continue
        
        # Check if the series fits within the provided year range
        if start >= startYear and (endYear == -1 or end == -1 or end <= endYear):
            result.append(series["name"])
    
    # Return the sorted list of show names
    return sorted(result)

# Example usage
print(showsInProduction(2000, 2020))
