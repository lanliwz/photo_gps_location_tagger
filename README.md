# Photo GPS Location Tagger

Photo GPS Location Tagger is a Python program that allows you to tag the GPS location information onto photos. With this program, you can easily add GPS coordinates to your photos, enabling you to organize and categorize them based on their capture location.

### Features

Extracts GPS coordinates from a variety of sources, including GPS-enabled cameras, GPS log files, or external GPS devices.
Tags the GPS location information onto photos in popular formats like JPEG and PNG.
Supports batch processing, allowing you to tag multiple photos simultaneously.
Offers customization options for the output file names and formatting of the GPS coordinates.
Provides detailed error handling and informative messages to ensure smooth execution.
### Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/photo-gps-location-tagger.git
Navigate to the project directory:
bash
Copy code
cd photo-gps-location-tagger
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage

Ensure that the photos you want to tag and the GPS data source (e.g., GPS log file) are accessible.
Modify the configuration file (config.ini) with the desired settings, including the paths to the input photos and GPS data, output directory, and customization options.
Run the program:
bash
Copy code
python photo_gps_location_tagger.py
The program will process the input photos and tag them with the GPS location information according to the configuration settings.
Configuration

You can customize the behavior of the Photo GPS Location Tagger program by modifying the config.ini file. Here are some important configuration options:

photo_directory: Path to the directory containing the photos to be tagged.
gps_data_file: Path to the GPS data source file (e.g., GPS log file).
output_directory: Path to the directory where the tagged photos will be saved.
output_file_format: Format of the output file names (e.g., {original_name}_tagged).
gps_coordinate_format: Format of the GPS coordinates to be displayed on the photo (e.g., Decimal Degrees).
Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please submit an issue or a pull request to this repository.

### License

This project is licensed under the MIT License.

### Acknowledgements

This project makes use of the following open-source libraries:

Pillow - Python Imaging Library (PIL)
pyexiv2 - Python binding to the Exiv2 image metadata library
Contact

For any inquiries or feedback, please contact lanliwz@yahoo.com.

Enjoy tagging your photos with GPS location information!
