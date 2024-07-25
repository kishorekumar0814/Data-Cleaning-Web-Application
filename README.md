# Data Cleaning Web Application

## Overview

This project is a web application designed for automated data cleaning. It allows users to upload datasets in CSV or XLSX format, processes the data to handle missing values and remove duplicates, and provides the cleaned dataset for download. The application is built using the Flask framework for web development and the Pandas library for data processing.

## Features

- Upload CSV or XLSX files
- Automatically clean data by handling missing values and removing duplicates
- Download the cleaned dataset in the same format as the input file

## Technologies Used

- **Flask**: A lightweight Python web framework for building the web application.
- **Pandas**: A data manipulation library in Python for processing and cleaning data.
- **openpyxl**: A library for reading and writing Excel files (XLSX format).

## Requirements

- Python 3.7 or higher
- Flask
- Pandas
- openpyxl

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/data-cleaning-webapp.git
   cd data-cleaning-webapp
2. **Set Up a Virtual Environment (Recommended)**
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Required Packages**
    ```bash
   pip install flask pandas openpyxl

## Configuration
1. Create a .env File (Optional, for custom configurations)

    #### Create a .env file in the root directory of the project if you need to set environment   variables. For example:
        FLASK_ENV=development

## Running the Application
1. **Start the Flask Server**
   ```bash
   python app.py
  
  By default, the Flask server will run on http://127.0.0.1:5000/.

2. **Access the Application**

      Open your web browser and navigate to http://127.0.0.1:5000/. You will see the file upload form.

3. **Upload a Dataset**

      Use the form to upload a CSV or XLSX file. The application will process the file and provide a cleaned dataset for download.

## Project Structure
    data-cleaning-webapp/
    │
    ├── app.py                  # Main application file
    ├── templates/
    │   ├── index.html           # HTML template for file upload
    ├── static/
    │   └── style.css            # CSS for styling (if any)
    ├── requirements.txt        # List of required Python packages
    └── README.md               # This file


## Testing
1. **Run Unit Tests (if applicable)**

   #### If you have unit tests in your project, you can run them using:
        pytest

## Troubleshooting
  **Missing Dependencies**: Ensure all required packages are installed. Run pip install -r       requirements.txt to install them.

  **File Upload Issues**: Verify that the file format is supported (CSV or XLSX) and that the file is not corrupted.

## Contributing
  Feel free to contribute to the project by submitting issues or pull requests. For detailed contribution guidelines, please refer to **CONTRIBUTING.md.**

## License
  This project is licensed under the **MIT License**. See the **LICENSE** file for more details.

#### _Project Report :_ [Data Cleaning Web Application Project Report.docx](https://github.com/user-attachments/files/16382152/Data.Cleaning.Web.Application.Project.Report.docx)


...

## Contact

- **Email**: [Mail me](mailto:kishorekumar1409@gmail.com)
- **GitHub**: [GitHub Profile](https://github.com/kishorekumar0814/)
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/kishorekumar1409/)
