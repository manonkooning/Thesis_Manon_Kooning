import pandas as pd

df = pd.read_csv('classified_output_topics_entertainment.csv')

# Check if the 'topic' column exists
if 'topic' not in df.columns:
    raise ValueError("The CSV file does not contain a 'topic' column.")

# Calculate the distribution
counts = df['topic'].value_counts()
percentages = df['topic'].value_counts(normalize=True) * 100
distribution = pd.DataFrame({
    'Count': counts,
    'Percentage': percentages.round(2)
})
print(distribution)
