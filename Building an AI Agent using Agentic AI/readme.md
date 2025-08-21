Agentic AI refers to artificial intelligence systems that can perceive their environment, make decisions, and act autonomously to achieve a goal. These agents typically use reinforcement learning (RL) methods to optimize their behaviour over time through interactions with an environment.

Understanding the Components of Agentic AI
Agentic AI involves several key components. In this article, I’ll be building an AI Agent for trading. So, let’s understand the key components of Agentic AI with our example:

The Agent: The agent is the decision-making entity in the AI system. In our case, the DQN trading agent will be responsible for making trading decisions based on market data.
The Environment: The environment is the external system in which the agent operates. Our trading environment will consist of stock market data, where the agent will interact with price movements and execute trades.
The State: The state represents the information available to the agent at any given time. Our trading agent’s state includes the stock’s closing price, moving averages, and daily returns.
The Action Space: The action space defines what actions the agent can take. Our trading agent has three possible actions: Buy, Sell, and Hold.
The Reward Function: The reward function determines the agent’s performance by assigning a numerical value to its actions. The goal of our trading agent will be to maximize total profit by the end of the trading session.
Having this knowledge will help you understand all the steps we will take further to build an AI Agent using Agentic AI.
