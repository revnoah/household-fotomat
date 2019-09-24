#!/usr/bin/python3

from dotenv import load_dotenv
load_dotenv()

import ftplib
import os
import sqlite3

from PIL import Image

#read settings from env file
ftpserver=os.getenv('FTP_SERVER')
ftpuser=os.getenv('FTP_USER')
ftppass=os.getenv('FTP_PASS')
sourcedir=os.getenv('SOURCE_DIR')
cachedir=os.getenv('CACHE_DIR')
sqldb=os.getenv('DB_FILE', 'data/fotomatdb')
maxwidth=int(os.getenv('MAX_WIDTH', 1024))
maxheight=int(os.getenv('MAX_HEIGHT', 1024))

# get filepath to upload, creating temp file if necessary
def file_to_upload(filepath):
	im = Image.open(filepath)

	if im.size[0] > maxwidth or im.size[1] > maxheight:
		return file_resize(filepath);
	else:
		return filepath;

# resize file
def file_resize(filepath):
	# extract filename and extension
	filename=os.path.basename(filepath)
	fileext=os.path.splitext(filepath)

	# read image and resize if necessary
	im = Image.open(filepath)
	im.thumbnail((maxwidth, maxheight), Image.ANTIALIAS)
	if fileext[1] == '.png':
		imformat='PNG'
	else:
		imformat='JPEG'
	im.save(cachedir + '/' + filename, imformat)
	return cachedir + '/' + filename;

# exif data related to file
def file_exif(filepath):
	f = open(filepath, 'rb')
	data = exifread.process_file(f)
	return data;

# initial setup of db
def db_setup():
	db = sqlite3.connect(sqldb)
	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE photos(id INTEGER PRIMARY KEY, 
			filename TEXT unique,
			filetype CHAR(4),
			active TINYINT DEFAULT 0, 
			filecreated DATETIME NULL,
			created DATETIME DEFAULT CURRENT_TIMESTAMP,
			updated DATETIME DEFAULT CURRENT_TIMESTAMP)
	''')
	db.commit()

# add photo entry to db
def db_add_photo(filename, filetype, filecreated):
	db = sqlite3.connect(sqldb)
	cursor = db.cursor()
	cursor.execute('''
		INSERT INTO photos 
			(filename, filetype, filecreated) 
			VALUES (?, ?, ?)''', 
		(filename, filetype, filecreated))
	db.commit()

ftpsession = ftplib.FTP(ftpserver, ftpuser, ftppass)

for root, dirs, files in os.walk(sourcedir):
	for filename in files:
		sourcepath = sourcedir + '/' + filename
		path = file_to_upload(sourcepath)
		created = os.path.getctime(sourcepath)
		modified = os.path.getmtime(sourcepath)
		
#		file = open(sourcedir + '/' + filename,'rb')
#		ftpsession.storbinary('STOR ' + filename, file)
#		file.close()		

print ("File List: ")
files = ftpsession.dir()
print (files)

ftpsession.quit()

