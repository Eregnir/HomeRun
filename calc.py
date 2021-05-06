import json
import pandas as pd


history = pd.read_csv('history_data.csv', encoding='latin-1')

# Calculate sum of hours spent on each event.

filter_history = history.filter(items=['event_title', 'duration_in_hours'])

sum_per_events = filter_history.groupby(['event_title']).sum()

# change sum_per_events to json format.
sum_per_events.to_json('file.json', orient='split', compression='infer', index='true')
final_df = pd.read_json('file.json', orient='split', compression='infer')
# final_df.to_json()

# check
done_df = final_df.to_json()


# Making the dataframe to kids

filter_attendees = history.filter(items=['event_title', 'duration_in_hours', 'attendees'])

kids = filter_attendees.groupby(['attendees']).sum()

# change sum_per_events to json format.
kids.to_json('file.json', orient='split', compression='infer', index='true')
kids_df = pd.read_json('file.json', orient='split', compression='infer')
# final_df.to_json()

# check
attendees_sum_df = kids_df.to_json()





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