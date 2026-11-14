"""Health and General Insurance Policy & Claims Adjudication Controller."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class InsurancePolicy:
    policy_id: str
    insured_member_name: str
    sum_insured: float
    deductible_amount: float
    copay_percentage: float  # e.g., 10.0 for 10%
    is_active: bool = True
    cumulative_claims_paid_this_year: float = 0.0


@dataclass
class ClaimAssessmentResult:
    claim_id: str
    policy_id: str
    claimed_hospital_amount: float
    deductible_applied: float
    copay_amount_patient_share: float
    approved_settlement_payout: float
    remaining_sum_insured_balance: float
    status: str  # APPROVED, REJECTED_LIMIT_EXCEEDED, REJECTED_POLICY_INACTIVE


class InsuranceClaimsEngine:
    """Evaluates cashless hospital insurance claims against policy deductibles, co-pays, and balance sums."""

    def adjudicate_claim(
        self,
        claim_id: str,
        policy: InsurancePolicy,
        hospital_bill_amount: float
    ) -> ClaimAssessmentResult:
        if not policy.is_active:
            return ClaimAssessmentResult(
                claim_id=claim_id,
                policy_id=policy.policy_id,
                claimed_hospital_amount=hospital_bill_amount,
                deductible_applied=0.0,
                copay_amount_patient_share=0.0,
                approved_settlement_payout=0.0,
                remaining_sum_insured_balance=0.0,
                status="REJECTED_POLICY_INACTIVE"
            )

        available_limit = max(0.0, policy.sum_insured - policy.cumulative_claims_paid_this_year)
        if available_limit <= 0:
            return ClaimAssessmentResult(
                claim_id=claim_id,
                policy_id=policy.policy_id,
                claimed_hospital_amount=hospital_bill_amount,
                deductible_applied=0.0,
                copay_amount_patient_share=0.0,
                approved_settlement_payout=0.0,
                remaining_sum_insured_balance=0.0,
                status="REJECTED_LIMIT_EXCEEDED"
            )

        # 1. Apply deductible
        after_deductible = max(0.0, hospital_bill_amount - policy.deductible_amount)
        # 2. Apply co-pay
        copay = round((after_deductible * policy.copay_percentage) / 100.0, 2)
        insurable_after_copay = round(after_deductible - copay, 2)

        approved_payout = min(insurable_after_copay, available_limit)
        policy.cumulative_claims_paid_this_year += approved_payout
        new_balance = round(policy.sum_insured - policy.cumulative_claims_paid_this_year, 2)

        return ClaimAssessmentResult(
            claim_id=claim_id,
            policy_id=policy.policy_id,
            claimed_hospital_amount=hospital_bill_amount,
            deductible_applied=policy.deductible_amount,
            copay_amount_patient_share=copay,
            approved_settlement_payout=approved_payout,
            remaining_sum_insured_balance=new_balance,
            status="APPROVED"
        )
