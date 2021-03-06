from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def _get_if_exist(data, key):
    if key in data:
        return data[key]
    return None

def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def convertion(value):
    d = value[0]
    m = value[1]
    s = value[2]
    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None
    if "GPSInfo" in exif_data:		
        gps_info = exif_data["GPSInfo"]
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convertion(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat = 0 - lat
            lon = convertion(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon
    return [lat, lon]

def get_time(exif_data):
    L = exif_data.keys()
    if 'DateTime' in L :
        return exif_data['DateTime']
