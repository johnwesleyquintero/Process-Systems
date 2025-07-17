import csv
from datetime import datetime, timedelta
from collections import defaultdict

def parse_sales_data(sales_file_path):
    sales_velocity = defaultdict(lambda: {"total_quantity": 0, "days_sold": set()})
    try:
        with open(sales_file_path, 'r', encoding='utf-8') as f:
            # sales.csv is comma-separated
            reader = csv.DictReader(f)
            for row in reader:
                sku = row.get('sku')
                quantity = int(row.get('quantity', 0))
                open_date_str = row.get('purchase-date')

                if sku and quantity > 0 and open_date_str:
                    try:
                        # Parse date, handling potential timezone info like 'PDT'
                        # We'll strip timezone info for simplicity if present
                        date_part = open_date_str.split(' ')[0]
                        sale_date = datetime.strptime(date_part, '%Y-%m-%d')
                        sales_velocity[sku]["total_quantity"] += quantity
                        sales_velocity[sku]["days_sold"].add(sale_date.date())
                    except ValueError:
                        # Handle cases where date format might be unexpected
                        continue
    except FileNotFoundError:
        print(f"Error: Sales file not found at {sales_file_path}")
        return None
    except Exception as e:
        print(f"Error processing sales file: {e}")
        return None
    return sales_velocity

def parse_inventory_data(inventory_file_path):
    inventory_levels = {}
    try:
        with open(inventory_file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f) # Assuming comma-separated for inventory
            for row in reader:
                sku = row.get('sku') # Assuming 'sku' is the column name for SKU
                # Assuming 'quantity available' or similar is the column for available inventory
                available_quantity = 0
                try:
                    available_quantity = int(row.get('available', 0))
                except ValueError:
                    continue
                
                if sku and available_quantity >= 0:
                    inventory_levels[sku] = available_quantity
    except FileNotFoundError:
        print(f"Error: Inventory file not found at {inventory_file_path}")
        return None
    except Exception as e:
        print(f"Error processing inventory file: {e}")
        return None
    return inventory_levels

def generate_restock_recommendations(sales_data, inventory_data, restock_threshold_days=30):
    recommendations = []
    if not sales_data or not inventory_data:
        return recommendations

    for sku, sales_info in sales_data.items():
        total_quantity_sold = sales_info["total_quantity"]
        days_with_sales = len(sales_info["days_sold"])

        if days_with_sales == 0:
            continue # Skip if no sales data

        # Calculate average daily sales
        # We use days_with_sales to get a more accurate average if sales are not daily
        avg_daily_sales = total_quantity_sold / days_with_sales

        if avg_daily_sales <= 0:
            continue # Skip if average daily sales is zero or negative

        current_inventory = inventory_data.get(sku, 0)

        # Calculate days of supply
        days_of_supply = current_inventory / avg_daily_sales if avg_daily_sales > 0 else float('inf')

        # Generate recommendation if days of supply is below threshold
        if days_of_supply < restock_threshold_days:
            recommendations.append({
                "sku": sku,
                "avg_daily_sales": round(avg_daily_sales, 2),
                "current_inventory": current_inventory,
                "days_of_supply": round(days_of_supply, 2),
                "restock_needed_in_days": max(0, int(restock_threshold_days - days_of_supply)),
                "recommendation": f"Restock recommended. {int(days_of_supply)} days of supply remaining."
            })
    
    # Sort recommendations by days needed to restock (ascending)
    recommendations.sort(key=lambda x: x["restock_needed_in_days"])
    
    return recommendations

def save_recommendations(recommendations, output_file_path):
    if not recommendations:
        print("No restock recommendations generated.")
        return

    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ["sku", "avg_daily_sales", "current_inventory", "days_of_supply", "restock_needed_in_days", "recommendation"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(recommendations)
        print(f"Restock recommendations saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving recommendations: {e}")

if __name__ == "__main__":
    sales_file_path = "../reports/sales/sales.csv"
    inventory_file_path = "../reports/inventory/inventory.csv"
    recommendations_output_path = "../recommendations/restock_recommendations.csv"

    print(f"Analyzing sales data from: {sales_file_path}")
    sales_data = parse_sales_data(sales_file_path)
    
    print(f"Analyzing inventory data from: {inventory_file_path}")
    inventory_data = parse_inventory_data(inventory_file_path)

    if sales_data and inventory_data:
        print("Sales SKUs:", list(sales_data.keys()))
        print("Inventory SKUs:", list(inventory_data.keys()))
        print("Generating restock recommendations...")
        restock_recommendations = generate_restock_recommendations(sales_data, inventory_data)
        save_recommendations(restock_recommendations, recommendations_output_path)
    else:
        print("Could not generate recommendations due to missing data.")
