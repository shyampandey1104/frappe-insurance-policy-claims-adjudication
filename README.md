# Frappe Insurance Policy & Claims Adjudication Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![IRDAI](https://img.shields.io/badge/FinTech-IRDAI%20Ready-blue.svg)](https://irdai.gov.in)

Scalable insurance policy ledger and automated claim adjudication controller calculating deductibles, co-pays, and remaining balances.

## Features
- **Deductible & Co-Pay Engine:** Configurable policy tiers with automatic patient co-pay calculations.
- **Sum Insured Balance Depletion:** Tracks multi-claim lifecycle over active policy tenures.
- **Cashless Settlement Vouchers:** Formatted adjudication receipts for hospital TPA desk settlement.

## Tests
```bash
python3 -m unittest discover tests
```
