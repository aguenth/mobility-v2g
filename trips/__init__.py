from otree.api import *
import json

doc = """
Trip diary where participants can add trips dynamically.
"""


class C(BaseConstants):
    NAME_IN_URL = 'trip_diary'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_CHOICES = [(f'{h:02}:{m:02}', f'{h:02}:{m:02}') for h in range(24) for m in (0, 30)]
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Tuesday = models.BooleanField(blank=True)
    Wednesday = models.BooleanField(blank=True)
    Thursday = models.BooleanField(blank=True)
    Friday = models.BooleanField(blank=True)
    Saturday = models.BooleanField(blank=True)
    Sunday = models.BooleanField(blank=True)

#Monday
    mo_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    mo_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    mo_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    mo_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    mo_distance_10 = models.IntegerField(blank=True, min=0, max=300)


# Tuesday
    tue_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    tue_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    tue_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    tue_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    tue_distance_10 = models.IntegerField(blank=True, min=0, max=300)


# Wednesday
    wed_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    wed_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    wed_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    wed_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    wed_distance_10 = models.IntegerField(blank=True, min=0, max=300)



# Thursday
    thu_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    thu_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    thu_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    thu_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    thu_distance_10 = models.IntegerField(blank=True, min=0, max=300)


# Friday
    fri_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    fri_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    fri_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    fri_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    fri_distance_10 = models.IntegerField(blank=True, min=0, max=300)


# Saturday
    sat_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    sat_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    sat_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    sat_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    sat_distance_10 = models.IntegerField(blank=True, min=0, max=300)


# Sunday
    sun_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Started day at:"
    )
    sun_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        label="Ended day at:"
    )

    sun_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_1 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_1 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_2 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_2 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_3 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_3 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_4 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_4 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_5 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_5 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_6 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_6 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_7 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_7 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_8 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_8 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_9 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_9 = models.IntegerField(blank=True, min=0, max=300)

    sun_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Outdoors', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_10 = models.IntegerField(blank=True, min=0, max=300)
    sun_distance_10 = models.IntegerField(blank=True, min=0, max=300)


