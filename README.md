# Photo GPS Location Tagger

![License](https://img.shields.io/badge/License-MIT-blue.svg)

**Photo GPS Location Tagger** is a Python program that allows you to tag the GPS location information onto photos. With this program, you can easily add GPS coordinates to your photos, enabling you to organize and categorize them based on their capture location.

## Features

- Extracts GPS coordinates from Google timeline json files.
- Tags the GPS location information onto photos in format of JPEG.
- Supports batch processing, allowing you to tag multiple photos simultaneously.
- Offers customization options for input image file and timeline json file timezone and duration expansion for better matching ratio.
- Provides detailed error handling and informative messages to ensure smooth execution.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/photo-gps-location-tagger.git


2. Navigate to the project directory:
    ```bash
    cd photo-gps-location-tagger
3. install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

Ensure that the photos you want to tag and the GPS data source (e.g., GPS log file) are accessible.
Run the program:
   ```bash
   python photo_gps_location_tagger.py /images /google/timeline/2023-05-01.json

   
positional arguments:
image_file_folder     image file directory (folder), for example, c:\images for Window or /images for Mac
timeline_json_file    Google timeline json file, for example, c:\timeline 3-05-01.json for Window or /google/timeline/2023-05-01.json



You can customize the behavior of the Photo GPS Location Tagger program by optional parameters:
   ```bash
   python photo_gps_location_tagger.py /images /google/timeline/2023-05-01.json
    
   
optional arguments:
-j JPEG_TIMEZONE, --jpeg_timezone JPEG_TIMEZONE
                        Optional parameter for image timestamp timezone, default 'Europe/Lisbon'
-t TIMELINE_TIMEZONE, --timeline_timezone TIMELINE_TIMEZONE
                        Optional parameter for google file timezone, default 'Europe/Lisbon'
-a TIMELINE_ADJUST_MINUTE, --timeline_adjust_minute TIMELINE_ADJUST_MINUTE
                        Optional parameter for google duration, larger number means better chance for tagging, but less precision


Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please submit an issue or a pull request to this repository.

## License

This project is licensed under the MIT License.

## Acknowledgements

This project makes use of the following open-source libraries:

Pillow - Python Imaging Library (PIL)
pyexiv2 - Python binding to the Exiv2 image metadata library

## Contact

For any inquiries or feedback, please contact lanliwz@yahoo.com.

Enjoy tagging your photos with GPS location information!
