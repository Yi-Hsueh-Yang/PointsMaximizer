# 🎯 PointsMaximizer - Quick Reference Card

## Command Cheat Sheet

### 🎬 Run Demo (5 minutes)
```bash
cd "Side_projects/PointsMaximizer-1/src"
python3 demo.py
```
Shows 5 scenarios with sample cards.

### 🎮 Interactive App (Live)
```bash
cd "Side_projects/PointsMaximizer-1/src"
python3 main.py
```
Get recommendations for your actual purchases.

---

## 📂 Files You Need to Know

| File | Purpose | Edit? |
|------|---------|-------|
| `data/sample_cards.py` | Your credit cards | **YES** - Add your cards here |
| `src/main.py` | Interactive app | Maybe - add categories |
| `src/card_model.py` | Card structure | No - leave as is |
| `src/recommendation_engine.py` | Recommendation logic | No - leave as is |
| `src/demo.py` | Demo script | No - leave as is |

---

## 🃏 How to Add Your Credit Card

### 1. Open: `data/sample_cards.py`

### 2. Find where cards are defined:
```python
card1 = CreditCard(
    name="Chase Sapphire Preferred",
    ...
)
```

### 3. Copy & Paste This Template:
```python
my_card = CreditCard(
    name="Your Card Name Here",
    bank="Your Bank Name",
    is_active=True,
    base_points=1.0,
    category_multipliers={
        "travel": 1.0,
        "dining": 1.0,
        "groceries": 1.0,
        "gas": 1.0,
        "shopping": 1.0,
    },
    annual_fee=0.0,
)
```

### 4. Replace with YOUR card benefits
For example, if your card gives:
- 3x points on dining
- 1.5x points on travel
- 1x points on everything else

```python
my_card = CreditCard(
    name="My Best Card",
    bank="Chase",
    is_active=True,
    base_points=1.0,
    category_multipliers={
        "travel": 1.5,      # 1.5x travel
        "dining": 3.0,      # 3x dining
        "groceries": 1.0,   # 1x groceries
        "gas": 1.0,         # 1x gas
        "shopping": 1.0,    # 1x shopping
    },
    annual_fee=95.0,    # Your annual fee
)
```

### 5. Add to return list:
Find this at the bottom of the file:
```python
return [card1, card2, card3, card4]
```

Add your card:
```python
return [card1, card2, card3, card4, my_card]
```

### 6. Save and test!
```bash
python3 src/main.py
```

---

## 📊 Understanding Multipliers

**Multiplier = Points per dollar spent**

- `1.0` = 1 point per $1 = 1%
- `2.0` = 2 points per $1 = 2%
- `3.0` = 3 points per $1 = 3%
- `4.0` = 4 points per $1 = 4%

**Example:**
- $100 purchase with 3.0 multiplier = 300 points
- $50 purchase with 2.0 multiplier = 100 points

---

## 🎯 Categories Available

Default categories (can add more):
- `"travel"` → Flights, hotels, transportation
- `"dining"` → Restaurants, food delivery
- `"groceries"` → Grocery stores
- `"gas"` → Gas stations
- `"shopping"` → Retail, online shopping
- `"other"` → Everything else

---

## 🔄 How the Recommendation Engine Works

1. **You enter**: Amount + Category
2. **Engine calculates**: Points for each card in that category
3. **Engine returns**: 
   - Best card with highest points
   - Ranking of all cards
   - ROI percentage

**Example:**
- You: "$100 dinner"
- Engine checks all cards' dining multipliers
- Shows: "Use Amex Gold for 400 points"

---

## 📱 Interactive App Menu

When you run `python3 src/main.py`:

```
Options:
1. Get recommendation for a purchase
2. View all your cards
3. View all categories
4. Exit
```

### Option 1: Get Recommendation
- Enter amount: `75`
- Select category: `2` (Dining)
- Instant recommendation!

### Option 2: View Cards
- Shows all your cards
- Lists benefits for each
- Shows annual fees

### Option 3: View Categories
- Lists all available categories
- Helps you choose correct category

### Option 4: Exit
- Closes the app

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `python: command not found` | Use `python3` instead |
| `ModuleNotFoundError` | Run from `src/` folder |
| Card doesn't appear | Check it's in return list |
| Wrong points | Check multiplier values |
| Can't run interactive app | Make sure Python 3 is installed |

---

## 💡 Real Examples

### Example 1: AmEx Gold
```python
amex = CreditCard(
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
)
```

### Example 2: Chase Sapphire
```python
chase = CreditCard(
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

### Example 3: No Annual Fee Card
```python
walmart = CreditCard(
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
)
```

---

## ✨ Tips

✅ **Copy from examples** → Use the examples above as templates
✅ **Check your card** → Get benefits from your card's website
✅ **Test with demo first** → Run demo to see how it works
✅ **Start simple** → Add basic cards first, then refine
✅ **Save often** → Save your edits to `sample_cards.py`

---

## 🎓 Complete Workflow

1. **Understand it** → Read README.md
2. **Learn details** → Read GUIDE.md
3. **Try demo** → `python3 src/demo.py`
4. **Copy template** → From this file
5. **Add your cards** → Edit `data/sample_cards.py`
6. **Run app** → `python3 src/main.py`
7. **Get recommendations** → Use and enjoy!

---

## 📞 Quick Help

**How do I add a card?** → Edit `data/sample_cards.py`, copy template, paste, customize

**How do I add a category?** → Edit categories list in `src/main.py`

**How do I deactivate a card?** → Set `is_active=False`

**How do I verify it works?** → Run `python3 src/demo.py`

---

**Ready? Let's go!** 🚀

Start with: `python3 src/demo.py`
