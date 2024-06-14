from otree.api import *
import json

doc = """
Trip diary where participants can add trips dynamically.
"""

class C(BaseConstants):
    NAME_IN_URL = 'trip_diary'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    trip_1 = models.StringField(label="First trip")
    trip_2 = models.StringField(label="Last trip")
    additional_trips = models.LongStringField(blank=True, initial=json.dumps([]))  # Store as JSON

class TripDiary(Page):
    form_model = 'player'
    form_fields = ['trip_1', 'trip_2']

    def vars_for_template(player: Player):
        additional_trips = json.loads(player.additional_trips)  # Load additional trips from JSON
        return {
            'additional_trips': additional_trips
        }

    def before_next_page(player: Player, timeout_happened):
        additional_trips = player.participant.vars.get('additional_trips', [])
        player.additional_trips = json.dumps(additional_trips)  # Save additional trips as JSON

page_sequence = [TripDiary]
