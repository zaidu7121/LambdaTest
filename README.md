# Selenium Automation - Firefox  

## Documentation  

### Overview  
This project automates the validation of the **Table Search Demo**** page on the [Selenium Playground](https://www.lambdatest.com/selenium-playground/table-sort-search-demo) using **Selenium WebDriver with Firefox**.  

### Features  
✔ Opens the Table Search Demo page.  
✔ Inputs `"New York"` into the search box.  
✔ Verifies that the search results display **5 matching entries**.  

### Usage  
1. Ensure **Firefox** is installed and **GeckoDriver** is configured (refer to `requirements.txt`).  
2. Run the test with:  
   ```bash
   pytest qa_selenium_test.py
   ```  

### Expected Output  
- The test **passes** if exactly **5 entries** appear in the search results.  
- Otherwise, it **fails** with an assertion error.  

For dependencies and setup, check **requirements.txt**.  


Let me know if you need any modifications! 
