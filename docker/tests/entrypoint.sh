#!/bin/bash

export FIREBASE_CREDENTIALS=$(cat ./flexier-app-firebase-adminsdk-o7mqw-ea14b93862.json)

pytest $@


