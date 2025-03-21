import pandas as pd
import numpy as np
def sample_equal_sentiment(df, sample_size, sentiment_column = "sentiment_score"):

    if sample_size > 63:
        raise ValueError("The dataset only has 21 rows with negative sentiment_score, so sample less than 63 please!")
    if sample_size % 3 != 0:
        raise ValueError("sample_size must be a multiple of 3!")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input 'df' must be a pandas DataFrame.")
        
    # Divide the DataFrame into three groups based on sentiment score
    positive_df = df[df[sentiment_column] > 0]
    zero_df = df[df[sentiment_column] == 0]
    negative_df = df[df[sentiment_column] < 0]

    # Calculate the number of samples to select from each group
    group_size = sample_size // 3

    # Randomly sample from each group
    positive_sample = positive_df.sample(n=group_size, random_state=42)  # For reproducibility
    zero_sample = zero_df.sample(n=group_size, random_state=42)
    negative_sample = negative_df.sample(n=group_size, random_state=42)

    # Combine the samples into a single DataFrame
    stratified_sample = pd.concat([positive_sample, zero_sample, negative_sample])

    # Shuffle the combined sample to mix the order
    stratified_sample = stratified_sample.sample(frac=1, random_state=42).reset_index(drop=True)
    print('Just before the error')

    # # Create a new DataFrame with the required columns according to the format defined by prof Miguel
    # new_df = pd.DataFrame({
    #     '': range(1, sample_size+1),  # First column: indices starting from 1
    #     'sentence': stratified_sample['post_text'].reset_index(drop=True),  # Second column: post_text
    #     'label': np.nan  # Third column: empty entries
    # })

    # Save to Excel
    # new_df.to_excel('output.xlsx', index=False, engine='openpyxl')
    stratified_sample.to_excel('output.xlsx', index=False, engine='openpyxl')
