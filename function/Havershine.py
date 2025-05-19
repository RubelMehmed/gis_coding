#The Haversine formula calculates the distance between two points on the Earth’s surface.Geospatial Problem
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# Example usage
distance = haversine(35.6895, 139.6917, 34.0522, -118.2437)
print(f"Distance: {distance:.2f} km")