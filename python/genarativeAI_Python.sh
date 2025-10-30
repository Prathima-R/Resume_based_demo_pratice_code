#!/bin/bash
echo "🔹 Checking Python installation..."
python3 --version || { echo "❌ Python not found"; exit 1; }

echo "🔹 Creating virtual environment..."
python3 -m venv myenv
source myenv/bin/activate

echo "🔹 Installing packages..."
pip install --upgrade pip
pip install numpy pandas matplotlib seaborn plotly openpyxl tabulate

echo "🔹 Saving requirements..."
pip freeze > requirements.txt

echo "✅ Setup complete!"

