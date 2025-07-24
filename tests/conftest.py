import sys
import os

# Ensure the project root is on the Python path so cogs can be imported
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Provide minimal stub modules for third party dependencies that are not
# installed in the test environment.  This allows the cogs modules to be
# imported without raising ImportError.
import types

discord_stub = types.ModuleType("discord")
discord_stub.Object = lambda id: None
discord_stub.Embed = object
discord_stub.Interaction = object

app_commands_stub = types.ModuleType("discord.app_commands")
checks_stub = types.ModuleType("checks")
checks_stub.has_role = lambda *a, **k: (lambda f: f)
app_commands_stub.command = lambda *a, **k: (lambda f: f)
app_commands_stub.checks = checks_stub

ext_stub = types.ModuleType("discord.ext")
commands_stub = types.ModuleType("discord.ext.commands")
commands_stub.Cog = object
commands_stub.Bot = object
commands_stub.bot = object
ext_stub.commands = commands_stub

discord_stub.ext = ext_stub
discord_stub.app_commands = app_commands_stub

sys.modules.setdefault("discord", discord_stub)
sys.modules.setdefault("discord.ext", ext_stub)
sys.modules.setdefault("discord.ext.commands", commands_stub)
sys.modules.setdefault("discord.app_commands", app_commands_stub)

sleeper_stub = types.ModuleType("sleeper_wrapper")
sleeper_stub.League = object
sys.modules.setdefault("sleeper_wrapper", sleeper_stub)

# psycopg2 stub so that db_connect can be imported
from unittest.mock import MagicMock
psycopg2_stub = types.ModuleType("psycopg2")
psycopg2_stub.connect = MagicMock(return_value=MagicMock(cursor=MagicMock()))
psycopg2_stub.Error = Exception
sys.modules.setdefault("psycopg2", psycopg2_stub)

# Minimal pandas and tabulate stubs for modules that import them
pandas_stub = types.ModuleType("pandas")
pandas_stub.DataFrame = object
sys.modules.setdefault("pandas", pandas_stub)

tabulate_stub = types.ModuleType("tabulate")
tabulate_stub.tabulate = lambda *a, **k: ""
sys.modules.setdefault("tabulate", tabulate_stub)
