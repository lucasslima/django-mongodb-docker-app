#!/bin/bash
CFG_SCRIPT="{
    _id: 'apprepl',
    members: [
        {_id: 1, host: 'mongo1:27017'},
        {_id: 2, host: 'mongo2:27017'},
        {_id: 3, host: 'mongo3:27017'}
    ]
}"
docker-compose up
docker-compose exec mongo1 mongo localhost:27017 --eval "JSON.stringify(db.adminCommand({'replSetInitiate' : $CFG_SCRIPT}))"
