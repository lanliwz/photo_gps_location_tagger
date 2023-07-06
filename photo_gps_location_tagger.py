from function import attach_gps, get_jpeg_datetime, is_between, timeline_activity_segment, timeline_place_visit, \
    convert_timezone
from datetime import timedelta
from function import get_file_paths,timeline_to_datetime,add_timezone
import argparse

def photo_gps_location_tagger(jpeg_folder,timeline_json_file,jpeg_timezone = None, timeline_timezone = None,timeline_adjust_minute:int = None, timeline_element_tag = None):
    if jpeg_timezone == None:
        jpeg_timezone = 'Europe/Lisbon'
    if timeline_timezone == None:
        timeline_timezone = 'Europe/Lisbon'
    if timeline_adjust_minute == None:
        timeline_adjust_minute:int = 0
    print("start tagging ... ...")
    print(f"search files in {jpeg_folder}")

    picfiles = get_file_paths(jpeg_folder)

    numoffiles = len(picfiles)
    notaggingfiles = 0

    print(f'Total {numoffiles} image files found')

    jpeg_datetime_adjust_minutes: int = 0

    datetime_adjust_minute = timedelta(minutes=timeline_adjust_minute)
    if jpeg_datetime_adjust_minutes >=0:
        jpeg_datetime_adjust_minute =  timedelta(minutes=jpeg_datetime_adjust_minutes)
    else:
        jpeg_datetime_adjust_minute = - timedelta(minutes=jpeg_datetime_adjust_minutes)

    if timeline_element_tag == 'activitySegment':
        place_visit = timeline_activity_segment(timeline_json_file)
    elif timeline_element_tag == 'placeVisit' or timeline_element_tag == None:
        place_visit = timeline_place_visit(timeline_json_file)



    for picfile in filter(lambda f: str(f).lower().endswith('jpg'), picfiles) :
        match = False
        picdatetime = convert_timezone(get_jpeg_datetime(picfile),jpeg_timezone,timeline_timezone)

        for la,lo,stime,etime,address in place_visit:
            sstime = add_timezone(timeline_to_datetime(stime) - datetime_adjust_minute, timeline_timezone)
            eetime = add_timezone(timeline_to_datetime(etime) + datetime_adjust_minute, timeline_timezone)
            outfile = picfile

            if is_between(picdatetime,sstime,eetime):
                attach_gps(picfile,
                           outfile,
                           la,
                           lo)
                match = True
                break
        if match == False:
            notaggingfiles = notaggingfiles +1
            print(f'image timestamp: {picdatetime}, no GPS tagging for image file {picfile}')
    print(f"end tagging, total {numoffiles - notaggingfiles} of {numoffiles} tagged")


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Description of your script")

    # Add input parameters
    parser.add_argument("image_file_folder", type=str, help="image file directory (folder), for example, c:\\images for Window or /image for Mac")
    parser.add_argument("timeline_json_file", type=str, help="Google timeline json file, for example, c:\\timeline\2023-05-01.json for Window or /timeline/2023-05-01.json")
    parser.add_argument("-j", "--jpeg_timezone", type=str, help="Optional parameter for image timestamp timezone, default 'Europe/Lisbon'")
    parser.add_argument("-t", "--timeline_timezone", type=str, help="Optional parameter for google file timezone, default 'Europe/Lisbon'")
    parser.add_argument("-a", "--timeline_adjust_minute", type=int, help="Optional parameter for google duration, larger number means better chance for tagging, but less precision")
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the provided input parameters
    print(type(args.timeline_adjust_minute))
    photo_gps_location_tagger(args.image_file_folder,args.timeline_json_file,args.jpeg_timezone, args.timeline_timezone,args.timeline_adjust_minute )






