# ### Task 1
# Scrape weather information from an HTML file and process it using Python and BeautifulSoup.
# Assume you are given the following HTML structure (you can save it as `weather.html`):

weather_html="""
```html
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>"""

# 1. **Parse the HTML File**:
#    - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.
from bs4 import BeautifulSoup
soup = BeautifulSoup(weather_html, 'html.parser')
print(soup.prettify())

# 2. **Display Weather Data**:
#    - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

print("5-Day Weather Forecast:")
for row in soup.find("tbody").find_all("tr"):
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temperature = columns[1].text.strip()
    condition = columns[2].text.strip()
    print(f"{day}: {temperature}, {condition}")

# 3. **Find Specific Data**:
#    - Identify and print the day(s) with:
#      - The highest temperature.
#      - The "Sunny" condition.
# Extract weather data

weather_data = []
for row in soup.find("tbody").find_all("tr"):
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temperature = int(columns[1].text.strip().replace("°C", ""))  # Convert to int
    condition = columns[2].text.strip()
    weather_data.append((day, temperature, condition))

# Find the highest temperature
max_temp = max(weather_data, key=lambda x: x[1])[1]
hottest_days = [day for day, temp, cond in weather_data if temp == max_temp]

# Find all "Sunny" days
sunny_days = [day for day, temp, cond in weather_data if cond == "Sunny"]

# Print results
print(f"Day(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")
    
# 4. **Calculate Average Temperature**:
#    - Compute and print the **average temperature** for the week.

sum=sum(temp for day,temp,cond in weather_data) 
print(round((sum/5),2))  