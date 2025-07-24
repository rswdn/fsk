import asyncio
from unittest.mock import AsyncMock, MagicMock

from cogs import matchups as matchups_mod


def test_get_matchups_no_league():
    cursor = MagicMock()
    cursor.fetchall.return_value = []
    matchups_mod.c = cursor

    league_cls = MagicMock()
    matchups_mod.League = league_cls

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    instance = matchups_mod.Matchups(None)
    asyncio.run(instance.get_matchups(interaction, "test", "1"))

    cursor.execute.assert_called_once_with(
        "SELECT league_number FROM league WHERE league_name = %s;", ("test",)
    )
    interaction.response.send_message.assert_awaited_with("No league found.")
    league_cls.assert_not_called()
