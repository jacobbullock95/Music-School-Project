from django.db import models
from django.urls import reverse

INST_CHOICES = (
        ("Guitar", 'Guitar'),
        ("Drums", 'Drums'),
        ("Violin", 'Violin'),
        ("Saxophone", 'Saxophone'),
        ("Clarinet", 'Clarinet'),
        ("Piano", 'Piano'),
        ("Cello", 'Cello')
    )


class Lesson(models.Model):

	# lesson time
	# date and time is simply entered currently with no checks for double ups
	# fix this later!!!
    lesson_time = models.DateTimeField('Lesson Time') #Lesson Time

    # lesson duration
    # stored as CHAR as it takes far less room than INT and they are not used for arithmeic
    LESSON_DURATION_CHOICES = (
        ("30", '30 Minutes'),
        ("60", '1 Hour'),
        ("90", '1.5 Hours'),
        ("120", '2 Hours')
    )

    lesson_duration = models.CharField(
        max_length = 3,
        choices = LESSON_DURATION_CHOICES,
        default = "60"
    )

    # lesson location
    LESSON_LOCATION_CHOICES = (
        ("A0", 'Room A0'),
        ("A1", 'Room A1'),
        ("A2", 'Room A2'),
        ("A3", 'Room A3'),
        ("A4", 'Room A4')
    )

    lesson_location = models.CharField(
        max_length = 2,
        choices = LESSON_LOCATION_CHOICES,
        default = "A0"
    )

    feedback_student = models.CharField(max_length = 256)
    feedback_teacher = models.CharField(max_length = 256)

    #add foreign keys for teacher and student involved in lesson
    lesson_student = models.ForeignKey("accounts.User", limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, default=1, related_name = "student")
#
    lesson_teacher = models.ForeignKey("accounts.User", limit_choices_to={'groups__name': "Teacher"}, on_delete=models.CASCADE, default=1, related_name = "teacher")
    lesson_instrument = models.CharField(
        max_length = 20,
        choices = INST_CHOICES,
        default = "Guitar"
    )
class Inst(models.Model):


    due_back = models.DateTimeField('Due Back', null=True, blank=True) #Lesson Time




    instrument = models.CharField(
        max_length = 20,
        choices = INST_CHOICES,
        default = "1"
    )

    INST_COND_CHOICES = (
        ("Excellent", 'Excellent'),
        ("Great", 'Great'),
        ("Good", 'Good'),
        ("Poor", 'Poor'),
        ("Broken", 'Broken')
    )

    instrument_condition = models.CharField(
        max_length = 10,
        choices = INST_COND_CHOICES,
        default = "1"
    )

    #add foreign keys for teacher and student involved in lesson
    loan_student = models.ForeignKey("accounts.User", limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, default=1, related_name = "loan_student", null=True, blank=True)
#
    def get_absolute_url(self):
        return reverse('instrument:index')




