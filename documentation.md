# Airbnb Data Analysis Project Documentation

## Overview
This project examines Airbnb listings in Seattle to uncover factors that influence pricing, occupancy, and guest satisfaction. The analysis includes:

- **Price Distribution:** Understanding the range and frequency of listing prices.
- **Seasonal Trends:** Evaluating how prices vary by month.
- **Occupancy Analysis:** Comparing available versus booked days.
- **Amenities Impact:** Analyzing the relationship between provided amenities and guest review scores.

## Data Sources
- **Listings Data:** Contains detailed property descriptions, prices, and guest ratings.
- **Calendar Data:** Includes daily pricing and availability.
- **Reviews Data:** Features guest reviews and ratings.

## Methodology

### Data Preparation
- CSV files were loaded into pandas DataFrames.
- Date columns in the calendar data were converted to datetime objects.
- New features (like the month of the booking date) were derived for seasonal analysis.
- For listings with an `amenities` column, the number of amenities per listing was computed.

### Exploratory Data Analysis (EDA)
1. **Price Distribution**  
   A histogram was created to show the frequency distribution of listing prices.

2. **Seasonal Price Trends**  
   The average price per month was computed and plotted. This helped identify peak (summer) and off-peak (winter) periods.

3. **Occupancy Analysis**  
   The availability of listings (available vs. booked days) was analyzed to understand occupancy rates.

4. **Amenities Impact on Reviews**  
   The number of amenities per listing was calculated and correlated with review scores using scatter plots.

### Visualizations
The following visualizations are generated and stored in the `images/` folder:
- `price_distribution.png`
- `price_trend.png`
- `occupancy_plot.png`
- `amenities_count.png` (if applicable)
- `amenities_vs_reviews.png` (if applicable)

### Tools & Libraries
- **Python 3.x:** Primary programming language
- **pandas:** Data manipulation and analysis
- **numpy:** Numerical operations
- **matplotlib:** Data visualization

## How to Run
1. **Data Setup**  
   Place your `listings.csv`, `calendar.csv`, and `reviews.csv` files into the `data/` folder.

2. **Install Dependencies**  
   ```bash
   pip install pandas numpy matplotlib

Execute Analysis Script
python analysis.py

This will generate visualizations and save them in the images/ folder.

Conclusion
The analysis provides actionable insights for both Airbnb hosts and travelers. For hosts, understanding price drivers and occupancy trends can help optimize listing strategies. For travelers, seasonal trends and amenity impacts offer tips for securing cost-effective stays.

Prepared by: Hemanth Kumar Kurapati (khemanthkumar1309@gmail.com)