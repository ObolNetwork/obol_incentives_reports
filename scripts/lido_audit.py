import pandas as pd

week_folder = "../week_2025-05-05"

lido_address = "0x388c818ca8b9251b393131c08a736a67ccb19297"
contribution_to_obol = 172039790539366.46875

contributions_summary_df = pd.read_csv(f"{week_folder}/contributions_summary.csv")

# Filter contributions_summary_df for the Lido address
lido_contributions = contributions_summary_df[contributions_summary_df['address'] == lido_address]

# Calculate the sum of the 'amount' column
total_lido_incentives = lido_contributions['total_contribution'] * contribution_to_obol

print(f"Total Lido Incentives: {total_lido_incentives/(10**18)}")

