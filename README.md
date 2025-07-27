# Amazon Flatfile & Systems Assistant

### Project Overview

The "Amazon Systems Assistant" is a localized, user-friendly micro-application designed to help our team automate repetitive tasks and generate intelligent reports for Amazon operations. It uses a simple architecture combining Excel for user interaction and Python for data processing and systems generation.

The goal of this system is to improve our team's efficiency and accuracy, reduce the time spent on manual work, and elevate our focus from simple data entry to high-level strategy and analysis.

### Architecture

*   **Input Layer (Excel/CSV):** Simple, non-threatening Excel or CSV files serve as the user's main interaction point.
*   **Processing Engine (Python):** A powerful suite of Python scripts that function as the "brain" of the operation. They read inputs, perform complex calculations, blend data, and forge new files.
*   **Launchpad (NPM Scripts):** The `package.json` file contains simple command-line scripts that act as easy-to-use "buttons," allowing any team member to trigger the Python automation without needing to write code.

### Workflow Blueprint

1.  **Select a Task:** Identify the process you need to run (e.g., generate a restock report, create a pricing template).
2.  **Prepare Input (if necessary):** For some scripts, you may need to fill out a simple Excel/CSV template.
3.  **Run Command:** Open your terminal in the project root and execute the corresponding NPM script (e.g., `npm run forge:restock-recommender`).
4.  **Retrieve Output:** The generated Excel template or Amazon-ready flat file will be saved in the `excel_templates/` or `output/` directory, ready for use.

---

## The Pythonic Arsenal: Current Capabilities

This repository contains two primary types of systems: **Flatfile Generators** for direct Amazon uploads, and **Template Forges** for creating intelligent analysis tools.

### Flatfile Generation Suite

*(This section contains the existing scripts for generating Amazon-ready flat files.)*

*   **Price Update Automation:** ... *(logic remains the same)*
*   **FBA Restock Recommendations:** ... *(logic remains the same)*
*   **Promotional Discount Suggestions:** ... *(logic remains the same)*
*   **Listing Creation Automation:** ... *(logic remains the same)*
*   **Template Validation:** ... *(logic remains the same)*

---

### Excel Template Generation Suite (The Trojan Horses)

This suite of scripts doesn't generate flat files; it forges powerful, intelligent Excel templates from scratch. These templates are designed to look like simple spreadsheets but contain sophisticated, data-driven logic to automate analysis and guide strategic decision-making.

*   **Buy Box Dominance Tracker**
    *   **Purpose:** Forges the `Buy_Box_Dominance_Tracker.xlsx`, an intelligent dashboard that analyzes sales and traffic data to automatically prioritize ASINs that are losing the Buy Box and suggests corrective actions. It transforms a reactive monitoring task into a proactive, strategic operation.
    *   **Script:** `src/forge_trojan_horse.py`
    *   **Command:** `npm run forge:buybox-tracker`
    *   **Output:** `excel_templates/Buy_Box_Dominance_Tracker_v1.1.xlsx`
    *   **Template Usage:** Paste the 'Detail Page Sales & Traffic' report into the `Data_Input` tab. The `Buy_Box_Dashboard` will auto-populate, highlighting critical issues in red and suggesting priority levels.

*   **Restock Recommender**
    *   **Purpose:** Forges the `Restock_Recommender.xlsx`, a complete supply chain command center. It blends data from FBA Inventory and Business Reports to calculate `Days of Supply` and provide a precise, 60-day forecast for `Recommended Units` to order. It includes a "Forecast Control Panel" to model for holidays and promotions.
    *   **Script:** `src/forge_restock_report.py`
    *   **Command:** `npm run forge:restock-recommender`
    *   **Output:** `excel_templates/Restock_Recommender_v1.2.xlsx`
    *   **Template Usage:** Paste the FBA Inventory and Business Report data into their respective `Data_Input` tabs. The `Restock_Dashboard` will provide a full, actionable restocking plan.

*   **Listing Health & Sentiment Report Template**
    *   **Purpose:** Forges the `Listing_Health_Sentiment_Report.xlsx`, a structured framework for conducting deep-dive analysis. It turns a vague "freestyle" request into a rigorous, multi-source investigation tool.
    *   **Script:** `src/forge_sentiment_report.py`
    *   **Command:** `npm run forge:sentiment-report`
    *   **Output:** `excel_templates/Listing_Health_Sentiment_Report_v1.0.xlsx`
    *   **Template Usage:** Paste data from VOC, Business Reports, and competitor analysis into the input tabs. Use the `ASIN_Deep_Dive` tab to consolidate findings and formulate a final recommendation.

*   **Surgical Strike Profitability Calculator**
    *   **Purpose:** Forges the `Surgical_Strike_Calculator.xlsx`, a simple but ruthless tool designed to calculate the exact profitability of a proposed discount. It serves as a mathematical "truth machine" to prevent money-losing promotions.
    *   **Script:** `src/forge_calculator.py`
    *   **Command:** `npm run forge:promo-calculator`
    *   **Output:** `excel_templates/Surgical_Strike_Calculator_v1.0.xlsx`
    *   **Template Usage:** Input the product's price, costs, fees, and a proposed discount percentage. The calculator will instantly display the final profit per unit and a "LOSING MONEY!" warning if applicable.

*(...The rest of the `README.md` for Troubleshooting, Installation, etc., remains the same...)*
