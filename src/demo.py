"""Script to test the recommendation engine"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card_model import CreditCard
from recommendation_engine import RecommendationEngine
from data.sample_cards import get_sample_cards

def print_separator(title=""):
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print(f"\n{'-'*60}\n")

def demo():
    """Run a demo of the recommendation engine"""
    print("\n" + "="*60)
    print("   POINTSMAXIMIZER - DEMO")
    print("="*60)
    
    # Load sample cards
    cards = get_sample_cards()
    engine = RecommendationEngine(cards)
    
    print_separator("Sample Credit Cards Loaded:")
    for i, card in enumerate(cards, 1):
        print(f"{i}. {card.name} ({card.bank})")
    
    # Demo scenarios
    scenarios = [
        (100, "dining"),
        (50, "groceries"),
        (200, "travel"),
        (75, "gas"),
        (150, "shopping"),
    ]
    
    for amount, category in scenarios:
        print_separator(f"Scenario: ${amount:.2f} purchase in {category.upper()}")
        
        best_card, best_points = engine.find_best_card(amount, category)
        recommendations = engine.get_recommendations_ranked(amount, category)
        
        print(f"💡 RECOMMENDATION: Use {best_card.name}")
        print(f"   Earn: {best_points:.1f} points ({(best_points/amount*100):.1f}% ROI)\n")
        
        print("📊 Full Ranking:")
        for i, (card, points) in enumerate(recommendations, 1):
            roi = (points/amount*100)
            print(f"   {i}. {card.name:30} → {points:6.1f} pts ({roi:5.1f}% ROI)")
    
    print("\n" + "="*60)
    print("✨ Demo Complete!")
    print("="*60 + "\n")

if __name__ == "__main__":
    demo()
