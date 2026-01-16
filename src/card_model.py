"""Credit Card Data Model"""
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class CreditCard:
    """Represents a credit card with its benefits"""
    name: str
    bank: str
    points_name: str = "Points"  # e.g., "UR", "MR", "Miles", "Points"
    is_active: bool = True
    base_points: float = 1.0  # Points per dollar spent
    
    # Category multipliers (category_name -> multiplier)
    category_multipliers: Dict[str, float] = field(default_factory=dict)
    
    # Annual fee
    annual_fee: float = 0.0
    
    # Special bonuses
    bonus_categories: Dict[str, float] = field(default_factory=dict)
    
    def get_points_for_purchase(self, amount: float, category: str) -> float:
        """Calculate points earned for a purchase in a specific category"""
        if not self.is_active:
            return 0.0
        
        # Get category multiplier, default to base points
        multiplier = self.category_multipliers.get(category, self.base_points)
        
        # Add any category bonus
        bonus = self.bonus_categories.get(category, 0.0)
        
        total_multiplier = multiplier + bonus
        return amount * total_multiplier
    
    def __str__(self):
        return f"{self.name} ({self.bank})"
