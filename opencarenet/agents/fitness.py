from typing import Any
from .protocols import Agent


class FitnessAgent:
    """
    An agent that provides fitness-related actions.
    """

    def act(self, observation: Any) -> str:
        """
        Return a fitness recommendation based on the observation.

        Args:
            observation: The input data for the agent.

        Returns:
            A string with a fitness recommendation.
        """
        # Placeholder logic
        return "Remember to take a walk today!"
