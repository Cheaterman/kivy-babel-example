#!/bin/sh
pybabel extract \
    -F babel.ini \
    --project I18n \
    --version 0.1 \
    --msgid-bugs-address dev@local \
    --copyright-holder dev \
    -o messages.pot \
    .
# Assuming you already have languages
pybabel update \
    -i messages.pot \
    -d translations
