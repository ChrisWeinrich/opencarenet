"""Fitness agent implementation for the opencarenet.agents package."""


class FitnessAgent:
    """An agent that provides fitness-related actions."""

    def act(self: "FitnessAgent", observation: str) -> str:
        """Return a fitness recommendation based on the observation.

        Args:
        ----
            observation (str): The input data for the agent.

        Returns:
        -------
            str: A string with a fitness recommendation.

        """
        _ = observation  # unused argument
        # Placeholder logic
        return "Remember to take a walk today!"
