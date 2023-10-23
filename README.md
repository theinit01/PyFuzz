# PyFuzz
#🐍 PyFuzz - Python Subdomain and Directory Fuzzer
PyFuzz is a lightweight and efficient Python-based subdomain and directory fuzzer tool that helps in finding hidden subdomains and directories on a target website.
## Installation
To use PyFuzz, you'll need to have Python 3 installed on your system. You can download and install Python 3 from the official Python website.

Once you have Python 3 installed, follow these steps to install PyFuzz:

1. Clone the PyFuzz repository to your local system using git clone https://github.com/theinit01/PyFuzz.git or download the source code from the repository and extract it to a local directory.
2. Navigate to the PyFuzz directory in your terminal/command prompt.
3. Install the required Python modules using ```pip install -r requirements.txt.```

## Usage
To use PyFuzz, follow these steps:
1. Navigate to the PyFuzz directory in your terminal/command prompt.
2. Run python pyfuzz.py -h to view the help menu and see the available options.
3. Use the -u option to specify the target URL, -w option to specify the wordlist, and other options as required.
4. Wait for PyFuzz to complete scanning the target website.
5. Review the results in the specified output format, such as CSV, JSON, or plain text.

## Rate Limiting Feature
We've recently added a rate limiting feature to PyFuzz. This feature helps control the number of requests per second, preventing overload of the target server. Rate limiting is an important consideration to avoid inadvertently affecting the availability of the target.

## Contributing
PyFuzz is an open-source project and welcomes contributions from the community. To contribute to PyFuzz, please follow these steps:

1. Fork the PyFuzz repository to your own account.
2. Create a new branch for your changes.
3. Make your changes and commit them with a descriptive commit message.
4. Push your changes to your forked repository.
5. Create a pull request to the original PyFuzz repository.
