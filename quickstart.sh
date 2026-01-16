#!/bin/bash
# Quick Start Script for PointsMaximizer

echo "🎯 Welcome to PointsMaximizer!"
echo ""
echo "Running demo first to show you how it works..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd "$(dirname "$0")/src"
python3 demo.py

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Demo complete!"
echo ""
echo "📖 Next steps:"
echo "1. Edit data/sample_cards.py to add your actual credit cards"
echo "2. Run: python3 src/main.py (for interactive mode)"
echo "3. Customize categories and multipliers as needed"
echo ""
