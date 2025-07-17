import csv
from collections import defaultdict
import argparse
import os

def analyze_tsv_data(brand_name):
    file_path = os.path.join('BRANDS', brand_name, 'all-listing-report.tsv')
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: Input file not found at {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

    if not data:
        return "No data found in the file."

    # Total number of items
    total_items = len(data)

    # Price analysis
    prices = []
    for item in data:
        try:
            price = float(item.get('price', '0').replace(',', ''))
            prices.append(price)
        except ValueError:
            continue # Skip items with invalid price

    min_price = min(prices) if prices else 0
    max_price = max(prices) if prices else 0
    avg_price = sum(prices) / len(prices) if prices else 0

    # Status distribution
    status_counts = defaultdict(int)
    for item in data:
        status_counts[item.get('status', 'UNKNOWN')] += 1

    # Item type categorization (simple approach based on keywords in item-name)
    item_types = defaultdict(int)
    for item in data:
        name = item.get('item-name', '').lower()
        if 'kids' in name or 'child' in name:
            item_types['Kids Trackers'] += 1
        elif 'elderly' in name or 'senior' in name or 'medical alert' in name or 'dementia' in name or 'alzheimer' in name:
            item_types['Elderly/Medical Trackers'] += 1
        elif 'vehicle' in name or 'car' in name or 'truck' in name or 'rv' in name or 'motorcycle' in name or 'obd' in name:
            item_types['Vehicle Trackers'] += 1
        elif 'wristband' in name or 'smartwatch' in name:
            item_types['Wearable Trackers'] += 1
        elif 'magnetic case' in name or 'case' in name:
            item_types['Accessories'] += 1
        else:
            item_types['Other/General Trackers'] += 1

    # Open date range
    open_dates = [item.get('open-date', '') for item in data if item.get('open-date')]
    min_open_date = min(open_dates) if open_dates else "N/A"
    max_open_date = max(open_dates) if open_dates else "N/A"

    insights = {
        "Total Items": total_items,
        "Price Statistics": {
            "Minimum Price": f"${min_price:.2f}",
            "Maximum Price": f"${max_price:.2f}",
            "Average Price": f"${avg_price:.2f}"
        },
        "Item Status Distribution": dict(status_counts),
        "Categorization of Items": dict(item_types),
        "Open Date Range": {
            "Earliest Open Date": min_open_date,
            "Latest Open Date": max_open_date
        }
    }
    return insights

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze TSV data for a specific brand.")
    parser.add_argument('--brand', type=str, default='SL', help="The brand name (e.g., 'SL', 'STK').")
    args = parser.parse_args()

    analysis_results = analyze_tsv_data(args.brand)
    if analysis_results:
        import json
        print(json.dumps(analysis_results, indent=4))
