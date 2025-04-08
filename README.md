![incentives](https://framerusercontent.com/images/2Z8Sb7Im4ztuVKI9IL9oLUtysU.png)

# Obol Incentives Reports

This repository contains the automated reporting system for Obol Network's incentive program runs. The reports are generated on a weekly basis to track and analyze the performance and distribution of incentives across the network. Learn more about this program at https://obol.org/incentives

## Overview

These reports provide insights into the weekly Obol incentive program runs, helping track:
- Validator performance metrics
- Incentive distribution calculations
- Participation statistics
- Network health indicators

## Report Generation

Reports are automatically generated on a weekly basis, capturing data from the previous week's validator operations and incentive distributions. Each report includes:

- Earned incentives breakdown
- Participation levels
- Historical comparisons

## Report Structure

Each weekly report is organized in the following format:
```
./
  └── week_YYYY-MM-DD/
      ├── README.md
      ├── address_mappings.csv
      ├── contributions_summary.csv
      ├── incentives_summary.csv
      └── lido_csm_contributors.csv
```

The files contain:
- `README.md`: Weekly report summary and context
- `address_mappings.csv`: Mapping of addresses to identifiers
- `contributions_summary.csv`: Summary of contributions for the week
- `incentives_summary.csv`: Detailed breakdown of incentives
- `lido_csm_contributors.csv`: Lido CSM contributor information

## Contact

For questions about the Obol incentive program or these reports, please reach out to the Obol team or visit [obol.tech](https://obol.tech).

## Disclaimer

The data presented in these reports is for informational purposes only. While we strive for accuracy in our reporting, all figures should be considered preliminary until formally verified. The incentive distributions are subject to review and may be adjusted based on additional verification processes. Obol Network reserves the right to modify the incentive program structure and distribution mechanisms at any time.
