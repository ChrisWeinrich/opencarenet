"""Smoke test for FitnessAgent."""

import pytest

from opencarenet.agents.fitness import FitnessAgent


def test_fitness_agent_act_returns_nonempty_string() -> None:
    """Test that FitnessAgent.act returns a non-empty string."""
    agent = FitnessAgent()
    result = agent.act("ping")
    assert isinstance(result, str)
    assert result.strip() != ""
