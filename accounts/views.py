from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django import forms
from .models import User, SavedCard


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class RegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html", {"form": RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, "accounts/register.html", {"form": form})


class TopUpForm(forms.Form):
    amount = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2)
    # Card entry fields (stub, not processed for real payments)
    card_number = forms.CharField(max_length=19, required=False)
    cardholder_name = forms.CharField(max_length=100, required=False)
    exp_month = forms.IntegerField(min_value=1, max_value=12, required=False)
    exp_year = forms.IntegerField(min_value=2024, max_value=2100, required=False)
    cvv = forms.CharField(max_length=4, required=False)
    save_card = forms.BooleanField(required=False)
    use_saved_card = forms.ModelChoiceField(queryset=SavedCard.objects.none(), required=False, empty_label='Не использовать сохраненную карту')

    def __init__(self, *args, **kwargs):
        user: User | None = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['use_saved_card'].queryset = SavedCard.objects.filter(user=user)


@login_required
def top_up(request):
    if request.method == "POST":
        form = TopUpForm(request.POST, user=request.user)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            saved_card: SavedCard | None = form.cleaned_data.get("use_saved_card")
            save_new = form.cleaned_data.get("save_card")

            # Validate card presence: either saved card or entered fields
            if not saved_card and not form.cleaned_data.get('card_number'):
                form.add_error('card_number', 'Введите данные карты или выберите сохраненную')
            else:
                # Fake charge success; optionally save new card as stub
                if not saved_card and save_new:
                    number = form.cleaned_data.get('card_number', '')
                    last4 = number.replace(' ', '').replace('-', '')[-4:] if number else '0000'
                    SavedCard.objects.create(
                        user=request.user,
                        brand='VISA' if number.startswith('4') else 'Card',
                        last4=last4,
                        exp_month=form.cleaned_data.get('exp_month') or 1,
                        exp_year=form.cleaned_data.get('exp_year') or 2030,
                        cardholder_name=form.cleaned_data.get('cardholder_name', ''),
                        is_default=False,
                    )

                request.user.balance = (request.user.balance or 0) + amount
                request.user.save(update_fields=["balance"])
                return redirect("home")
    else:
        form = TopUpForm(user=request.user)
    return render(request, "accounts/top_up.html", {"form": form})

# Create your views here.
