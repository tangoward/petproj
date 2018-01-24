from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime, timedelta
import requests
import timeago


class DotaMatches(TemplateView):
    template_name = 'matches/dota_matches.html'

    def get(self, request, *args, **kwargs):
        # Get the URL of the API using requests module
        url = requests.get('https://api.opendota.com/api/proMatches')
        # Decode the data
        json_data = url.json()

        # List that will contain dictionaries
        game_data = []

        for data in json_data:
            # Will contain the values from the dictionary data of json_data
            j_data = {}
            j_data['League'] = data['league_name']
            j_data['Radiant'] = data['radiant_name']
            j_data['Dire'] = data['dire_name']
            j_data['Duration'] = str(timedelta(seconds=data['duration']))
            j_data['Finished'] = timeago.format(datetime.now() - datetime.fromtimestamp(data['start_time']))

            # Check who the winner of the match
            if data['radiant_win'] == False:
                j_data['Winner'] = data['dire_name']
            else:
                j_data['Winner'] = data['radiant_name']

            # Put the data in our game_data list
            game_data.append(j_data)

        return render(request, self.template_name, {'game_data': game_data})
