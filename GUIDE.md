# 🚀 PointsMaximizer - Getting Started Guide

Welcome to the PointsMaximizer project! This guide will walk you through setup, customization, and usage. **No coding required—just copy & paste!**

---

## 📋 Table of Contents
1. [Quick Start (30 seconds)](#quick-start)
2. [Running the Demo](#running-the-demo)
3. [Running Interactive Mode](#running-interactive-mode)
4. [Adding Your Credit Cards](#adding-your-credit-cards)
5. [Customization](#customization)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start

### From Terminal (macOS/Linux):

```bash
cd "/Users/ynorice/Desktop/Desktop - Alex的MacBook Pro/Side_projects/PointsMaximizer-1/src"
python3 demo.py
```

That's it! You'll see a live demo with sample credit cards.

---

## Running the Demo

The demo shows how the recommendation engine works with 5 different purchase scenarios.

### Command:
```bash
cd "/Users/ynorice/Desktop/Desktop - Alex的MacBook Pro/Side_projects/PointsMaximizer-1/src"
python3 demo.py
```

### What you'll see:
- 📌 4 sample credit cards loaded
- 🎯 5 different purchase scenarios (dining, groceries, travel, gas, shopping)
- 📊 Rankings showing which card to use for each purchase
- 💰 Points earned and ROI percentage

---

## Running Interactive Mode

This is where you interact with the app in real-time!

### Command:
```bash
cd "/Users/ynorice/Desktop/Desktop - Alex的MacBook Pro/Side_projects/PointsMaximizer-1/src"
python3 main.py
```

### Menu Options:
1. **Get recommendation for a purchase**
   - Enter purchase amount (e.g., `100`)
   - Select category (e.g., `2` for dining)
   - See instant recommendation

2. **View all your cards**
   - Shows all active credit cards
   - Card benefits and multipliers
   - Annual fees

3. **View all categories**
   - Lists all available purchase categories

4. **Exit**
   - Quit the application

---

## Adding Your Credit Cards

This is the key customization step. You'll replace the sample cards with your actual cards.

### Step 1: Open the file
```
data/sample_cards.py
```

### Step 2: Find the credit card definitions

You'll see code like this:

```python
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
)
```

### Step 3: Replace with YOUR cards

**Template to copy & paste:**

```python
card1 = CreditCard(
    name="YOUR CARD NAME",
    bank="YOUR BANK NAME",
    is_active=True,
    base_points=1.0,  # Points per $1 (change this!)
    category_multipliers={
        "travel": 1.0,      # Change to actual multiplier
        "dining": 1.0,      # Change to actual multiplier
        "groceries": 1.0,   # Change to actual multiplier
        "gas": 1.0,         # Change to actual multiplier
        "shopping": 1.0,    # Change to actual multiplier
    },
    annual_fee=0.0,  # Your annual fee
)
```

### Example: Adding your own card

**Your card: American Express Blue**
- 3x points on dining
- 1.5x points on travel
- 1x points on groceries
- 1x points on gas
- 1x points on shopping
- $95 annual fee

**Code to use:**

```python
card1 = CreditCard(
    name="American Express Blue",
    bank="American Express",
    is_active=True,
    base_points=1.0,
    category_multipliers={
        "travel": 1.5,
        "dining": 3.0,
        "groceries": 1.0,
        "gas": 1.0,
        "shopping": 1.0,
    },
    annual_fee=95.0,
)
```

### Step 4: Update the return statement

At the bottom of `data/sample_cards.py`, make sure your cards are in the return list:

```python
def get_sample_cards():
    # ... your card definitions above ...
    
    return [card1, card2, card3, card4]  # List all your cards here
```

---

## Customization

### Adding a New Purchase Category

Want to add a category like "utilities" or "entertainment"?

#### Step 1: Edit `src/main.py`

Find this line (around line 47):
```python
categories = ["travel", "dining", "groceries", "gas", "shopping", "other"]
```

Add your new category:
```python
categories = ["travel", "dining", "groceries", "gas", "shopping", "utilities", "entertainment", "other"]
```

#### Step 2: Update all cards in `data/sample_cards.py`

For each card's `category_multipliers`, add the new category:

```python
category_multipliers={
    "travel": 3.0,
    "dining": 3.0,
    "groceries": 1.0,
    "gas": 1.0,
    "shopping": 1.0,
    "utilities": 2.0,        # Add this line
    "entertainment": 1.5,    # Add this line
}
```

### Modifying Base Points

If a card earns 2x points on everything:

```python
base_points=2.0,  # Changed from 1.0 to 2.0
```

### Deactivating a Card Temporarily

Set `is_active=False`:

```python
card = CreditCard(
    name="Old Card",
    is_active=False,  # This card won't be recommended
    # ... other settings
)
```

---

## Troubleshooting

### Issue: "python: command not found"

**Solution:** Use `python3` instead:
```bash
python3 src/demo.py
python3 src/main.py
```

### Issue: "ModuleNotFoundError: No module named 'data'"

**Solution:** Make sure you're in the correct directory:
```bash
cd "/Users/ynorice/Desktop/Desktop - Alex的MacBook Pro/Side_projects/PointsMaximizer-1/src"
python3 demo.py
```

### Issue: Changes to cards aren't showing up

**Solution:** Make sure you save the file after editing `data/sample_cards.py`, then restart the app.

### Issue: "The card I added isn't showing up"

**Solution:** Check that:
1. The card variable is defined (e.g., `card5 = CreditCard(...)`)
2. It's added to the return list: `return [card1, card2, card3, card4, card5]`
3. The file is saved

---

## 📊 Understanding the Recommendations

When you ask for a recommendation, you get:

```
============================================================
💳 BEST CARD FOR $100.00 DINING PURCHASE
============================================================

✅ USE: American Express Gold
   Points earned: 400.0 pts
   ROI: 4.0%

📊 ALL CARDS RANKED:
   1. American Express Gold: 400.0 pts (4.0%)
   2. Chase Sapphire Preferred: 300.0 pts (3.0%)
```

- **Best Card**: The card that earns the most points for this purchase
- **Points earned**: Total points you'll earn with the recommended card
- **ROI**: Return on investment (higher % = better return)
- **Ranking**: All cards sorted by points earned

---

## 💡 Real-World Examples

### Example 1: You're going out to dinner ($75)

1. Run: `python3 src/main.py`
2. Select option 1 (Get recommendation)
3. Enter amount: `75`
4. Select category: `2` (Dining)
5. **Result**: See which card gives you the most points!

### Example 2: Grocery shopping ($150)

1. Run: `python3 src/main.py`
2. Select option 1
3. Enter amount: `150`
4. Select category: `3` (Groceries)
5. **Result**: Your best card for groceries

### Example 3: Book a flight ($400)

1. Run: `python3 src/main.py`
2. Select option 1
3. Enter amount: `400`
4. Select category: `1` (Travel)
5. **Result**: Maximum travel points!

---

## 🎯 Next Steps

1. ✅ **Run the demo** to understand how it works
2. ✅ **Edit your cards** in `data/sample_cards.py`
3. ✅ **Run interactive mode** and test with real purchases
4. ✅ **Add more categories** if needed
5. ✅ **Share your results!**

---

## 📚 File Reference

| File | Purpose |
|------|---------|
| `src/card_model.py` | Credit card data structure (don't change) |
| `src/recommendation_engine.py` | Recommendation logic (don't change) |
| `src/main.py` | Interactive app - modify categories here |
| `src/demo.py` | Demo script (don't change) |
| `data/sample_cards.py` | **YOUR CARDS GO HERE** ← Edit this! |
| `README.md` | Full project documentation |

---

## 🆘 Need Help?

- **Syntax error?** Check that your Python code matches the examples (colons, commas, etc.)
- **Card not showing?** Make sure it's in the return statement
- **Wrong points calculated?** Double-check your multipliers match your actual card benefits
- **Missing category?** Add it to both the categories list AND all card definitions

---

**Happy points maximizing! 🎉**

Make sure to check your actual card benefits and update multipliers accordingly. The more accurate your card data, the better the recommendations!
