import os
from PIL import Image, ExifTags
import piexif
import json
import pytz
from datetime import datetime


def add_timezone(dt, timezone):
    # Get the timezone object based on the timezone string
    tz = pytz.timezone(timezone)

    # Localize the datetime object with the specified timezone
    localized_dt = tz.localize(dt)

    return localized_dt

# Convert GPX time string to datetime object
def timeline_to_datetime(gpx_time_string):
    mytime:datetime = None
    try:
        mytime = datetime.strptime(gpx_time_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    except:
        mytime = datetime.strptime(gpx_time_string, "%Y-%m-%dT%H:%M:%SZ")
    return mytime

def convert_timezone(dt: datetime, from_tz, to_tz):
    # Set the source timezone
    source_tz = pytz.timezone(from_tz)

    # Set the destination timezone
    dest_tz = pytz.timezone(to_tz)

    # Convert the datetime to the source timezone
    localized_dt = source_tz.localize(dt)

    # Convert the datetime to the destination timezone
    converted_dt = localized_dt.astimezone(dest_tz)

    return converted_dt


def is_between(check_dt,start_dt, end_dt):
    return start_dt <= check_dt <= end_dt

# convert your lat/long from decimal degree to degrees, minutes, and seconds
def convert_to_degrees(value):
    v = abs(value)
    d = abs(int(value))
    md = abs(v - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [(d, 1), (m, 1), (int(round(sd*10000)), 10000)]

def attach_gps(in_jpg_image, out_jpg_image,latitude,longitude):
    img = Image.open(in_jpg_image)
    exif_dict = piexif.load(img.info['exif'])
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = convert_to_degrees(latitude)
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = convert_to_degrees(longitude)

    # Depending on whether the coordinates are north/south or east/west, you'll need to set these values accordingly
    exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = 'N' if latitude >= 0 else 'S'
    exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = 'E' if longitude >= 0 else 'W'
    exif_bytes = piexif.dump(exif_dict)
    img.save(out_jpg_image, exif=exif_bytes,quality = 100)
def extract_jpg_metadata(image_path):
    try:
        image = Image.open(image_path)
        metadata = image._getexif()
        exif_dict = piexif.load(image.info['exif'])
        if metadata is None:
            print("No metadata found.")
            return None

        extracted_metadata = {}
        for tag, value in metadata.items():
            if tag in ExifTags.TAGS:
                tag_name = ExifTags.TAGS[tag]
                extracted_metadata[tag_name] = value

        return extracted_metadata
    except FileNotFoundError:
        print("Image file not found.")
        return None
    except Exception as e:
        print("An error occurred while extracting metadata:", str(e))
        return None

def get_jpeg_datetime(image_path):
    meta = extract_jpg_metadata(image_path)
    return jpeg_to_datetime(meta['DateTime'])

def timeline_place_visit(json_file_path):
    places = []
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        for location in json_data['timelineObjects']:
            try:
                latitude=location['placeVisit']['location']['latitudeE7']/10**7,
                longitude=location['placeVisit']['location']['longitudeE7']/10**7,
                btime=location['placeVisit']['duration']['startTimestamp']
                etime=location['placeVisit']['duration']['endTimestamp']
                address = location['placeVisit']['location']['address']
                places.append((latitude[0],longitude[0],btime,etime,address))
            except:
                None
    return places
def timeline_activity_segment(json_file_path):
    places = []
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        for location in json_data['timelineObjects']:
            try:
                latitude=location['activitySegment']['startLocation']['latitudeE7']/10**7,
                longitude=location['activitySegment']['startLocation']['longitudeE7']/10**7,
                btime=location['activitySegment']['duration']['startTimestamp']
                etime=location['activitySegment']['duration']['endTimestamp']
                places.append((latitude[0],longitude[0],btime,etime,''))
            except:
                None
    return places

def jpeg_to_datetime(date_string):
    # Parse the string into a datetime object
    dt = datetime.strptime(date_string, "%Y:%m:%d %H:%M:%S")
    return dt


def get_file_paths(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths
