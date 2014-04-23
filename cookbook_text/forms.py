from django import forms


class BootstrapFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(BootstrapFormMixin, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs.update({
                'class': 'form-control'
            })


class Recipe01Form(BootstrapFormMixin, forms.Form):
    METHODS = (
        ('A', 'List Comprehension'),
        ('B', 'Map Built-In Function'),
    )

    string = forms.CharField(max_length=100)
    method = forms.ChoiceField(choices=METHODS)