# Amazon Flatfile Alchemist

## Project Overview

The "Amazon Flatfile Alchemist" is a localized, user-friendly micro-application designed to automate repetitive, high-volume flatfile tasks for Amazon operations. It leverages a powerful and practical architecture combining Excel for user input, Python for robust data transformation, and NPM scripts for easy execution. This system aims to liberate Amazon specialists from mindless, error-prone manual data manipulation, allowing them to focus on higher-level strategy and analysis.

This project embodies the "Heretic's Codex" by turning a grinding agency task into a systemic advantage, providing "Sovereignty" in action by automating critical workflows.

## Architecture

*   **Input Template (Excel/CSV):** Structured Excel or CSV files serve as the user's interaction point, allowing easy input and pasting of data. Designed for simplicity with clear headers and validation hints.
*   **Transformation Engine (Python):** Python scripts, primarily using the `pandas` library, read the input, perform necessary data cleaning, validation, and complex transformations, and generate Amazon-specific flatfiles.
*   **Launchpad (NPM Scripts):** `package.json` defines simple command-line scripts that act as "buttons" for users to trigger the Python automation with ease.

## Workflow Blueprint

1.  **Prepare Input:** Fill out the relevant Excel/CSV template (e.g., `excel_templates/price_update_template.csv`) with the data for your task.
2.  **Run Transformation:** Open your terminal in the project root and execute the corresponding NPM script (e.g., `npm run run:price-update`).
3.  **Retrieve Output:** The transformed Amazon flatfile will be generated in the `output/` directory, ready for upload to Amazon Seller Central.

## Current Capabilities

*   **Price Update Automation:**
    *   **Input:** `excel_templates/price_update_template.csv` (SKU, Old Price, New Price, Start Date, End Date)
    *   **Script:** `src/price_update.py`
    *   **Command:** `npm run run:price-update`
    *   **Output:** `output/amazon_price_update_flatfile.csv`

## Installation and Setup

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

## How to Use

1.  **Select a Task:** Identify the Amazon flatfile task you need to automate (e.g., Price Update).
2.  **Prepare Input Data:** Navigate to the `excel_templates/` directory and open the relevant template file (e.g., `price_update_template.csv`). Input your data according to the column headers.
3.  **Run the Script:** From the project root directory in your terminal, run the corresponding NPM script:
    ```bash
    npm run run:price-update
    ```
    (Replace `run:price-update` with the appropriate script for other tasks as they are added.)
4.  **Check Output:** The generated flatfile will be saved in the `output/` directory. Review it before uploading to Amazon Seller Central.

## Strategic Considerations & Future Expansion

*   **Modular Design:** Each distinct flatfile task (e.g., inventory update, new listing, product content update) will have its own dedicated Python script and Excel/CSV template, ensuring maintainability and scalability.
*   **Error Handling:** Scripts are designed to provide user-friendly error messages and, where applicable, generate error reports for invalid data.
*   **Version Control:** The entire project is under Git version control to track changes, facilitate collaboration, and enable easy rollbacks.
*   **Scalability:** This framework is built to be easily expandable, anticipating the addition of many more manual tasks as Amazon specialists' needs evolve. Future integrations with web-based interfaces or data ingestion layers are possible.

## Contribution

Contributions are welcome! Please follow the modular design principles when adding new flatfile automation tasks.
