import asyncio
from unittest.mock import AsyncMock, MagicMock, call

from cogs import assign as assign_mod


def test_assign_league_inserts_new_league():
    cursor = MagicMock()
    cursor.fetchall.return_value = []
    connection = MagicMock()
    assign_mod.c = cursor
    assign_mod.connection = connection

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    assign_instance = assign_mod.Assign()

    asyncio.run(assign_instance.assign_league(interaction, "test", "1"))

    cursor.execute.assert_any_call(
        "SELECT * FROM league WHERE league_name = %s;", ("test",)
    )
    cursor.execute.assert_any_call(
        "INSERT INTO league (league_name,league_number) VALUES(%s,%s)",
        ("test", "1"),
    )
    connection.commit.assert_called_once()
    interaction.response.send_message.assert_awaited_with(
        "League successfully assigned."
    )


def test_assign_league_existing_league():
    cursor = MagicMock()
    cursor.fetchall.return_value = [("row",)]
    connection = MagicMock()
    assign_mod.c = cursor
    assign_mod.connection = connection

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    assign_instance = assign_mod.Assign()

    asyncio.run(assign_instance.assign_league(interaction, "test", "1"))

    connection.commit.assert_not_called()
    # ensure insert was not attempted
    insert_call = (
        "INSERT INTO league (league_name,league_number) VALUES(%s,%s)",
        ("test", "1"),
    )
    assert insert_call not in [call.args for call in cursor.execute.call_args_list]
    interaction.response.send_message.assert_awaited_with(
        "League name or number already exists, please try again with a different combination."
    )
