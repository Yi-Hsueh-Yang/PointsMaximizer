"""Comprehensive Credit Card Database"""
from src.card_model import CreditCard

class CardDatabase:
    """Database of real credit cards organized by bank"""
    
    # CHASE CARDS
    CHASE_CARDS = {
        "Chase Sapphire Preferred": CreditCard(
            name="Chase Sapphire Preferred",
            bank="Chase",
            points_name="UR",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 1.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=95.0,
        ),
        "Chase Sapphire Reserve": CreditCard(
            name="Chase Sapphire Reserve",
            bank="Chase",
            points_name="UR",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 1.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=550.0,
        ),
        "Chase Freedom Flex": CreditCard(
            name="Chase Freedom Flex",
            bank="Chase",
            points_name="UR",
            base_points=1.0,
            category_multipliers={
                "travel": 1.0,
                "dining": 1.0,
                "groceries": 5.0,
                "gas": 1.5,
                "shopping": 5.0,
            },
            annual_fee=0.0,
        ),
        "Chase Freedom Unlimited": CreditCard(
            name="Chase Freedom Unlimited",
            bank="Chase",
            points_name="UR",
            base_points=1.5,
            category_multipliers={
                "travel": 1.5,
                "dining": 1.5,
                "groceries": 1.5,
                "gas": 1.5,
                "shopping": 1.5,
            },
            annual_fee=0.0,
        ),
        "Chase Business Preferred": CreditCard(
            name="Chase Business Preferred",
            bank="Chase",
            points_name="UR",
            base_points=1.0,
            category_multipliers={
                "travel": 2.0,
                "dining": 2.0,
                "groceries": 3.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=95.0,
        ),
    }
    
    # AMERICAN EXPRESS CARDS
    AMEX_CARDS = {
        "American Express Gold": CreditCard(
            name="American Express Gold",
            bank="American Express",
            points_name="MR",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 4.0,
                "groceries": 4.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=250.0,
        ),
        "American Express Platinum": CreditCard(
            name="American Express Platinum",
            bank="American Express",
            points_name="MR",
            base_points=1.0,
            category_multipliers={
                "travel": 5.0,
                "dining": 1.0,
                "groceries": 1.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=695.0,
        ),
        "American Express Blue Preferred": CreditCard(
            name="American Express Blue Preferred",
            bank="American Express",
            points_name="MR",
            base_points=1.0,
            category_multipliers={
                "travel": 1.0,
                "dining": 1.0,
                "groceries": 6.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=95.0,
        ),
        "American Express Green": CreditCard(
            name="American Express Green",
            bank="American Express",
            points_name="MR",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 1.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=150.0,
        ),
    }
    
    # CAPITAL ONE CARDS
    CAPITAL_ONE_CARDS = {
        "Capital One Venture X": CreditCard(
            name="Capital One Venture X",
            bank="Capital One",
            points_name="Miles",
            base_points=2.0,
            category_multipliers={
                "travel": 10.0,
                "dining": 2.0,
                "groceries": 2.0,
                "gas": 2.0,
                "shopping": 2.0,
            },
            annual_fee=395.0,
        ),
        "Capital One Venture": CreditCard(
            name="Capital One Venture",
            bank="Capital One",
            points_name="Miles",
            base_points=2.0,
            category_multipliers={
                "travel": 2.0,
                "dining": 2.0,
                "groceries": 2.0,
                "gas": 2.0,
                "shopping": 2.0,
            },
            annual_fee=95.0,
        ),
        "Capital One Quicksilver": CreditCard(
            name="Capital One Quicksilver",
            bank="Capital One",
            points_name="Cashback",
            base_points=1.5,
            category_multipliers={
                "travel": 1.5,
                "dining": 1.5,
                "groceries": 1.5,
                "gas": 1.5,
                "shopping": 1.5,
            },
            annual_fee=0.0,
        ),
    }
    
    # CITI CARDS
    CITI_CARDS = {
        "Citi Prestige": CreditCard(
            name="Citi Prestige",
            bank="Citi",
            points_name="ThankYou",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 1.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=495.0,
        ),
        "Citi Premier": CreditCard(
            name="Citi Premier",
            bank="Citi",
            points_name="ThankYou",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 2.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=95.0,
        ),
        "Citi Double Cash": CreditCard(
            name="Citi Double Cash",
            bank="Citi",
            points_name="ThankYou",
            base_points=2.0,
            category_multipliers={
                "travel": 2.0,
                "dining": 2.0,
                "groceries": 2.0,
                "gas": 2.0,
                "shopping": 2.0,
            },
            annual_fee=0.0,
        ),
    }
    
    # DISCOVER CARDS
    DISCOVER_CARDS = {
        "Discover it Chrome": CreditCard(
            name="Discover it Chrome",
            bank="Discover",
            points_name="Cashback",
            base_points=1.0,
            category_multipliers={
                "travel": 2.0,
                "dining": 1.0,
                "groceries": 1.0,
                "gas": 2.0,
                "shopping": 1.0,
            },
            annual_fee=0.0,
        ),
        "Discover it Cashback": CreditCard(
            name="Discover it Cashback",
            bank="Discover",
            points_name="Cashback",
            base_points=1.0,
            category_multipliers={
                "travel": 1.0,
                "dining": 5.0,
                "groceries": 5.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=0.0,
        ),
    }
    
    # WALMART CARDS
    WALMART_CARDS = {
        "Walmart Rewards Card": CreditCard(
            name="Walmart Rewards Card",
            bank="Walmart",
            points_name="Points",
            base_points=1.0,
            category_multipliers={
                "shopping": 3.0,
                "gas": 2.0,
                "dining": 1.0,
                "groceries": 1.0,
                "travel": 1.0,
            },
            annual_fee=0.0,
        ),
    }
    
    # COSTCO CARDS
    COSTCO_CARDS = {
        "Costco Anywhere Visa": CreditCard(
            name="Costco Anywhere Visa",
            bank="Costco",
            points_name="Cashback",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 2.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=120.0,
        ),
    }
    
    # BANK OF AMERICA CARDS
    BOA_CARDS = {
        "Bank of America Premium Rewards": CreditCard(
            name="Bank of America Premium Rewards",
            bank="Bank of America",
            points_name="Points",
            base_points=1.5,
            category_multipliers={
                "travel": 1.5,
                "dining": 1.5,
                "groceries": 1.5,
                "gas": 1.5,
                "shopping": 1.5,
            },
            annual_fee=95.0,
        ),
        "Bank of America Cash Rewards": CreditCard(
            name="Bank of America Cash Rewards",
            bank="Bank of America",
            points_name="Cashback",
            base_points=1.0,
            category_multipliers={
                "travel": 1.0,
                "dining": 3.0,
                "groceries": 2.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=0.0,
        ),
    }
    
    # WELLS FARGO CARDS
    WELLS_FARGO_CARDS = {
        "Wells Fargo Rewards Preferred": CreditCard(
            name="Wells Fargo Rewards Preferred",
            bank="Wells Fargo",
            points_name="Points",
            base_points=1.0,
            category_multipliers={
                "travel": 3.0,
                "dining": 3.0,
                "groceries": 1.0,
                "gas": 1.0,
                "shopping": 1.0,
            },
            annual_fee=95.0,
        ),
        "Wells Fargo Active Cash": CreditCard(
            name="Wells Fargo Active Cash",
            bank="Wells Fargo",
            points_name="Cashback",
            base_points=2.0,
            category_multipliers={
                "travel": 2.0,
                "dining": 2.0,
                "groceries": 2.0,
                "gas": 2.0,
                "shopping": 2.0,
            },
            annual_fee=0.0,
        ),
    }
    
    # ALL BANKS
    ALL_BANKS = {
        "Chase": CHASE_CARDS,
        "American Express": AMEX_CARDS,
        "Capital One": CAPITAL_ONE_CARDS,
        "Citi": CITI_CARDS,
        "Discover": DISCOVER_CARDS,
        "Walmart": WALMART_CARDS,
        "Costco": COSTCO_CARDS,
        "Bank of America": BOA_CARDS,
        "Wells Fargo": WELLS_FARGO_CARDS,
    }
    
    @classmethod
    def get_all_banks(cls):
        """Get list of all banks"""
        return sorted(cls.ALL_BANKS.keys())
    
    @classmethod
    def get_cards_by_bank(cls, bank_name):
        """Get all cards for a specific bank"""
        if bank_name in cls.ALL_BANKS:
            return cls.ALL_BANKS[bank_name]
        return {}
    
    @classmethod
    def get_card_by_name(cls, card_name):
        """Get a specific card by name"""
        for bank_cards in cls.ALL_BANKS.values():
            if card_name in bank_cards:
                return bank_cards[card_name]
        return None
    
    @classmethod
    def get_all_cards(cls):
        """Get all cards as a flat dictionary"""
        all_cards = {}
        for bank_cards in cls.ALL_BANKS.values():
            all_cards.update(bank_cards)
        return all_cards
