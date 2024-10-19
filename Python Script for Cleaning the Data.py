import pandas as pd

# Load the datasets
ecommerce_data = pd.read_csv("ecommerce_product_reviews.csv")
social_data = pd.read_csv("social_media_engagement.csv")

# Cleaning the e-commerce data
ecommerce_data.dropna(inplace=True)  # Drop missing values
ecommerce_data['Product Price'] = ecommerce_data['Product Price'].str.replace('$', '').astype(float)

# Cleaning the social media data
social_data.dropna(inplace=True)

# Save cleaned datasets
ecommerce_data.to_csv("cleaned_ecommerce_reviews.csv", index=False)
social_data.to_csv("cleaned_social_media_data.csv", index=False)

print("Data cleaning completed.")
