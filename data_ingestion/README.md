
# Data Ingestion Scripts Overview

This directory contains scripts related to data ingestion, showcasing both a new and an old approach to handling data ingestion processes. These scripts are part of the data pipeline that feeds into our system, designed with error handling and project layout restructuring in mind.

## Files Description

- `data_ingestion_test_new.py`: This is the latest version of our data ingestion script. It includes enhanced error handling mechanisms and a restructured project layout for improved maintainability and scalability. This script should be used for all new data ingestion tasks.

- `data_ingestion_test_old.py`: This script represents the previous approach to data ingestion. It's kept for historical reference and backward compatibility reasons. However, it's recommended to use the new script for future data ingestion efforts.

## Getting Started

To use these scripts, you will need Python installed on your system along with necessary dependencies which can be found in the `requirements.txt` file at the root of the project. 

### Installation

1. Ensure Python and pip are installed on your system.
2. Install the required Python packages:

```bash
pip3 install pulsar-client   
pip3 install selenium pandas psycopg2-binary webdriver-manager
```

### Usage

To run the new data ingestion script, execute the following command from the terminal:

```bash
python data_ingestion_test_new.py
```

For the old data ingestion script, use:

```bash
python data_ingestion_test_old.py
```

## Important Notes

- Always ensure you're using the correct script for your data ingestion needs. The new script (`data_ingestion_test_new.py`) is preferred for its advanced error handling and improved project layout.
- The old script (`data_ingestion_test_old.py`) is maintained for legacy purposes and might not receive further updates :)


