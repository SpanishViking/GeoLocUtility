# GeoLocUtility
GeoLocUtility is a utility CLI application that returns Lat, Lon, and other relevant information as provided by the Open Weather API's
Built using Python 3.9
## Usage
From Terminal
```bash
python geolocutil.py --locations "Madison, WI" "12345" "Chicago, Il" "10001"
```
In Python
```python
import geolocutil

# Sample call
geolocutil.main(["--locations", "Maryville, TN", "78550"])
```
Returns
```python
Location 1: [
    {
        "name": "Maryville",
        "lat": 35.7564719,
        "lon": -83.9704593,
        "country": "US",
        "state": "Tennessee"
    }
]
Location 2: {
    "zip": "78550",
    "name": "Harlingen",
    "lat": 26.1951,
    "lon": -97.689,
    "country": "US"
}
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
