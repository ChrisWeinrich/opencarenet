import pytest

from opencarenet.agents.fitness import FitnessAgent


@pytest.mark.asyncio()
async def test_fitness_agent_handle_ping_returns_nonempty_string():
    agent = FitnessAgent()
    result = await agent.handle("ping")
    assert isinstance(result, str)
    assert result.strip() != ""
