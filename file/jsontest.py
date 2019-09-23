#!/usr/bin/env python3

import json
import json

data = [ 
            {   
                        'user_id': 1000,
                                'name': 'Shiyan',
                                        'pass': 10, 
                                                'study_time': 50, 
                                                    },  
                {   
                            'user_id': 2000,
                                    'name': 'Lou',
                                            'pass': 15, 
                                                    'study_time': 171,
                                                        }   
                ]


json.dumps(data)

with open('/tmp/jsontest.json', 'w') as f:
    f.write(json.dumps(data))
