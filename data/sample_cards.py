"""Sample Credit Cards Data"""
from src.card_model import CreditCard

def get_sample_cards():
    """Return a list of sample credit cards"""
    
    # Chase Sapphire Preferred
    card1 = CreditCard(
        name="Chase Sapphire Preferred",
        bank="Chase",
        is_active=True,
        base_points=1.0,
        category_multipliers={
            "travel": 3.0,
            "dining": 3.0,
            "groceries": 1.0,
            "gas": 1.0,
            "shopping": 1.0,
        },
        annual_fee=95.0,
        bonus_categories={}
    )
    
    # American Express Gold
    card2 = CreditCard(
        name="American Express Gold",
        bank="American Express",
        is_active=True,
        base_points=1.0,
        category_multipliers={
            "travel": 3.0,
            "dining": 4.0,
            "groceries": 4.0,
            "gas": 1.0,
            "shopping": 1.0,
        },
        annual_fee=250.0,
        bonus_categories={}
    )
    
    # Capital One Venture
    card3 = CreditCard(
        name="Capital One Venture",
        bank="Capital One",
        is_active=True,
        base_points=2.0,  # 2x on everything
        category_multipliers={
            "travel": 2.0,
            "dining": 2.0,
            "groceries": 2.0,
            "gas": 2.0,
            "shopping": 2.0,
        },
        annual_fee=95.0,
        bonus_categories={}
    )
    
    # Walmart Rewards
    card4 = CreditCard(
        name="Walmart Rewards",
        bank="Walmart",
        is_active=True,
        base_points=1.0,
        category_multipliers={
            "shopping": 3.0,
            "gas": 2.0,
            "dining": 1.0,
            "groceries": 1.0,
            "travel": 1.0,
        },
        annual_fee=0.0,
        bonus_categories={}
    )
    
    return [card1, card2, card3, card4]
