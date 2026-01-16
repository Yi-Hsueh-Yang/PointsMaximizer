"""Points Recommendation Engine"""
from typing import List, Tuple, Optional
from card_model import CreditCard

class RecommendationEngine:
    """Recommends the best credit card for a purchase"""
    
    def __init__(self, cards: List[CreditCard]):
        """Initialize with a list of credit cards"""
        self.cards = [c for c in cards if c.is_active]
    
    def find_best_card(self, amount: float, category: str) -> Tuple[Optional[CreditCard], float]:
        """
        Find the best card for a specific purchase
        
        Returns:
            Tuple of (best_card, points_earned)
        """
        if not self.cards:
            return None, 0.0
        
        best_card = None
        best_points = 0.0
        
        for card in self.cards:
            points = card.get_points_for_purchase(amount, category)
            if points > best_points:
                best_points = points
                best_card = card
        
        return best_card, best_points
    
    def get_recommendations_ranked(self, amount: float, category: str) -> List[Tuple[CreditCard, float]]:
        """
        Get all cards ranked by points earned
        
        Returns:
            List of (card, points_earned) sorted by points descending
        """
        recommendations = []
        for card in self.cards:
            points = card.get_points_for_purchase(amount, category)
            recommendations.append((card, points))
        
        # Sort by points descending
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations
    
    def add_card(self, card: CreditCard):
        """Add a new card to the recommendation engine"""
        if card not in self.cards:
            self.cards.append(card)
    
    def deactivate_card(self, card_name: str):
        """Deactivate a card temporarily"""
        for card in self.cards:
            if card.name.lower() == card_name.lower():
                card.is_active = False
                self.cards = [c for c in self.cards if c.is_active]
                break

