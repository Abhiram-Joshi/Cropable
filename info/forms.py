from django.forms import ModelForm, DateTimeInput, TextInput, Textarea

from .models  import ReminderModel

class ReminderForm(ModelForm):
    class Meta:
        model = ReminderModel
        exclude = ["user"]
        widgets = {
            "datetime": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "id": "datetime",
                }
            ),
            "title": TextInput(
                attrs={
                    "id": "title",
                },
            ),
            "description": Textarea(
                attrs={
                    "id": "description",
                    "style": """margin-top: 5px;width: 100%; padding: 12px 20px;margin: 8px 0px 28px 0px;display: inline-block;
                        border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;"""
                },
            ),
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