class Monday(Page):
    form_model = 'player'
    form_fields = [
        'mo_first_trip', 'mo_last_trip', 'mo_additional_trip_1', 'mo_start_time_1', 'mo_duration_1', 'mo_distance_1',
        'mo_additional_trip_2', 'mo_start_time_2', 'mo_duration_2', 'mo_distance_2', 'mo_additional_trip_3',
        'mo_start_time_3', 'mo_duration_3', 'mo_distance_3', 'mo_additional_trip_4', 'mo_start_time_4',
        'mo_duration_4', 'mo_distance_4', 'mo_additional_trip_5', 'mo_start_time_5', 'mo_duration_5',
        'mo_distance_5', 'mo_additional_trip_6', 'mo_start_time_6', 'mo_duration_6', 'mo_distance_6',
        'mo_additional_trip_7', 'mo_start_time_7', 'mo_duration_7', 'mo_distance_7', 'mo_additional_trip_8',
        'mo_start_time_8', 'mo_duration_8', 'mo_distance_8', 'mo_additional_trip_9', 'mo_start_time_9',
        'mo_duration_9', 'mo_distance_9', 'mo_additional_trip_10', 'mo_start_time_10', 'mo_duration_10',
        'mo_distance_10', 'Thursday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'
    ]

    def vars_for_template(player: Player):
        mo_additional_trips = [
            getattr(player, 'mo_additional_trip_1', '') or '',
            getattr(player, 'mo_additional_trip_2', '') or '',
            getattr(player, 'mo_additional_trip_3', '') or '',
            getattr(player, 'mo_additional_trip_4', '') or '',
            getattr(player, 'mo_additional_trip_5', '') or '',
            getattr(player, 'mo_additional_trip_6', '') or '',
            getattr(player, 'mo_additional_trip_7', '') or '',
            getattr(player, 'mo_additional_trip_8', '') or '',
            getattr(player, 'mo_additional_trip_9', '') or '',
            getattr(player, 'mo_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': mo_additional_trips,
            'days': C.DAYS
        }


class Tuesday(Page):
    form_model = 'player'
    form_fields = [
        'tue_first_trip', 'tue_last_trip', 'tue_additional_trip_1', 'tue_start_time_1', 'tue_duration_1', 'tue_distance_1',
        'tue_additional_trip_2', 'tue_start_time_2', 'tue_duration_2', 'tue_distance_2', 'tue_additional_trip_3',
        'tue_start_time_3', 'tue_duration_3', 'tue_distance_3', 'tue_additional_trip_4', 'tue_start_time_4',
        'tue_duration_4', 'tue_distance_4', 'tue_additional_trip_5', 'tue_start_time_5', 'tue_duration_5',
        'tue_distance_5', 'tue_additional_trip_6', 'tue_start_time_6', 'tue_duration_6', 'tue_distance_6',
        'tue_additional_trip_7', 'tue_start_time_7', 'tue_duration_7', 'tue_distance_7', 'tue_additional_trip_8',
        'tue_start_time_8', 'tue_duration_8', 'tue_distance_8', 'tue_additional_trip_9', 'tue_start_time_9',
        'tue_duration_9', 'tue_distance_9', 'tue_additional_trip_10', 'tue_start_time_10', 'tue_duration_10',
        'tue_distance_10'
    ]

    def vars_for_template(player: Player):
        tue_additional_trips = [
            getattr(player, 'tue_additional_trip_1', '') or '',
            getattr(player, 'tue_additional_trip_2', '') or '',
            getattr(player, 'tue_additional_trip_3', '') or '',
            getattr(player, 'tue_additional_trip_4', '') or '',
            getattr(player, 'tue_additional_trip_5', '') or '',
            getattr(player, 'tue_additional_trip_6', '') or '',
            getattr(player, 'tue_additional_trip_7', '') or '',
            getattr(player, 'tue_additional_trip_8', '') or '',
            getattr(player, 'tue_additional_trip_9', '') or '',
            getattr(player, 'tue_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': tue_additional_trips
        }


class Wednesday(Page):
    form_model = 'player'
    form_fields = [
        'wed_first_trip', 'wed_last_trip', 'wed_additional_trip_1', 'wed_start_time_1', 'wed_duration_1', 'wed_distance_1',
        'wed_additional_trip_2', 'wed_start_time_2', 'wed_duration_2', 'wed_distance_2', 'wed_additional_trip_3',
        'wed_start_time_3', 'wed_duration_3', 'wed_distance_3', 'wed_additional_trip_4', 'wed_start_time_4',
        'wed_duration_4', 'wed_distance_4', 'wed_additional_trip_5', 'wed_start_time_5', 'wed_duration_5',
        'wed_distance_5', 'wed_additional_trip_6', 'wed_start_time_6', 'wed_duration_6', 'wed_distance_6',
        'wed_additional_trip_7', 'wed_start_time_7', 'wed_duration_7', 'wed_distance_7', 'wed_additional_trip_8',
        'wed_start_time_8', 'wed_duration_8', 'wed_distance_8', 'wed_additional_trip_9', 'wed_start_time_9',
        'wed_duration_9', 'wed_distance_9', 'wed_additional_trip_10', 'wed_start_time_10', 'wed_duration_10',
        'wed_distance_10'
    ]

    def vars_for_template(player: Player):
        wed_additional_trips = [
            getattr(player, 'wed_additional_trip_1', '') or '',
            getattr(player, 'wed_additional_trip_2', '') or '',
            getattr(player, 'wed_additional_trip_3', '') or '',
            getattr(player, 'wed_additional_trip_4', '') or '',
            getattr(player, 'wed_additional_trip_5', '') or '',
            getattr(player, 'wed_additional_trip_6', '') or '',
            getattr(player, 'wed_additional_trip_7', '') or '',
            getattr(player, 'wed_additional_trip_8', '') or '',
            getattr(player, 'wed_additional_trip_9', '') or '',
            getattr(player, 'wed_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': wed_additional_trips
        }


class Thursday(Page):
    form_model = 'player'
    form_fields = [
        'thu_first_trip', 'thu_last_trip', 'thu_additional_trip_1', 'thu_start_time_1', 'thu_duration_1', 'thu_distance_1',
        'thu_additional_trip_2', 'thu_start_time_2', 'thu_duration_2', 'thu_distance_2', 'thu_additional_trip_3',
        'thu_start_time_3', 'thu_duration_3', 'thu_distance_3', 'thu_additional_trip_4', 'thu_start_time_4',
        'thu_duration_4', 'thu_distance_4', 'thu_additional_trip_5', 'thu_start_time_5', 'thu_duration_5',
        'thu_distance_5', 'thu_additional_trip_6', 'thu_start_time_6', 'thu_duration_6', 'thu_distance_6',
        'thu_additional_trip_7', 'thu_start_time_7', 'thu_duration_7', 'thu_distance_7', 'thu_additional_trip_8',
        'thu_start_time_8', 'thu_duration_8', 'thu_distance_8', 'thu_additional_trip_9', 'thu_start_time_9',
        'thu_duration_9', 'thu_distance_9', 'thu_additional_trip_10', 'thu_start_time_10', 'thu_duration_10',
        'thu_distance_10'
    ]

    def vars_for_template(player: Player):
        thu_additional_trips = [
            getattr(player, 'thu_additional_trip_1', '') or '',
            getattr(player, 'thu_additional_trip_2', '') or '',
            getattr(player, 'thu_additional_trip_3', '') or '',
            getattr(player, 'thu_additional_trip_4', '') or '',
            getattr(player, 'thu_additional_trip_5', '') or '',
            getattr(player, 'thu_additional_trip_6', '') or '',
            getattr(player, 'thu_additional_trip_7', '') or '',
            getattr(player, 'thu_additional_trip_8', '') or '',
            getattr(player, 'thu_additional_trip_9', '') or '',
            getattr(player, 'thu_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': thu_additional_trips
        }


class Friday(Page):
    form_model = 'player'
    form_fields = [
        'fri_first_trip', 'fri_last_trip', 'fri_additional_trip_1', 'fri_start_time_1', 'fri_duration_1', 'fri_distance_1',
        'fri_additional_trip_2', 'fri_start_time_2', 'fri_duration_2', 'fri_distance_2', 'fri_additional_trip_3',
        'fri_start_time_3', 'fri_duration_3', 'fri_distance_3', 'fri_additional_trip_4', 'fri_start_time_4',
        'fri_duration_4', 'fri_distance_4', 'fri_additional_trip_5', 'fri_start_time_5', 'fri_duration_5',
        'fri_distance_5', 'fri_additional_trip_6', 'fri_start_time_6', 'fri_duration_6', 'fri_distance_6',
        'fri_additional_trip_7', 'fri_start_time_7', 'fri_duration_7', 'fri_distance_7', 'fri_additional_trip_8',
        'fri_start_time_8', 'fri_duration_8', 'fri_distance_8', 'fri_additional_trip_9', 'fri_start_time_9',
        'fri_duration_9', 'fri_distance_9', 'fri_additional_trip_10', 'fri_start_time_10', 'fri_duration_10',
        'fri_distance_10'
    ]

    def vars_for_template(player: Player):
        fri_additional_trips = [
            getattr(player, 'fri_additional_trip_1', '') or '',
            getattr(player, 'fri_additional_trip_2', '') or '',
            getattr(player, 'fri_additional_trip_3', '') or '',
            getattr(player, 'fri_additional_trip_4', '') or '',
            getattr(player, 'fri_additional_trip_5', '') or '',
            getattr(player, 'fri_additional_trip_6', '') or '',
            getattr(player, 'fri_additional_trip_7', '') or '',
            getattr(player, 'fri_additional_trip_8', '') or '',
            getattr(player, 'fri_additional_trip_9', '') or '',
            getattr(player, 'fri_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': fri_additional_trips
        }


class Saturday(Page):
    form_model = 'player'
    form_fields = [
        'sat_first_trip', 'sat_last_trip', 'sat_additional_trip_1', 'sat_start_time_1', 'sat_duration_1',
        'sat_distance_1',
        'sat_additional_trip_2', 'sat_start_time_2', 'sat_duration_2', 'sat_distance_2', 'sat_additional_trip_3',
        'sat_start_time_3', 'sat_duration_3', 'sat_distance_3', 'sat_additional_trip_4', 'sat_start_time_4',
        'sat_duration_4', 'sat_distance_4', 'sat_additional_trip_5', 'sat_start_time_5', 'sat_duration_5',
        'sat_distance_5', 'sat_additional_trip_6', 'sat_start_time_6', 'sat_duration_6', 'sat_distance_6',
        'sat_additional_trip_7', 'sat_start_time_7', 'sat_duration_7', 'sat_distance_7', 'sat_additional_trip_8',
        'sat_start_time_8', 'sat_duration_8', 'sat_distance_8', 'sat_additional_trip_9', 'sat_start_time_9',
        'sat_duration_9', 'sat_distance_9', 'sat_additional_trip_10', 'sat_start_time_10', 'sat_duration_10',
        'sat_distance_10'
    ]

    def vars_for_template(player: Player):
        sat_additional_trips = [
            getattr(player, 'sat_additional_trip_1', '') or '',
            getattr(player, 'sat_additional_trip_2', '') or '',
            getattr(player, 'sat_additional_trip_3', '') or '',
            getattr(player, 'sat_additional_trip_4', '') or '',
            getattr(player, 'sat_additional_trip_5', '') or '',
            getattr(player, 'sat_additional_trip_6', '') or '',
            getattr(player, 'sat_additional_trip_7', '') or '',
            getattr(player, 'sat_additional_trip_8', '') or '',
            getattr(player, 'sat_additional_trip_9', '') or '',
            getattr(player, 'sat_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': sat_additional_trips
        }


class Sunday(Page):
    form_model = 'player'
    form_fields = [
        'sun_first_trip', 'sun_last_trip', 'sun_additional_trip_1', 'sun_start_time_1', 'sun_duration_1',
        'sun_distance_1',
        'sun_additional_trip_2', 'sun_start_time_2', 'sun_duration_2', 'sun_distance_2', 'sun_additional_trip_3',
        'sun_start_time_3', 'sun_duration_3', 'sun_distance_3', 'sun_additional_trip_4', 'sun_start_time_4',
        'sun_duration_4', 'sun_distance_4', 'sun_additional_trip_5', 'sun_start_time_5', 'sun_duration_5',
        'sun_distance_5', 'sun_additional_trip_6', 'sun_start_time_6', 'sun_duration_6', 'sun_distance_6',
        'sun_additional_trip_7', 'sun_start_time_7', 'sun_duration_7', 'sun_distance_7', 'sun_additional_trip_8',
        'sun_start_time_8', 'sun_duration_8', 'sun_distance_8', 'sun_additional_trip_9', 'sun_start_time_9',
        'sun_duration_9', 'sun_distance_9', 'sun_additional_trip_10', 'sun_start_time_10', 'sun_duration_10',
        'sun_distance_10'
    ]

    def vars_for_template(player: Player):
        sun_additional_trips = [
            getattr(player, 'sun_additional_trip_1', '') or '',
            getattr(player, 'sun_additional_trip_2', '') or '',
            getattr(player, 'sun_additional_trip_3', '') or '',
            getattr(player, 'sun_additional_trip_4', '') or '',
            getattr(player, 'sun_additional_trip_5', '') or '',
            getattr(player, 'sun_additional_trip_6', '') or '',
            getattr(player, 'sun_additional_trip_7', '') or '',
            getattr(player, 'sun_additional_trip_8', '') or '',
            getattr(player, 'sun_additional_trip_9', '') or '',
            getattr(player, 'sun_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': sun_additional_trips
        }


page_sequence = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
