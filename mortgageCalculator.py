def mortgageCalculator(principal, annual_rate, number_months, monthly_payment, first_payment=None):
    if first_payment is None:
        first_payment = monthly_payment
    
    monthly_rate = annual_rate / 12

    total_interest = 0.0
    total_principal = 0.0
    principal_left = principal

    # Month 1
    monthly_interest = principal_left * monthly_rate
    monthly_principal = first_payment - monthly_interest

    total_interest += monthly_interest
    total_principal += monthly_principal
    principal_left -= monthly_principal

    # Months 2..N
    for _ in range(2, number_months + 1):
        monthly_interest = principal_left * monthly_rate
        monthly_principal = monthly_payment - monthly_interest

        total_interest += monthly_interest
        total_principal += monthly_principal
        principal_left -= monthly_principal

    return total_interest, total_principal, principal_left


mortgageCalculator(
    principal=400000,
    annual_rate=0.0397,
    number_months=60,
    monthly_payment=1800
)
