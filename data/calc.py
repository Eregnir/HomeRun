import json
import pandas as pd

history = pd.read_csv('history_data.csv.csv', encoding='latin-1')


# def get_books():
#     print("Hello") ##delete
#     request_params = request.json
#     print(request_params) #delete
#     result = recommend_book(request_params['name'])
#
#     response = {
#         'user_id': request_params['user_id'],
#         'isbns': result
#     }
#     return json.dumps(response)