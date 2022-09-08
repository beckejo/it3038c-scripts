#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
TODAY=$(date)

echo "As of $TODAY, there have been $POSITIVE positive COVID tests and $NEGATIVE negative tests, with $HOSPITALIZED people currently fighting covid in a hospital. There have been $DEATHS deaths."
