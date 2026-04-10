{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "516b0815-bb96-4acf-8786-53a8067eeed1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📊 Stock Portfolio Tracker\n",
      "Available stocks: AAPL, TSLA, GOOG, AMZN\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter stock name (or 'done' to finish):  AAPL\n",
      "Enter quantity of AAPL:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Added AAPL worth ₹540\n"
     ]
    }
   ],
   "source": [
    "def stock_tracker():\n",
    "    # Predefined stock prices\n",
    "    prices = {\n",
    "        \"AAPL\": 180,\n",
    "        \"TSLA\": 250,\n",
    "        \"GOOG\": 2800,\n",
    "        \"AMZN\": 3300\n",
    "    }\n",
    "\n",
    "    total_investment = 0\n",
    "\n",
    "    print(\"📊 Stock Portfolio Tracker\")\n",
    "    print(\"Available stocks:\", \", \".join(prices.keys()))\n",
    "    \n",
    "    while True:\n",
    "        stock = input(\"Enter stock name (or 'done' to finish): \").upper()\n",
    "        \n",
    "        if stock == \"DONE\":\n",
    "            break\n",
    "        \n",
    "        if stock in prices:\n",
    "            qty = int(input(f\"Enter quantity of {stock}: \"))\n",
    "            value = prices[stock] * qty\n",
    "            total_investment += value\n",
    "            print(f\"✅ Added {stock} worth ₹{value}\")\n",
    "        else:\n",
    "            print(\"❌ Stock not available\")\n",
    "\n",
    "    print(f\"\\n💰 Total Investment Value: ₹{total_investment}\")\n",
    "\n",
    "# Run\n",
    "stock_tracker()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4689d9dc-77c1-4e35-80a6-c69678686e7c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
