# Household Fotomat

## A utility script to upload files to an FTP server

**Household Fotomat** is a script to upload images from a source folder to an FTP server. The script will automatically resize images that exceed the maximum dimensions. The script also extracts original image creation date and generates an export file to assist with further processing.

## Installing The Program

The program requires python to run.

### Setup

Copy the .env.example file to a new .env and update this file with your FTP and folder settings.

### Prerequisites

It may be necessary to install python3, or it may already be installed. To check, run the following command:
$ python -v

If you do not see python 3.x, you may need to install it.

$ sudo apt-get install python3

## Using This Program

This script reads from application settings to connect and authenticate. It is necessary to configure the env file before using it.

$ python3 __init__.py

## Contributing

Please review the [CONTRIBUTING.md](CONTRIBUTING.md) file if you are interested in helping develop or 
maintain this program. Also, please be aware that contributors are expected to adhere to the 
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and use the [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md) 
when submitting code.

## About This Program

This script was created by Noah Stewart to help manage a local image library and deploy it automatically to the cloud for further processing. This script is just one component of a more complex system and is used to coordinate content between the local network and the cloud accessible exports.

## License

The program **Household Fotomat** is open-sourced software licensed under the ISC license.
