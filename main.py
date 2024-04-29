# File: main.py

import os
from metadata_extractor import MetadataExtractor

if __name__ == "__main__":
    # Define paths relative to the root directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(root_dir, 'Data-Lake', 'Data')
    metadata_path = os.path.join(root_dir, 'Data-Lake', 'Metadata')

    # Create MetadataExtractor instance and extract metadata
    extractor = MetadataExtractor(source_path, metadata_path)
    extractor.extract_metadata()
