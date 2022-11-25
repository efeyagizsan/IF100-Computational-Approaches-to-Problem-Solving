

team_results = input('Please enter the Conf. Semis results: ').upper()
team_check = input('Please enter the team that you want to check: ').upper()


west = team_results.split(';')[0]
east = team_results.split(';')[1]

west_conf_semis = west.split(',')
east_conf_semis = east.split(',')

west_semis_1 = west_conf_semis[0].split(':')
west_semis_2 = west_conf_semis[1].split(':')

w_name = west_semis_1[0] + '-' + west_semis_2[0]
w_name_list = w_name.split('-')

w_score = west_semis_1[1] + '-' + west_semis_2[1]
w_score_list = w_score.split('-')

east_semis_1 = east_conf_semis[0].split(':')
east_semis_2 = east_conf_semis[1].split(':')

e_name = east_semis_1[0] + '-' + east_semis_2[0]
e_name_list = e_name.split('-')

e_score = east_semis_1[1] + '-' + east_semis_2[1]
e_score_list = e_score.split('-')

name_list = e_name_list + w_name_list 
score_list = e_score_list + w_score_list


if (team_check not in name_list):
  print(team_check +" does not exist!")

else:
  winner_list = []
  loser_list = []

  for i in name_list:
    if score_list[name_list.index(i)] < str(4) :
      loser_list.append(i)

  for e in name_list:
    if score_list[name_list.index(e)] > str(3) :
      winner_list.append(e)

  if team_check in loser_list :
    againstidx = loser_list.index(team_check)
    print(team_check + ' lost the game against ' + winner_list[againstidx] + ".")

  else:
    w1list = []
    w2list = []

    w1list.append(winner_list[0]) 
    w1list.append(winner_list[2])
    w2list.append(winner_list[1])
    w2list.append(winner_list[3])
    
    
    
    if team_check in w1list :

      nextidx = w1list.index(team_check)
      print('Next opponent of ' + team_check + ' will be ' + w2list[nextidx] + '.')
    
    elif team_check in w2list :
      next2idx = w2list.index(team_check)
      print('Next opponent of ' + team_check + ' will be ' + w1list[next2idx] + '.')

