"""Main CLI Application for PointsMaximizer"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card_model import CreditCard
from recommendation_engine import RecommendationEngine
from data.sample_cards import get_sample_cards

def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print("        CREDIT CARD POINTS MAXIMIZER")
    print("="*60 + "\n")

def print_menu():
    """Print main menu"""
    print("\nOptions:")
    print("1. Get recommendation for a purchase")
    print("2. View all your cards")
    print("3. View all categories")
    print("4. Exit")
    print()

def format_currency(amount):
    """Format amount as currency"""
    return f"${amount:.2f}"

def format_points(points):
    """Format points"""
    return f"{points:.1f} pts"

def main():
    """Main application loop"""
    print_header()
    print("Welcome! Let's maximize your credit card points!\n")
    
    # Initialize with sample cards
    cards = get_sample_cards()
    engine = RecommendationEngine(cards)
    
    # Define available categories
    categories = ["travel", "dining", "groceries", "gas", "shopping", "other"]
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Get recommendation
            try:
                amount = float(input("\nEnter purchase amount: $"))
                if amount < 0:
                    print("❌ Amount must be positive!")
                    continue
                
                print("\nAvailable categories:")
                for i, cat in enumerate(categories, 1):
                    print(f"  {i}. {cat.capitalize()}")
                
                cat_choice = input("Enter category number: ").strip()
                try:
                    cat_idx = int(cat_choice) - 1
                    if 0 <= cat_idx < len(categories):
                        category = categories[cat_idx]
                    else:
                        print("❌ Invalid category!")
                        continue
                except ValueError:
                    print("❌ Please enter a valid number!")
                    continue
                
                # Get best card and ranked recommendations
                best_card, best_points = engine.find_best_card(amount, category)
                all_recs = engine.get_recommendations_ranked(amount, category)
                
                print("\n" + "="*60)
                print(f"💳 BEST CARD FOR ${amount:.2f} {category.upper()} PURCHASE")
                print("="*60)
                
                if best_card:
                    print(f"\n✅ USE: {best_card.name}")
                    print(f"   Bank: {best_card.bank}")
                    print(f"   Points earned: {format_points(best_points)}")
                    print(f"   ROI: {(best_points/amount*100):.1f}%")
                else:
                    print("❌ No active cards available!")
                    continue
                
                # Show all rankings
                print(f"\n📊 ALL CARDS RANKED:")
                for i, (card, points) in enumerate(all_recs, 1):
                    roi = (points/amount*100)
                    print(f"   {i}. {card.name}: {format_points(points)} ({roi:.1f}%)")
                
                print()
                
            except ValueError:
                print("❌ Please enter a valid amount!")
        
        elif choice == "2":
            # View all cards
            print("\n" + "="*60)
            print("💳 YOUR CREDIT CARDS")
            print("="*60 + "\n")
            
            for card in cards:
                status = "✅ Active" if card.is_active else "❌ Inactive"
                print(f"Card: {card.name}")
                print(f"Bank: {card.bank} - {status}")
                print(f"Annual Fee: {format_currency(card.annual_fee)}")
                print(f"Base Points: {card.base_points}x")
                print(f"Category Bonuses:")
                for cat, mult in card.category_multipliers.items():
                    print(f"  • {cat.capitalize()}: {mult}x")
                print()
        
        elif choice == "3":
            # View categories
            print("\n" + "="*60)
            print("📂 AVAILABLE CATEGORIES")
            print("="*60)
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat.capitalize()}")
            print()
        
        elif choice == "4":
            print("\n👋 Thank you for using PointsMaximizer!")
            print("Happy points earning!\n")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
