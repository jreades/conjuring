#!/usr/bin/env bash

DISPLAY=$(echo $DISPLAY | sed 's|localhost||')

export DISPLAY="$DISPLAY"

