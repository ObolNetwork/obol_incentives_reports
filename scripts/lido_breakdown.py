import pandas as pd

# Define the base path for the weekly report
week_folder = "../week_2025-05-05"

# Read local CSV files
address_mappings_df = pd.read_csv(f"{week_folder}/address_mappings.csv")
contributions_summary_df = pd.read_csv(f"{week_folder}/contributions_summary.csv")
incentives_summary_df = pd.read_csv(f"{week_folder}/incentives_summary.csv")
lido_csm_contributors_df = pd.read_csv(f"{week_folder}/lido_csm_contributors.csv")

# Read the remote CSV file from the URL
lido_distribution_url = "https://raw.githubusercontent.com/lidofinance/dvv-incentivisation/refs/heads/main/Obol/obol_distribution_by_lp_holders_28-04-2025_05-05-2025.csv"
lido_distribution_df = pd.read_csv(lido_distribution_url)

print("DataFrames loaded successfully:")
print("Address Mappings:", address_mappings_df.shape)
print("Contributions Summary:", contributions_summary_df.shape)
print("Incentives Summary:", incentives_summary_df.shape)
print("Lido CSM Contributors:", lido_csm_contributors_df.shape)

# Sum the total amount of Obol distributed to the Lido CSM

# Get the list of Lido CSM contributor addresses
lido_csm_addresses = lido_csm_contributors_df['address'].unique()

# Filter the incentives_summary_df for these addresses
filtered_incentives_df = incentives_summary_df[incentives_summary_df['address'].isin(lido_csm_addresses)]

# Calculate the sum of the 'amount' column and divide by 10^18
total_amount_to_lido_csm = 0.0  # Initialize
if not filtered_incentives_df.empty:
    total_amount_to_lido_csm = filtered_incentives_df['amount'].astype(float).sum() / (10**18)
    print(f"\nTotal Obol distributed to Lido CSM contributors: {total_amount_to_lido_csm}")
else:
    print("\nNo incentives found for Lido CSM contributors in the summary.")

# Separate Lido distribution addresses by tag and calculate incentive sums

# Get addresses for 'dvv' tag
dvv_addresses = lido_distribution_df[lido_distribution_df['tag'] == 'dvv']['address'].unique()

# Get addresses for 'sdvt' tag
sdvt_addresses = lido_distribution_df[lido_distribution_df['tag'] == 'sdvt']['address'].unique()

# --- Calculate sum for DVV addresses ---
filtered_incentives_dvv = incentives_summary_df[incentives_summary_df['address'].isin(dvv_addresses)]

total_amount_dvv = 0.0  # Initialize
if not filtered_incentives_dvv.empty:
    total_amount_dvv = filtered_incentives_dvv['amount'].astype(float).sum() / (10**18)
    print(f"\nTotal Obol distributed to 'dvv' tagged addresses: {total_amount_dvv}")
else:
    print("\nNo incentives found for 'dvv' tagged addresses in the summary.")

# --- Calculate sum for SDVT addresses ---
filtered_incentives_sdvt = incentives_summary_df[incentives_summary_df['address'].isin(sdvt_addresses)]

total_amount_sdvt = 0.0  # Initialize
if not filtered_incentives_sdvt.empty:
    total_amount_sdvt = filtered_incentives_sdvt['amount'].astype(float).sum() / (10**18)
    print(f"\nTotal Obol distributed to 'sdvt' tagged addresses: {total_amount_sdvt}")
else:
    print("\nNo incentives found for 'sdvt' tagged addresses in the summary.")

# --- Calculate and print the grand total ---
grand_total = total_amount_to_lido_csm + total_amount_dvv + total_amount_sdvt
print(f"\nGRAND TOTAL of Obol distributed to Lido CSM, DVV, and SDVT: {grand_total}")

# --- Calculate and print percentages of the grand total ---
if grand_total > 0:
    csm_percentage = (total_amount_to_lido_csm / grand_total) * 100
    dvv_percentage = (total_amount_dvv / grand_total) * 100
    sdvt_percentage = (total_amount_sdvt / grand_total) * 100
    print(f"  Lido CSM percentage: {csm_percentage:.2f}%")
    print(f"  DVV tagged percentage: {dvv_percentage:.2f}%")
    print(f"  SDVT tagged percentage: {sdvt_percentage:.2f}%")
else:
    print("  Percentages cannot be calculated as the grand total is zero.")
