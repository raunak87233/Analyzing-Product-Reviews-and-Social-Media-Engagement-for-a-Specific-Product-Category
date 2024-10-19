# Load cleaned datasets
ecommerce_data = pd.read_csv("cleaned_ecommerce_reviews.csv")
social_data = pd.read_csv("cleaned_social_media_data.csv")

# Correlation between price and rating
price_rating_corr = ecommerce_data['Product Price'].corr(ecommerce_data['Average Rating'])
print(f"Correlation between Product Price and Rating: {price_rating_corr}")

# Analyzing social media engagement by hashtags
social_data['Total Engagement'] = social_data['Likes'] + social_data['Retweets']
top_hashtags = social_data.groupby('Hashtags')['Total Engagement'].sum().sort_values(ascending=False)
print("Top Hashtags by Engagement:\n", top_hashtags.head())

# Save results
top_hashtags.to_csv("top_hashtags.csv", index=False)
