import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create images folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Load data
listings = pd.read_csv('data/listings.csv')
calendar = pd.read_csv('data/calendar.csv')
reviews = pd.read_csv('data/reviews.csv')

# -------------------------------
# 1. Price Distribution Analysis
# -------------------------------
plt.figure(figsize=(10, 6))
plt.hist(listings['price'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Listing Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('images/price_distribution.png')
plt.close()

# -------------------------------------------
# 2. Seasonal Price Trends from Calendar Data
# -------------------------------------------
# Convert date column to datetime and extract month
calendar['date'] = pd.to_datetime(calendar['date'])
calendar['month'] = calendar['date'].dt.month

# Compute average price per month for available dates
monthly_prices = calendar[calendar['available'] == True].groupby('month')['price'].mean()

plt.figure(figsize=(10, 6))
monthly_prices.plot(kind='line', marker='o', color='green')
plt.title('Average Price per Month for Available Listings')
plt.xlabel('Month')
plt.ylabel('Average Price')
plt.xticks(range(1, 13))
plt.grid(True)
plt.savefig('images/price_trend.png')
plt.close()

# ---------------------------------------
# 3. Occupancy Analysis (Availability)
# ---------------------------------------
occupancy = calendar['available'].value_counts()

plt.figure(figsize=(6, 4))
occupancy.plot(kind='bar', color=['salmon', 'lightblue'])
plt.title('Occupancy: Available vs Booked Days')
plt.xlabel('Availability (True=Available, False=Booked)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.savefig('images/occupancy_plot.png')
plt.close()

# -----------------------------------------------------------
# 4. Amenities Impact on Reviews (if amenities info exists)
# -----------------------------------------------------------
if 'amenities' in listings.columns:
    # Calculate number of amenities per listing (assuming comma-separated)
    listings['amenities_count'] = listings['amenities'].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0)

    # Histogram of amenities count
    plt.figure(figsize=(10, 6))
    plt.hist(listings['amenities_count'], bins=30, color='orange', edgecolor='black')
    plt.title('Distribution of Amenities Count per Listing')
    plt.xlabel('Number of Amenities')
    plt.ylabel('Frequency')
    plt.savefig('images/amenities_count.png')
    plt.close()

    # Scatter plot: Amenities Count vs. Review Score (if review score exists)
    if 'review_scores_rating' in listings.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(listings['amenities_count'], listings['review_scores_rating'], alpha=0.5)
        plt.title('Amenities Count vs. Review Scores')
        plt.xlabel('Number of Amenities')
        plt.ylabel('Review Score')
        plt.savefig('images/amenities_vs_reviews.png')
        plt.close()

print("Analysis complete. Visualizations saved in the 'images' folder.")
