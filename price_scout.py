import pandas as pd
import random
import time

# --- 1. Web Scraping Module (Simulation) ---
# These functions simulate data extraction from two different e-commerce sites.
# In a real project, this is where you would use BeautifulSoup, Scrapy, or Selenium.

def scrape_site_A():
    """Simulates scraping the product data from E-commerce Site A."""
    print("Scraping data from ElectroMart.com...")
    # Simulate slight price variation (dynamic data)
    price = round(random.uniform(125.00, 135.00), 2)
    time.sleep(0.1) # Simulate network delay
    return {
        'product': 'Noise Cancelling Headphones (Model X)',
        'price': price,
        'rating': 4.5,
        'seller': 'ElectroMart.com',
        'timestamp': pd.Timestamp.now()
    }

def scrape_site_B():
    """Simulates scraping the product data from E-commerce Site B."""
    print("Scraping data from TechDeals.co...")
    price = round(random.uniform(130.00, 140.00), 2)
    time.sleep(0.1) # Simulate network delay
    return {
        'product': 'Noise Cancelling Headphones (Model X)',
        'price': price,
        'rating': 4.7,
        'seller': 'TechDeals.co',
        'timestamp': pd.Timestamp.now()
    }

# --- 2. Data Collection & 3. Data Cleaning/Storage Module ---

def run_price_scout():
    """Runs the full scraping, processing, and analysis workflow."""
    print("--- Starting Price Scout Workflow ---")

    # Step 1: Collect raw data from simulated scrapers
    raw_data = [scrape_site_A(), scrape_site_B()]

    # Step 2: Convert to a Pandas DataFrame (Data Cleaning & Normalization)
    # This step handles data standardization and structure for analysis.
    df = pd.DataFrame(raw_data)

    # Step 3: Save to CSV (Data Storage)
    file_name = 'price_comparison_data.csv'
    df.to_csv(file_name, index=False)
    print(f"\n✅ Data successfully cleaned, structured, and saved to {file_name}")

    # --- 4. Data Analysis Module ---

    # Find the row with the minimum price (Competitive Analysis)
    # This is the actionable intelligence provided by the system.
    best_price_row = df.loc[df['price'].idxmin()]

    best_price = best_price_row['price']
    best_seller = best_price_row['seller']
    
    # Print the actionable insight
    print("\n-------------------------------------")
    print("🚀 Competitive Pricing Insight (Actionable Intelligence)")
    print(f"Product: {best_price_row['product']}")
    print(f"The current lowest price found is **${best_price:.2f}** from **{best_seller}**.")
    print("-------------------------------------")
    
    # Optional: Display the full data structure in the console
    # print("\n--- Full Scraped Data (DataFrame) ---")
    # print(df[['seller', 'price', 'rating']])
    

if __name__ == "__main__":
    run_price_scout()
