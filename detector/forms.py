from django import forms

from .models import Crop

class CropAddForm(forms.ModelForm):
    class Meta:
        model = Crop
        # fields = ("crop", "min_price", "stock", "place", "description", "photo")
        fields = ("photo", )
        # exclude = ("user", "highest_bid")

        labels = {
            # "crop": "",
            # "place": "",
            # "min_price": "",
            # "description": "",
            "photo": "",
            # "stock": "",
        }

        widgets = {
            "photo": forms.FileInput(
                attrs = {
                    "class": "upload",
                    "name": "image",
                }
            )
        }

        # widgets = {
        #     "crop": forms.TextInput(
        #         attrs={
        #             "class": "form-control part1",
        #             "placeholder": "Crop Name",
        #         }
        #     ),
        #     "place": forms.TextInput(
        #         attrs={
        #             "class": "form-control place3",
        #             "placeholder": "Address",
        #         }
        #     ),
        #     "min_price": forms.NumberInput(
        #         attrs={
        #             "class": "form-control place2 part2",
        #             "placeholder": "Base price",
        #         }
        #     ),
        #     "description": forms.Textarea(
        #         attrs={
        #             "class": "form-control place2 part2",
        #             "placeholder": "Description",
        #         }
        #     ),
        #     "stock": forms.NumberInput(
        #         attrs={
        #             "class": "form-control place2 part3",
        #             "placeholder": "Stock",
        #         }
        #     ),
        # }