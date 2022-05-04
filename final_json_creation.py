import json

from Dictionary_qa import d_test
from Dictionary_qa import d_train
from Dictionary_qa import diz_qa
from Dictionary_qa import context_train
from Dictionary_qa import context_test
from Dictionary_qa import context_predict

json_prediction = [{"context": "Vin is a Mistborn of great power and skill.",
        "qas": [
            {
                "question": "What is Vin's speciality?",
                "id": "0",           }        ],   }]


json_format_train_test = [
    {
        "context": "ciao",
        "qas": [
            {
                "id": "",
                "is_impossible": False,
                "question": "",
                "answers": [
                    {
                        "text": "",
                        "answer_start": 71, }  ], }   ],  }]

train = json_format_train_test
test = json_format_train_test
prediction = json_prediction

list_qa_json_train = []
id = 1
answer_start = 1
for question in d_train:
    diz_qa_json = {}
    diz_qa_json["id"] = id
    diz_qa_json["is_impossible"] = False
    diz_qa_json["question"] = question
    diz_qa_json["answer"] = [{"text": d_train[question], "answer_start": answer_start}]
    id += 1
    answer_start += 1
    list_qa_json_train.append(diz_qa_json)

list_qa_json_test = []
id = 1
answer_start = 1
for question in d_test:
    diz_qa_json = {}
    diz_qa_json["id"] = id
    diz_qa_json["is_impossible"] = False
    diz_qa_json["question"] = question
    diz_qa_json["answer"] = [{"text": d_test[question], "answer_start": answer_start}]
    id += 1
    answer_start += 1
    list_qa_json_test.append(diz_qa_json)


if __name__ == '__main__':

    train[0]["qas"] = list_qa_json_train
    train[0]["context"] = context_train
    json_string_train = json.dumps(train)
    with open('train.json', 'w') as outfile:
        outfile.write(json_string_train)

    test[0]["qas"] = list_qa_json_test
    test[0]["context"] = context_test
    json_string_test = json.dumps(test)
    with open('test.json', 'w') as outfile:
        outfile.write(json_string_test)

    prediction[0]["context"] = context_predict
    print(prediction)