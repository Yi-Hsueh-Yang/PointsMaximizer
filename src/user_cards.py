"""User Card Management - Store and load selected cards"""
import json
import os
from typing import List
from card_model import CreditCard
from card_database import CardDatabase

USER_CARDS_FILE = "user_cards.json"

class UserCardManager:
    """Manages user's selected credit cards"""
    
    @staticmethod
    def save_cards(selected_card_names: List[str]):
        """Save selected cards to file"""
        data = {
            "selected_cards": selected_card_names
        }
        with open(USER_CARDS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def load_cards() -> List[CreditCard]:
        """Load user's selected cards"""
        if not os.path.exists(USER_CARDS_FILE):
            return []
        
        try:
            with open(USER_CARDS_FILE, 'r') as f:
                data = json.load(f)
            
            selected_card_names = data.get("selected_cards", [])
            cards = []
            
            for card_name in selected_card_names:
                card = CardDatabase.get_card_by_name(card_name)
                if card:
                    cards.append(card)
            
            return cards
        except Exception as e:
            print(f"Error loading cards: {e}")
            return []
    
    @staticmethod
    def has_saved_cards() -> bool:
        """Check if user has saved cards"""
        return os.path.exists(USER_CARDS_FILE)
    
    @staticmethod
    def clear_cards():
        """Clear saved cards"""
        if os.path.exists(USER_CARDS_FILE):
            os.remove(USER_CARDS_FILE)
    
    @staticmethod
    def add_card(card_name: str):
        """Add a single card to selection"""
        cards = UserCardManager.load_cards()
        card_names = [c.name for c in cards]
        
        if card_name not in card_names:
            card_names.append(card_name)
            UserCardManager.save_cards(card_names)
            return True
        return False
    
    @staticmethod
    def remove_card(card_name: str):
        """Remove a card from selection"""
        cards = UserCardManager.load_cards()
        card_names = [c.name for c in cards if c.name != card_name]
        UserCardManager.save_cards(card_names)
    
    @staticmethod
    def get_selected_card_names() -> List[str]:
        """Get names of selected cards"""
        cards = UserCardManager.load_cards()
        return [c.name for c in cards]
