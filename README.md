[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues open](https://img.shields.io/github/issues/RyanSowden/ffsk.svg?colour=orange)](https://github.com/RyanSowden/ffsk/issues)


# FSK

![](https://media.sproutsocial.com/uploads/2018/10/Fantasy-Sports.svg)

# Overview
FSK(Fantasy Sidekick) is a Python discord bot which uses the Sleeper Fantasy API to provide league information to a Discord server.
This is a self-hosted bot - meaning you will need to host and maintain your own instance.

Installing can be a little tricky as you have to setup a database but following [this](https://github.com/RyanSowden/fsk/wiki) guide should get you setup.

The default set of modules includes and is not limited to:

* Getting the standings for your league.
* Getting all the matchups & scores for your league.
* Getting all the starting lineups for your league.

# Installation
FSK currently is only supported on unix platforms,to install please refer to the wiki linked below:

* [FSK Wiki](https://github.com/RyanSowden/fsk/wiki)

# Quickstart
The wiki covers the full setup flow, but a minimal local run looks like:

1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment variables in a `.env` file (see the wiki for required values).
3. Run the bot: `python bot.py`

If you hit database errors, double-check the wiki setup guide for required tables.

# Testing
Run the test suite locally with:

`pytest`

# Supported versions
FSK is tested with Python 3.9+ on Unix-like platforms.

# Contributing
FSK is 100% open source and always looking at ways to become better, so if you have any ideas on ways to improve/add to the bot, create a pull request stating what you have changed/added.

# License
FSK is released under the [MIT License](https://opensource.org/licenses/MIT)
