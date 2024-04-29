# Heterogeneous Data Metadata Extraction Framework for Data Lake
An comprehensive metadata extraction framework designed and implemented in Python. It efficiently extracts metadata from heterogeneous data sources within a Data Lake environment.

## Overview
Data Lakes are repositories that store vast amounts of structured, semi-structured, and unstructured data from various sources. Extracting metadata from such diverse data sources is crucial for data governance, discovery, and analysis. 

## Features 
- Heterogeneous Extraction: DataLake MetaHarvest can extract metadata from any file type, including structured, semi-structured, and unstructured data formats.
- Comprehensive Metadata: The framework extracts business, technical, and operational metadata, providing a holistic view of the data within the Data Lake. 

## Setup and Installation
 1. Clone the repository
 ``` bash
 git clone https://github.com/NageshVk/Heterogeneous-Data-Metadata-Extraction-Framework-for-Data-Lake.git
```

2. Install the required dependencies
```bash
pip install -r requirements.txt
```

3. Run the extraction script
``` bash
python main.py
```

## Usage
1. Place your data files in the Data Lake/Data directory.
2. Open main.py and customize the metadata extraction process based on your specific requirements, if necessary.
3. Metadata files will be generated in the Data Lake/Metadata directory.

### Example Usage
```python
import Heterogeneous_Data_Metadata_Extraction_Framework_for_Data_Lake as hdme

# Example code for metadata extraction
metadata = hdme.extract_metadata('data_file.csv')
print(metadata)
```
## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


