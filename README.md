# 💳 Credit Card Points Maximizer

A smart recommendation system that helps credit card users maximize their points return by suggesting the best card to use for each purchase.

## 🎯 Project Overview

**Problem:** Credit card enthusiasts often have multiple cards with different benefits and multipliers, making it hard to remember which card to use for each purchase to maximize points.

**Solution:** PointsMaximizer provides instant recommendations on which credit card to use based on:
- Purchase amount
- Purchase category (dining, travel, groceries, etc.)
- Card multipliers and bonuses
- Current active cards

## 📁 Project Structure

```
PointsMaximizer-1/
├── src/
│   ├── __init__.py              # Python package marker
│   ├── card_model.py            # Credit card data model
│   ├── recommendation_engine.py # Core recommendation logic
│   ├── main.py                  # Interactive CLI app
│   └── demo.py                  # Demo script
├── data/
│   ├── __init__.py              # Python package marker
│   └── sample_cards.py          # Sample credit card data
└── README.md                    # This file
```

## 🚀 Quick Start

### Option 1: Run the Interactive CLI Application

```bash
python src/main.py
```

This launches an interactive menu where you can:
1. Get recommendations for specific purchases
2. View all your credit cards
3. Browse available categories
4. Exit

### Option 2: Run the Demo

```bash
python src/demo.py
```

This runs automated scenarios showing how the engine recommends cards for different purchase types.

## 📚 How to Use

### Step 1: Add Your Credit Cards

Edit `data/sample_cards.py` to add your actual credit cards. Here's the format:

```python
card = CreditCard(
    name="Your Card Name",
    bank="Bank Name",
    is_active=True,
    base_points=1.0,                    # Points per $1 spent
    category_multipliers={
        "travel": 3.0,                  # 3x points on travel
        "dining": 2.0,                  # 2x points on dining
        "groceries": 1.5,               # 1.5x points on groceries
        "gas": 1.0,
        "shopping": 1.0,
    },
    annual_fee=95.0,                    # Annual fee amount
    bonus_categories={}                 # Future: special bonuses
)
```

### Step 2: Launch the Application

Run the interactive CLI:
```bash
python src/main.py
```

### Step 3: Get Recommendations

When prompted:
1. Enter your purchase amount (e.g., `50`)
2. Select the category (e.g., `2` for dining)
3. See instant recommendations with:
   - ✅ **Best card** for that purchase
   - 📊 **Ranking** of all cards by points earned
   - 💰 **ROI percentage** for each card

## 🔧 Core Components

### `card_model.py`
Defines the `CreditCard` class with:
- Card metadata (name, bank, annual fee)
- Category multipliers
- Methods to calculate points for any purchase

### `recommendation_engine.py`
The brain of the system with methods:
- `find_best_card()` - Returns the optimal card for a purchase
- `get_recommendations_ranked()` - Ranks all cards by points
- `add_card()` - Add new cards dynamically
- `deactivate_card()` - Temporarily disable cards

### `main.py`
Interactive CLI application with:
- Menu-driven interface
- Purchase input (amount + category)
- Real-time recommendations
- Card browsing

### `demo.py`
Automated demo showing:
- 5 different scenarios
- How cards rank for each scenario
- Side-by-side comparison

## 💡 Example Scenarios

**Scenario 1: $100 Dining Purchase**
- Chase Sapphire Preferred: 300 points
- Amex Gold: 400 points ✅ **BEST**
- Capital One Venture: 200 points
- Walmart: 100 points

**Scenario 2: $50 Grocery Purchase**
- Chase Sapphire: 50 points
- Amex Gold: 200 points ✅ **BEST**
- Capital One: 100 points
- Walmart: 50 points

**Scenario 3: $200 Travel Purchase**
- Chase Sapphire: 600 points ✅ **BEST**
- Amex Gold: 600 points ✅ **BEST**
- Capital One: 400 points
- Walmart: 200 points

## 🛠️ Customization Guide

### Adding a New Credit Card

1. Open `data/sample_cards.py`
2. Create a new card variable:
   ```python
   my_new_card = CreditCard(
       name="My Card",
       bank="My Bank",
       base_points=1.5,
       category_multipliers={
           "dining": 3.0,
           # ... other categories
       },
       annual_fee=0.0,
   )
   ```
3. Add it to the return statement:
   ```python
   return [card1, card2, card3, card4, my_new_card]
   ```

### Adding a New Category

1. Open `src/main.py`
2. Find the `categories` list (around line 50)
3. Add your new category:
   ```python
   categories = ["travel", "dining", "groceries", "gas", "shopping", "utilities", "other"]
   ```
4. Update all cards in `data/sample_cards.py` to include multipliers for the new category

### Modifying Multipliers

Simply edit the `category_multipliers` dictionary in `data/sample_cards.py` for any card to match your actual card benefits.

## 📊 Understanding the Output

When you get a recommendation, you'll see:

```
============================================================
💳 BEST CARD FOR $100.00 DINING PURCHASE
============================================================

✅ USE: American Express Gold
   Bank: American Express
   Points earned: 400.0 pts
   ROI: 4.0%

📊 ALL CARDS RANKED:
   1. American Express Gold: 400.0 pts (4.0%)
   2. Chase Sapphire Preferred: 300.0 pts (3.0%)
   3. Capital One Venture: 200.0 pts (2.0%)
   4. Walmart Rewards: 100.0 pts (1.0%)
```

- **Points earned**: Total points you'll get with this card
- **ROI**: Return on investment as a percentage (higher is better)

## 🎨 Features

✅ Multiple credit card management
✅ Category-based recommendations
✅ Real-time points calculation
✅ Card ranking system
✅ Interactive CLI interface
✅ Customizable card data
✅ Annual fee tracking
✅ ROI calculations

## 🚀 Future Enhancements

- [ ] Web UI dashboard
- [ ] Annual spending analysis
- [ ] Points-per-dollar tracking
- [ ] Card comparison tool
- [ ] Bonus rewards tracking
- [ ] API integration for real card data
- [ ] Historical spending patterns
- [ ] Budget management
- [ ] Points redemption tracking
- [ ] Multi-user support

## 📝 Notes

- This is a prototype. Real-world usage may require integration with actual card data APIs.
- Annual fees are tracked but not yet subtracted from points calculations (future enhancement).
- All multipliers are based on example cards; update with your actual card benefits.

## 🤝 Next Steps

1. **Customize Your Cards**: Edit `data/sample_cards.py` with your actual cards
2. **Run the Demo**: Execute `python src/demo.py` to see it in action
3. **Try the App**: Run `python src/main.py` and test scenarios
4. **Expand**: Add more cards, categories, and features as needed

---

Made with ❤️ for credit card enthusiasts who love maximizing their rewards!
