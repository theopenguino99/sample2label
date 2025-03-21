# sample2label
Module to sample data from the fashion dataset such that samples have equal number of negative, postiive, and 0 "sentiment_score".

# ⚙️ Functions:
## 🔎 *sample_equal_sentiment(df, sample_size, sentiment_column = "sentiment_score")*
#### Function in order to sample the Fashion dataset with a sentiment column, and saves an excel file in the current directory with *sample_size* number of results, where a third of the samples have sentiment_score less than zero, a third equal to zero and another third more than zero. Use this function to generate an excel file in order for group members to manually evaluate the sentiment of each fashion post. This will be used to compare inter-coder reliability and also sentiment analysis of pysentimento and the sentiments provided by the dataset itself.
