{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "23d1a1d3-9c6e-4288-b7c1-1d058ea1aff1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Hi! This is Aira..your Chatbot Type 'bye' to exit.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  hello\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Hi there! 😊\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  your name\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: I'm a Aira created by AV! 😉\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  byee\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Sorry, I don't understand that.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  bye\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Goodbye! 👋\n"
     ]
    }
   ],
   "source": [
    "def chatbot():\n",
    "    print(\"Chatbot: Hi! This is Aira..your Chatbot Type 'bye' to exit.\")\n",
    "\n",
    "    while True:\n",
    "        user = input(\"You: \").lower()\n",
    "\n",
    "        if user == \"hello\":\n",
    "            print(\"Chatbot: Hi there! 😊\")\n",
    "        \n",
    "        elif user == \"how are you\":\n",
    "            print(\"Chatbot: I'm fine, thanks! How about you?\")\n",
    "        \n",
    "        elif user == \"i am fine\":\n",
    "            print(\"Chatbot: That's great to hear! 😄\")\n",
    "        \n",
    "        elif user == \"your name\":\n",
    "            print(\"Chatbot: I'm a Aira created by AV! 😉\")\n",
    "        \n",
    "        elif user == \"bye\":\n",
    "            print(\"Chatbot: Goodbye! 👋\")\n",
    "            break\n",
    "        \n",
    "        else:\n",
    "            print(\"Chatbot: Sorry, I don't understand that.\")\n",
    "\n",
    "# Run chatbot\n",
    "chatbot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5a11133-9c46-46e2-b505-1781c75f8c85",
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
