import unittest
from insurance.engine import InsuranceClaimsEngine, InsurancePolicy

class TestInsuranceClaims(unittest.TestCase):
    def test_claim_adjudication_math(self):
        engine = InsuranceClaimsEngine()
        policy = InsurancePolicy(
            policy_id="POL-2026-901",
            insured_member_name="Ramesh Patel",
            sum_insured=500000.0, # ₹5 Lakhs
            deductible_amount=5000.0,
            copay_percentage=10.0 # 10% co-pay
        )

        res = engine.adjudicate_claim(
            claim_id="CLM-771",
            policy=policy,
            hospital_bill_amount=105000.0
        )

        self.assertEqual(res.status, "APPROVED")
        self.assertEqual(res.deductible_applied, 5000.0)
        # Bill 105k - 5k deductible = 100k. 10% copay = 10,000.
        self.assertEqual(res.copay_amount_patient_share, 10000.0)
        # Approved = 90,000
        self.assertEqual(res.approved_settlement_payout, 90000.0)
        self.assertEqual(res.remaining_sum_insured_balance, 410000.0)

if __name__ == "__main__":
    unittest.main()
