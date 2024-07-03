# Daft.ie Property Scraper

This project automates the process of searching and applying for rental properties listed on Daft.ie. The script uses Selenium to interact with the website and Schedule to run the script at specified intervals. The purpose of this project is to enhance the likelihood of receiving a response from landlords by automating and expediting the application process. Given the high volume of rental applications, being among the first to apply can significantly increase your chances of securing your desired property.



**Prerequisites**

Before you begin, ensure you have the following installed on your local machine:

* Python 3.x
* Google Chrome browser
* ChromeDriver (ensure the version matches your installed Chrome browser)



**Installation**

1. Clone the Repository:
```
git clone https://github.com/your-username/daft-property-scraper.git
cd daft-property-scraper
```

2. Create a Virtual Environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install Dependencies:
```
pip install -r requirements.txt
```



**Usage**

Before running the script, make sure to configure the necessary details such as login credentials and other required fields.



**Configuration**

Update the following variables in the script with your details:

* username.send_keys("your_email@example.com")
* password.send_keys("your_password")
* Other form fields such as name, email, phone number, and message content in the apply function.



**Running the Script**

To run the script locally, execute:
```
python main.py
```



**Main Program**

1. Open Chrome:
   
The script will open Google Chrome using Selenium WebDriver.

3. Sign In:
   
The script will sign in to Daft.ie using the provided credentials.

5. Search and Apply:
   
The script will search for rental properties and apply to the ones that have not been applied to before.

7. Scheduling(Optional):
   
The script uses the schedule library to run the main_program function at specified intervals.



**Troubleshooting**

* ChromeDriver Compatibility:
Ensure the ChromeDriver version matches your installed Chrome browser version. You can download the appropriate version from ChromeDriver.

* Timeouts and NoSuchElementExceptions:
If you encounter timeouts or element not found errors, review the XPath and CSS selectors used in the script. Elements on the webpage may have changed.

* Login Issues:
Ensure the provided login credentials are correct and the login process is as expected.



**Contributing**

If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.



**License**

This project is licensed under the MIT License.

**Notes:** Replace "your-username" in the clone URL with your actual GitHub username and adjust the instructions as necessary to match your project's specifics.
