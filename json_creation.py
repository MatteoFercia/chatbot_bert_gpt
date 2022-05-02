
import json
train_data = [
    {
        "context": "The room will be previously cleaned and sanitized according to the Stanza Semplice standards."
        "Upon your arrival the room will be clean and sanitized through the use of disinfectants and ozone treatments that make the room safe and healthy."
            "The cleaning company will have already carried out its task according to the most recent regulations related to the emergency from COVID-19.",
        "qas": [
            {
                "id": "00001",
                "is_impossible": False,
                "question": "How my room will be cleaned before my arrival?",
                "answers": [
                    {
                        "text": "The cleaning company will have already carried out its task according to the most recent regulations related to the emergency from COVID-19",
                        "answer_start": 71,
                    }
                ],
            }
        ],
    },
    {
        "context": "Our mission? Semplify the life of students."
                    "We from Stanza Semplice provide rooms for rent for students and we are at your side to make your university time straightforward and happy."
                   "Choosing the rightaccommodation is fundamental: it is the place where you will prepare for your exams experience intense and vibrant times."
                   "For this reason we have selected for you the best rooms in the most significant Italian universities cities."
                    "No stress: you study, we provide you with the ideal room with eco-friendly optics, close to the university and to the public transport."
                   ".No deposit: with our All-Inclusive format you get everything you need without any bureaucratic problems or surprises.",
        "qas": [
            {
                "id": "00002",
                "is_impossible": False,
                "question": "What is the mission of Stanza Semplice?",
                "answers": [
                    {
                        "text": "Semplify the life of students",
                        "answer_start": 28,
                    }
                ],
            },
            {
                "id": "00003",
                "is_impossible": False,
                "question": "Where I can find the rooms of Stanza Semplice?",
                "answers": [
                    {
                        "text": "we have selected for you the best rooms in the most significant Italian universities cities",
                        "answer_start": 63,
                    }
                ],
            },
            {
                "id": "00004",
                "is_impossible": True,
                "question": "In the rent all the expenses are included?",
                "answers": [ {
                        "text": "with our All-Inclusive format you get everything you need without any bureaucratic problems or surprises",
                        "answer_start": 69,
                    } ],
            },
        ],
    },
]


json_string = json.dumps(train_data)
print(json_string)

with open('train.json', 'w') as outfile:
    outfile.write(json_string)




test_data = [
    {
        "context": "Stanza Semplice in Cagliari has 83 rooms, prices starts from 295 euros to 440 euros",
        "qas": [
            {
                "id": "00001",
                "is_impossible": False,
                "question": "How many rooms can I find in the city of Cagliari?",
                "answers": [
                    {
                        "text": "83 rooms",
                        "answer_start": 38,
                    },
                    {
                        "text": "You'll find 83 rooms",
                        "answer_start": 74,
                    },
                ],
            }
        ],
    },
    {
        "context": "Contracts with Stanza Semplice are individual."
                   "Each tenant has his own contract with his rent and room; "
                   "the other rooms do not affect your contractual position in any way."
                   "It's enough to have an identity document and an italian tax code.",
        "qas": [
            {
                "id": "00002",
                "is_impossible": False,
                "question": "What documents do I need to sign the contracts?",
                "answers": [
                    {
                        "text": "an identity document and an italian tax code",
                        "answer_start": 21,
                    }
                ],
            },
            {
                "id": "00003",
                "is_impossible": True,
                "question": "The contract is for the entire apartment?",
                "answers": [  {
                        "text": "No, Each tenant has his own contract with his rent and room",
                        "answer_start": 36,
                    }],
            },
        ],
    },
]


json_string_test = json.dumps(test_data)
print(json_string_test)

with open('test.json', 'w') as outfile:
    outfile.write(json_string_test)




#predict

predict =
    {
        "context": "Bologna is the University City par excellence. If you are a student looking for a room to rent, "
                   "Stanza Semplice can help you find it. Bologna is home to the oldest university in the western world, "
                   "the Alma Mater Studiorum, which to this day remains one of the most prominent in Italy and the world. "
                   "Stanza Semplice® in the city of Blogna has 105 rooms so far, prices starting from 360 euros to 900 euros",
        "qas": [
            {
                "question": "How much is it the cost for a room in Bologna?",
                "id": "0",
            }
        ],
    }
]

json_string_predict = json.dumps(predict)
print(json_string_predict)

with open('predict.json', 'w') as outfile:
    outfile.write(json_string_predict)
