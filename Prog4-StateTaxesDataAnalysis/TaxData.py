# UIN: 656538534
# repl.it URL: https://replit.com/@MykolaTurchak/Project-3#main.py
 
######################################################
import csv
import requests
import json
import matplotlib.pyplot as plt


def get_data_from_file():
  f = open("tax_return_data_2018.csv")
  reader = csv.reader(f)
  data = list(reader)
  f.close()
  return data

# print(get_data_from_file(




def get_data_from_internet():
  req = requests.get('https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt')
  j_req = req.json()
  return j_req

# print(get_data_from_internet())




def get_state_population(state_inp):
  state_populations = {}
  data = get_data_from_internet()
  state_code = ''


  # with open('states_titlecase.json') as f:
  #   reader = json.load(f)
    
  #   for state_name_dict in reader:
  #     # print(state_name_dict)
  #     for state_name in state_name_dict:
  #       # print(state_name_dict[state_name])

  #       if state_inp in state_name_dict[state_name]:

  #         state_code = state_name_dict['abbreviation']
  #         # print(state_code)

  for state_dict in data:
    for state in state_dict:

      state_populations[state[1:]] = int(state_dict[state])

  return state_populations[state_inp]

# print(get_state_population('Alabama'))




def get_state_name(state_code):
  state_names = {}
  data = get_data_from_internet()
  state_name = ''

  # for state_dict in data:
  #   for state in state_dict:
      
  #     state_names[state[1:]] = int(state_dict[state])

  with open('states_titlecase.json') as f:
    reader = json.load(f)
    
    for state_name_dict in reader:
      for state_name in state_name_dict:
        if state_code in state_name_dict[state_name]:

          state_name = state_name_dict['name']
          return state_name

def chart():
  sum =0;
  for state_dict in get_data_from_internet():
    sum+=state_dict.val
  labels = []
  weight =[]
  for state_dict in get_data_from_internet():
      labels = state_dict.key
      weight = round(state_dict.val/sum,1)
  fig1, ax1 = plt.subplots()
  ax1.pie(weight, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  print(labels)

chart()
# plt.show()
# print(get_state_name('AR'))


# f = open('answers.txt','w')
# f.write(str(avg1)+'\n'+str(avg2)+'\n'+str(big_state)+'\n'+str(big_state2))
# f.close()


