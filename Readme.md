# URL Redirect Checker

URL Redirect Checker is a web-based tool that allows users to upload a text file containing URLs and receive an Excel file with the redirect status and the redirected URLs.

## Features

- Upload a text file with URLs.
- Check each URL for redirection.
- Generate an Excel file with the results.
- User-friendly web interface.

## Technologies Used

- Python
- Flask
- Requests
- Pandas
- TQDM
- HTML/CSS

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/srma4tech/redirect-checker.git
    cd redirect-checker
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:
    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

3. **Upload a text file with URLs**:
    - Click on the "Browse" button to select your text file containing URLs.
    - Click "Upload" to process the file.

4. **Download the resulting Excel file**:
    - Once the processing is complete, the Excel file will be available for download.

## File Structure


## Detailed Explanation

### app.py

This is the main Flask application file. It contains the following key components:

- **Imports**: Necessary libraries for handling HTTP requests, data processing, and file handling.
- **check_redirect(url)**: Function to check if a URL redirects and returns the status and redirected URL.
- **process_urls(urls)**: Function to process a list of URLs, check for redirection, and generate an Excel file in memory.
- **Flask Routes**:
  - `/`: Renders the main HTML page.
  - `/upload`: Handles file uploads, processes the URLs, and returns the Excel file for download.

### templates/index.html

This is the HTML template for the main page. It includes a form for file upload and links to the CSS file for styling.

### static/styles.css

This CSS file provides styles for the HTML template, making the UI more visually appealing.

### requirements.txt

This file lists all the Python packages required to run the application.



## Example Usage

1. **Create a text file named `urls.txt`** with the following content:
    ```
    http://example.com
    http://google.com
    http://nonexistent.url
    ```

2. **Run the Flask application**:
    ```sh
    python app.py
    ```

3. **Open your web browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

4. **Upload the `urls.txt` file**:
    - Click on the "Browse" button to select `urls.txt`.
    - Click "Upload" to process the file.

5. **Download the resulting Excel file**:
    - Once the processing is complete, the Excel file will be available for download.

## Future Enhancements

1. **Concurrency**: Implement threading or asynchronous requests to speed up URL checking.
2. **Error Handling**: Improve error handling to manage different types of HTTP errors more gracefully.
3. **User Interface**: Enhance the UI with more features, such as progress bars, status messages, and better error reporting.
4. **Logging**: Add logging to capture detailed information about the processing for debugging purposes.
5. **Deployment**: Consider deploying the application using a web server like Gunicorn or Nginx for production use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- Requests: [Requests Documentation](https://docs.python-requests.org/en/latest/)
- Pandas: [Pandas Documentation](https://pandas.pydata.org/)
- TQDM: [TQDM Documentation](https://tqdm.github.io/)
- OpenPyXL: [OpenPyXL Documentation](https://openpyxl.readthedocs.io/en/stable/)

---

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!


