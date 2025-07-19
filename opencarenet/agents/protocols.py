from typing import Protocol, Any


class Agent(Protocol):
    """
    Protocol for all agents in the opencarenet.agents package.
    """

    def act(self, observation: Any) -> Any:
        """
        Take an action based on the given observation.

        Args:
            observation: The input data for the agent.

        Returns:
            The agent's action or response.
        """
        ...
