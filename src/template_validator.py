import pandas as pd
import argparse
import os

def validate_template(template_name, brand_name=None):
    """
    Validates the structure and content of a specified input template.

    Args:
        template_name (str): The name of the template to validate (e.g., 'price_update', 'new_listing').
        brand_name (str, optional): The brand name if the template is brand-specific.
    """
    template_paths = {
        'price_update': 'excel_templates/price_update_template.csv',
        'new_listing': 'excel_templates/new_listing_template.csv',
        'all_listing_report': os.path.join('BRANDS', brand_name, 'all-listing-report.tsv') if brand_name else None,
        'sales_report': os.path.join('BRANDS', brand_name, 'reports', 'sales', 'sales.csv') if brand_name else None,
        'inventory_report': os.path.join('BRANDS', brand_name, 'reports', 'inventory', 'inventory.csv') if brand_name else None
        # Add other templates here as they are created
    }

    if template_name not in template_paths or (template_paths[template_name] is None and brand_name is None):
        print(f"Error: Template '{template_name}' not recognized or brand name is missing for a brand-specific template. Available templates: {', '.join(template_paths.keys())}")
        return

    input_file_path = template_paths[template_name]

    try:
        df = pd.read_csv(input_file_path)

        # Define expected columns for each template
        expected_columns = {
            'price_update': ['sku', 'Old Price', 'New Price', 'Start Date', 'End Date'],
            'new_listing': ['seller-sku', 'product-id', 'product-id-type', 'item-name', 'item-description', 'price', 'quantity', 'fulfillment-channel'],
            'all_listing_report': ['item-name', 'item-description', 'listing-id', 'seller-sku', 'price', 'quantity', 'open-date', 'image-url', 'item-is-marketplace', 'product-id-type', 'zshop-shipping-fee', 'item-note', 'item-condition', 'zshop-category1', 'zshop-browse-path', 'zshop-storefront-feature', 'asin1', 'asin2', 'asin3', 'will-ship-internationally', 'expedited-shipping', 'zshop-boldface', 'product-id', 'bid-for-featured-placement', 'add-delete', 'pending-quantity', 'fulfillment-channel', 'merchant-shipping-group', 'status'],
            'sales_report': ['order-id', 'order-item-id', 'purchase-date', 'payments-date', 'reporting-date', 'currency', 'item-price', 'shipping-price', 'gift-wrap-price', 'item-tax', 'shipping-tax', 'gift-wrap-tax', 'regulatory-fee', 'tax-collection-model', 'is-business-order', 'purchase-order-number', 'price-designation', 'sku', 'item-name', 'quantity', 'fulfillment-channel', 'ship-city', 'ship-state', 'ship-postal-code', 'ship-country', 'order-status'],
            'inventory_report': ['sku', 'asin', 'product-name', 'condition', 'your-price', 'mfn-listing-exists', 'mfn-fulfillable-quantity', 'afn-listing-exists', 'afn-warehouse-quantity', 'afn-fulfillable-quantity', 'afn-unsellable-quantity', 'afn-reserved-quantity', 'afn-total-quantity', 'per-unit-volume', 'afn-inbound-working-quantity', 'afn-inbound-shipped-quantity', 'afn-inbound-receiving-quantity', 'afn-researching-quantity', 'afn-reserved-future-supply', 'afn-reserved-unsellable', 'afn-researching-quantity-tbd', 'afn-researching-quantity-resolved', 'listing-id', 'open-date', 'quantity', 'product-id-type', 'product-id', 'will-ship-internationally', 'expedited-shipping', 'zshop-boldface', 'zshop-shipping-fee', 'item-note', 'item-condition', 'zshop-category1', 'zshop-browse-path', 'zshop-storefront-feature', 'asin1', 'asin2', 'asin3']
        }

        if template_name in expected_columns:
            missing_columns = [col for col in expected_columns[template_name] if col not in df.columns]
            if missing_columns:
                print(f"Validation failed for '{template_name}' template: Missing required columns: {', '.join(missing_columns)}")
                return
            else:
                print(f"Validation successful for '{template_name}' template: All required columns are present.")
                # Add more specific data validation rules here (e.g., data types, value ranges)
                # For example:
                # if template_name == 'price_update':
                #     if not pd.api.types.is_numeric_dtype(df['New Price']):
                #         print("Warning: 'New Price' column contains non-numeric values.")
        else:
            print(f"Warning: No specific validation rules defined for template '{template_name}'. Only basic file reading performed.")

    except FileNotFoundError:
        print(f"Error: Template file not found at {input_file_path}. Please ensure it exists.")
    except pd.errors.EmptyDataError:
        print(f"Error: Template file at {input_file_path} is empty.")
    except Exception as e:
        print(f"An unexpected error occurred during validation: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Amazon flatfile templates.")
    parser.add_argument('--template', type=str, required=True, help="The name of the template to validate (e.g., 'price_update', 'new_listing', 'all_listing_report').")
    parser.add_argument('--brand', type=str, help="The brand name (e.g., 'SL', 'STK') for brand-specific templates.")
    args = parser.parse_args()

    validate_template(args.template, args.brand)
