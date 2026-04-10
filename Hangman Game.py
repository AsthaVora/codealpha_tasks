{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "afd319b9-cf62-4b1b-996a-52ba0e57a79e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎮 Welcome to Hangman!\n",
      "The word has 4 letters.\n",
      "\n",
      "Word: _ _ _ _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  java\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "⚠️ Please enter a single letter!\n",
      "\n",
      "Word: _ _ _ _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  j\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct guess!\n",
      "\n",
      "Word: j _ _ _\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct guess!\n",
      "\n",
      "Word: j a _ a\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a letter:  v\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct guess!\n",
      "🎉 You won! The word was 'java'\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def hangman():\n",
    "    words = [\"python\", \"java\", \"computer\", \"science\", \"program\"]\n",
    "    word = random.choice(words)\n",
    "    guessed = []\n",
    "    attempts = 6\n",
    "\n",
    "    print(\"🎮 Welcome to Hangman!\")\n",
    "    print(f\"The word has {len(word)} letters.\")\n",
    "\n",
    "    while attempts > 0:\n",
    "        display = \"\"\n",
    "        for letter in word:\n",
    "            display += letter + \" \" if letter in guessed else \"_ \"\n",
    "        \n",
    "        print(\"\\nWord:\", display.strip())\n",
    "        guess = input(\"Guess a letter: \").lower()\n",
    "        \n",
    "        if len(guess) != 1 or not guess.isalpha():\n",
    "            print(\"⚠️ Please enter a single letter!\")\n",
    "            continue\n",
    "        \n",
    "        if guess in guessed:\n",
    "            print(\"⚠️ Already guessed!\")\n",
    "            continue\n",
    "\n",
    "        guessed.append(guess)\n",
    "        \n",
    "        if guess not in word:\n",
    "            attempts -= 1\n",
    "            print(f\"❌ Wrong guess! Attempts left: {attempts}\")\n",
    "        else:\n",
    "            print(\"✅ Correct guess!\")\n",
    "\n",
    "        if all(letter in guessed for letter in word):\n",
    "            print(f\"🎉 You won! The word was '{word}'\")\n",
    "            break\n",
    "\n",
    "    else:\n",
    "        print(f\"💀 You lost! The word was '{word}'\")\n",
    "\n",
    "# Run game\n",
    "hangman()"
   ]
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
