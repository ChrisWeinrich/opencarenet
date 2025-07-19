"""Protocols for agents in the opencarenet.agents package."""

from typing import Protocol


class Agent(Protocol):
    """Protocol for all agents in the opencarenet.agents package."""

    def act(self, observation: str) -> str:
        """Take an action based on the given observation.

        Args:
        ----
            observation (str): The input data for the agent.

        Returns:
        -------
            str: The agent's action or response.

        """
        ...
