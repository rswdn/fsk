import asyncio
from unittest.mock import AsyncMock, MagicMock

from cogs import standings as standings_mod


def test_get_standings_no_league():
    cursor = MagicMock()
    cursor.fetchall.return_value = []
    standings_mod.c = cursor

    league_cls = MagicMock()
    standings_mod.League = league_cls

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    instance = standings_mod.Standings(None)
    asyncio.run(instance.get_standings(interaction, "test"))

    cursor.execute.assert_called_once_with(
        "SELECT league_number FROM league WHERE league_name = %s;", ("test",)
    )
    interaction.response.send_message.assert_awaited_with("No league found.")
    league_cls.assert_not_called()
