def calculate_target(
    expenses,
    deductibles
):

    return (expenses * 6) + deductibles


def calculate_net_worth(
    private_reserve,
    investment_balance,
    trust_value
):

    return (
        private_reserve
        + investment_balance
        + trust_value
    )