# File: metadata_extractor.py

import os
import json
from tinytag import TinyTag
from PyPDF2 import PdfFileReader
from PIL import Image
from PIL.ExifTags import TAGS

class MetadataExtractor:
    def __init__(self, source_path, metadata_path):
        self.source_path = source_path
        self.metadata_path = metadata_path

    def extract_audio_metadata(self, file_name):
        audio = TinyTag.get(file_name)
        metadata = {
            "Technical Metadata": {
                "Bit rate": audio.bitrate,
                "File Size": audio.filesize
            },
            "Business Metadata": {
                "Title": audio.title,
                "Artist": audio.artist,
                "Genre": audio.genre,
                "Album Artist": audio.albumartist
            },
            "Operational Metadata": {
                "Composer": audio.composer,
                "Duration": audio.duration,
                "Track Total": audio.track_total,
                "Year Released": audio.year
            }
        }
        return metadata

    def extract_video_metadata(self, file_name):
        video = TinyTag.get(file_name)
        metadata = {
            "Technical Metadata": {
                "Bit rate": video.bitrate,
                "File Size": video.filesize
            },
            "Business Metadata": {
                "Title": video.title,
                "Artist": video.artist,
                "Genre": video.genre,
                "Album Artist": video.albumartist
            },
            "Operational Metadata": {
                "Composer": video.composer,
                "Duration": video.duration,
                "Track Total": video.track_total,
                "Year Released": video.year
            }
        }
        return metadata

    def extract_image_metadata(self, file_name):
        image = Image.open(file_name)
        exif_data = image._getexif()
        metadata = {"EXIF": {}}
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata["EXIF"][tag_name] = value
        return metadata

    def extract_pdf_metadata(self, file_name):
        with open(file_name, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            metadata = {
                "Business Metadata": {
                    "Author": info.author,
                    "Subject": info.subject,
                    "Title": info.title,
                    "Producer": info.producer
                },
                "Operational Metadata": {
                    "Creation Date": str(info.creation_date),
                    "Modification Date": str(info.modification_date)
                }
            }
        return metadata

    def extract_metadata(self):
        os.chdir(self.source_path)
        for file_name in os.listdir():
            metadata = None
            if file_name.endswith((".mp3", ".mp4")):
                if file_name.endswith(".mp3"):
                    metadata = self.extract_audio_metadata(file_name)
                else:
                    metadata = self.extract_video_metadata(file_name)
            elif file_name.endswith((".jpg", ".jpeg", ".png")):
                metadata = self.extract_image_metadata(file_name)
            elif file_name.endswith(".pdf"):
                metadata = self.extract_pdf_metadata(file_name)

            if metadata:
                metadata_file_name = os.path.splitext(file_name)[0] + "_metadata.json"
                metadata_file_path = os.path.join(self.metadata_path, metadata_file_name)

                os.makedirs(os.path.dirname(metadata_file_path), exist_ok=True)

                with open(metadata_file_path, "w") as file_object:
                    json.dump(metadata, file_object)
