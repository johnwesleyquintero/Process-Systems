# Amazon Flatfile Assistant

### Project Overview

The "Amazon Flatfile Assistant" is a localized, user-friendly micro-application designed to help our team automate repetitive flat file tasks for Amazon operations. It uses a simple architecture combining Excel for user input and Python for data processing.

The goal of this system is to improve our team's efficiency and accuracy, reduce the time spent on manual data manipulation, and minimize common upload errors. This allows us to focus more on higher-level strategy and analysis.

### Architecture

*   **Input Template (Excel/CSV):** Simple Excel or CSV files with clear headers serve as the user's main interaction point, making data input straightforward.
*   **Transformation Engine (Python):** A set of Python scripts use the powerful `pandas` library to read the input files, perform necessary data cleaning, validation, and transformations.
*   **Launchpad (NPM Scripts):** The `package.json` file contains simple command-line scripts that act as easy-to-use "buttons," allowing any team member to trigger the Python automation without needing to write code.

### Workflow Blueprint

1.  **Prepare Input:** Fill out the relevant Excel/CSV template (e.g., `excel_templates/price_update_template.csv`) with the required data.
2.  **Run Transformation:** Open your terminal in the project root and execute the corresponding NPM script (e.g., `npm run run:price-update`).
3.  **Retrieve Output:** The generated Amazon-ready flat file will be saved in the `output/` directory, ready for review and upload to Seller Central.

### Current Capabilities

*   **Price Update Automation:**
    *   **Input:** `excel_templates/price_update_template.csv` (SKU, Old Price, New Price, Start Date, End Date)
    *   **Script:** `src/price_update.py`
    *   **Command:** `npm run run:price-update -- --brand [BRAND_NAME]` (e.g., `npm run run:price-update -- --brand SL`)
    *   **Output:** `BRANDS/[BRAND_NAME]/output/amazon_price_update_flatfile.csv`
*   **FBA Restock Recommendations:**
    *   **Purpose:** Generates strategic FBA restock recommendations based on sales velocity, inventory levels, supplier lead times, and desired safety stock. This script helps prevent stockouts and minimize overstocking.
    *   **Inputs:**
        *   `BRANDS/[BRAND_NAME]/reports/sales/sales.csv`: A tab-separated file containing historical sales data, including `order-status`, `sku`, `quantity`, and `purchase-date`.
        *   `BRANDS/[BRAND_NAME]/reports/inventory/inventory.csv`: A comma-separated file containing current inventory levels, including `sku` and `available` quantities.
    *   **Script:** `src/restock_recommender.py`
    *   **Command:** `npm run recommend:restock -- --brand [BRAND_NAME]` (e.g., `npm run recommend:restock -- --brand SL`)
    *   **Output:** `BRANDS/[BRAND_NAME]/recommendations/restock_recommendations.csv`
    *   **Logic:** The script calculates a `Reorder Point` for each SKU using the formula: `(Daily Sales Velocity * Lead Time) + Safety Stock`. If current inventory is below this point, it calculates a `Recommended Order Quantity` to meet the `Desired Days of Cover`. Key parameters like `LEAD_TIME_DAYS`, `SAFETY_STOCK_DAYS`, and `DESIRED_DAYS_OF_COVER` are configurable directly within the script.
*   **Promotional Discount Suggestions:**
    *   **Purpose:** Generates suggested promotional discounts for Amazon listings based on product age and current status. This helps in managing inventory and boosting sales without altering the base retail price.
    *   **Input:** `BRANDS/[BRAND_NAME]/all-listing-report.tsv` (current product listings)
    *   **Script:** `src/generate_promotional_suggestions.py`
    *   **Command:** `npm run generate:promotions -- --brand [BRAND_NAME]` (e.g., `npm run generate:promotions -- --brand SL`)
    *   **Output:** `BRANDS/[BRAND_NAME]/output/promotional_discount_suggestions.csv`
    *   **Logic:** The script identifies active products older than a configurable age threshold (default: 6 months) and calculates a `sale-price` by applying a configurable discount percentage (default: 15%). It also sets a `sale-start-date` (current date) and `sale-end-date` (configurable duration, default: 7 days).
*   **Listing Creation Automation:**
    *   **Purpose:** Automates the creation of Amazon-ready flat files for new product listings.
    *   **Input:** `excel_templates/new_listing_template.csv` (a template for new product data)
    *   **Script:** `src/listing_creation.py`
    *   **Command:** `npm run run:listing-creation -- --brand [BRAND_NAME]` (e.g., `npm run run:listing-creation -- --brand SL`)
    *   **Output:** `BRANDS/[BRAND_NAME]/output/amazon_new_listing_flatfile.csv`
    *   **Logic:** Reads data from the input template and generates a flat file. (Note: This is a basic placeholder; a full implementation would involve extensive data mapping and validation against Amazon's specific flatfile requirements.)
*   **Template Validation:**
    *   **Purpose:** Validates the structure and required columns of various input templates used by the automation scripts.
    *   **Input:** Specifies the template name (e.g., `price_update`, `new_listing`).
    *   **Script:** `src/template_validator.py`
    *   **Command:** `npm run validate:template -- --template [template_name] --brand [BRAND_NAME]` (e.g., `npm run validate:template -- --template price_update --brand SL`)
    *   **Output:** Console output indicating validation success or failure, including missing columns.
    *   **Logic:** Checks if the specified template file exists and contains all the necessary columns defined for that template.

### Troubleshooting

*   **FBA Restock Recommendations failing with "Could not generate recommendations due to missing data":**
    *   **Cause:** The `src/restock_recommender.py` script requires the `BRANDS/[BRAND_NAME]/reports/sales/sales.csv` file to be tab-separated and contain specific columns (`order-status`, `sku`, `quantity`, `purchase-date`).
    *   **Solution:** Ensure that the `sales.csv` file is properly formatted with tab separators and includes the required columns.

### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/johnwesleyquintero/Process-Systems.git
    cd Process-Systems
    ```
2.  **Install Python Dependencies:**
    ```bash
    pip install pandas openpyxl
    ```
3.  **Install Node.js Dependencies (for NPM scripts):**
    ```bash
    npm install
    ```

### How to Use

1.  **Select a Task:** Identify the flat file task you need to automate (e.g., Price Update).
2.  **Prepare Input Data:** Navigate to the `excel_templates/` directory and open the relevant template file. Input your data according to the column headers.
3.  **Run the Script:** From the project root directory in your terminal, run the corresponding NPM script:
    ```bash
    npm run run:price-update
    ```
    (Replace `run:price-update` with the appropriate script for other tasks as they are added.)
4.  **Check Output:** The generated flat file will be saved in the `output/` directory. Review it before uploading to Amazon Seller Central.

### Future Improvements

*   **Adding New Tasks:** The framework is designed to be easily expandable. New automation scripts for tasks like inventory updates or new listings can be added following the modular design.
*   **Enhanced Error Handling:** Scripts can be improved to provide even more user-friendly error messages for invalid data formats.

### Contribution

Contributions from the team are welcome! Please follow the existing modular design principles when adding new flat file automation tasks.
