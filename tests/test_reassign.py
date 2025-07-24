import asyncio
from unittest.mock import AsyncMock, MagicMock, call

from cogs import reassign as reassign_mod


def test_reassign_league_success():
    cursor = MagicMock()
    cursor.fetchall.return_value = [("row",)]
    connection = MagicMock()
    reassign_mod.c = cursor
    reassign_mod.connection = connection

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    instance = reassign_mod.Reassign()

    asyncio.run(instance.reassign_league(interaction, "test", "1"))

    cursor.execute.assert_any_call(
        "SELECT * FROM league WHERE league_name = %s;", ("test",)
    )
    cursor.execute.assert_any_call(
        "UPDATE league SET league_name= %s, league_number= %s WHERE league_name= %s",
        ("test", "1", "test"),
    )
    connection.commit.assert_called_once()
    interaction.response.send_message.assert_awaited_with(
        "League successfully reassigned."
    )


def test_reassign_league_not_found():
    cursor = MagicMock()
    cursor.fetchall.return_value = []
    connection = MagicMock()
    reassign_mod.c = cursor
    reassign_mod.connection = connection

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    instance = reassign_mod.Reassign()

    asyncio.run(instance.reassign_league(interaction, "test", "1"))

    connection.commit.assert_not_called()
    update_call = (
        "UPDATE league SET league_name= %s, league_number= %s WHERE league_name= %s",
        ("test", "1", "test"),
    )
    assert update_call not in [c.args for c in cursor.execute.call_args_list]
    interaction.response.send_message.assert_awaited_with(
        "League name or number does not  exist, please try again with a different combination."
    )
