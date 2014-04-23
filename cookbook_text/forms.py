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


class Recipe02Form(BootstrapFormMixin, forms.Form):
    CONVERSION_METHODS = (
        ('A', 'Characters to Numeric Codes'),
        ('B', 'Numeric Codes to Characters'),
    )

    ENCODING_METHODS = (
        ('I', 'ASCII (ISO)'),
        ('U', 'Unicode')
    )

    sequence = forms.CharField(max_length=100)
    conversion_method = forms.ChoiceField(choices=CONVERSION_METHODS)
    encoding_method = forms.ChoiceField(choices=ENCODING_METHODS)