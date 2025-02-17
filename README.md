# Selenium Automation - Firefox/Chrome

## Documentation

### Overview  
This project automates the validation of the **Table Search Demo** page on the [Selenium Playground](https://www.lambdatest.com/selenium-playground/table-sort-search-demo) using **Selenium WebDriver with Firefox/Chrome**.

### Features  
✔ Opens the Table Search Demo page.  
✔ Inputs `"New York"` into the search box.  
✔ Verifies that the search results display **5 matching entries**.

### Usage  
1. Ensure **Google Chrome** or **Firefox 135.0** is installed and the corresponding driver (**ChromeDriver** or **GeckoDriver**) is configured (refer to `requirements.txt`).
2. This project uses **pytest** for test execution.  
3. The code follows **PEP8** standards for clean and readable Python code.  

### Expected Output  
- The test **passes** if exactly **5 entries** appear in the search results.  
- Otherwise, it **fails** with an assertion error.

For dependencies and setup, check **requirements.txt**.
