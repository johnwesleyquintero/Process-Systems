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
    *   **Command:** `npm run run:price-update`
    *   **Output:** `output/amazon_price_update_flatfile.csv`
*   **FBA Restock Recommendations:**
    *   **Purpose:** Generates strategic FBA restock recommendations based on sales velocity, inventory levels, supplier lead times, and desired safety stock. This script helps prevent stockouts and minimize overstocking.
    *   **Inputs:**
        *   `SECULIFE/reports/sales/sales.csv`: A tab-separated file containing historical sales data, including `sku`, `quantity`, and `purchase-date`.
        *   `SECULIFE/reports/inventory/inventory.csv`: A comma-separated file containing current inventory levels, including `sku` and `available` quantities.
    *   **Script:** `src/restock_recommender.py`
    *   **Command:** `npm run recommend:restock`
    *   **Output:** `SECULIFE/recommendations/restock_recommendations.csv`
    *   **Logic:** The script calculates a `Reorder Point` for each SKU using the formula: `(Daily Sales Velocity * Lead Time) + Safety Stock`. If current inventory is below this point, it calculates a `Recommended Order Quantity` to meet the `Desired Days of Cover`. Key parameters like `LEAD_TIME_DAYS`, `SAFETY_STOCK_DAYS`, and `DESIRED_DAYS_OF_COVER` are configurable directly within the script.

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
