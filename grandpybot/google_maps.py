"""Module that call the Google Maps API
"""
import googlemaps

google_api_key = "AIzaSyC5ySLJJEg2yVmQ5JcNzFEM2-fcM42EWnU"


class GMaps:
    """Class to call Google Maps API"""

    def __init__(self, google_api_key):
        self.google_api_key = google_api_key

    def get_position(self, question):
        """Return the geographical coordinates of the parsed user input"""
        gmaps = googlemaps.Client(key=self.google_api_key)
        gmap_result = gmaps.geocode(question, region='fr')

        try:
            address = gmap_result[0]["formatted_address"]
            lat = gmap_result[0]["geometry"]["location"]["lat"]
            lng = gmap_result[0]["geometry"]["location"]["lng"]

            return {
                "address": address,
                "latitude": lat,
                "longitude": lng
            }

        except IndexError:
            return "no result"