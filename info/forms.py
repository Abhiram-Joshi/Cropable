from django.forms import ModelForm, DateTimeInput

from .models  import ReminderModel

class ReminderForm(ModelForm):
    class Meta:
        model = ReminderModel
        exclude = ["user"]
        widgets = {
            "datetime": DateTimeInput(attrs={"type": "datetime-local"}),
        }

# class ReminderForm(ModelForm):
#     class Meta:
#         model = ReminderModel
#         # fields = ("crop", "min_price", "stock", "place", "description", "photo")
#         # fields = ("photo", )
#         # exclude = ("user", "highest_bid")
#         exclude = ["user"]

#         labels = {
#             # "crop": "",
#             # "place": "",
#             # "min_price": "",
#             # "description": "",
#             # "photo": "",
#             # "stock": "",
#         }

#         # widgets = {
#         #     "photo": forms.FileInput(
#         #         attrs = {
#         #             "class": "upload",
#         #             "name": "image",
#         #         }
#         #     )
#         # }