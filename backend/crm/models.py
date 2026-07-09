from django.db import models
from django.core.validators import RegexValidator
from django_cryptography.fields import encrypt

COUNTRY_CODES = [
    ('+93', 'Afghanistan (+93)'), ('+355', 'Albania (+355)'), ('+213', 'Algeria (+213)'),
    ('+376', 'Andorra (+376)'), ('+244', 'Angola (+244)'), ('+54', 'Argentina (+54)'),
    ('+374', 'Armenia (+374)'), ('+61', 'Australia (+61)'), ('+43', 'Austria (+43)'),
    ('+994', 'Azerbaijan (+994)'), ('+973', 'Bahrain (+973)'), ('+880', 'Bangladesh (+880)'),
    ('+375', 'Belarus (+375)'), ('+32', 'Belgium (+32)'), ('+501', 'Belize (+501)'),
    ('+975', 'Bhutan (+975)'), ('+591', 'Bolivia (+591)'), ('+387', 'Bosnia and Herzegovina (+387)'),
    ('+267', 'Botswana (+267)'), ('+55', 'Brazil (+55)'), ('+673', 'Brunei (+673)'),
    ('+359', 'Bulgaria (+359)'), ('+855', 'Cambodia (+855)'), ('+237', 'Cameroon (+237)'),
    ('+1', 'Canada (+1)'), ('+56', 'Chile (+56)'), ('+86', 'China (+86)'),
    ('+57', 'Colombia (+57)'), ('+506', 'Costa Rica (+506)'), ('+385', 'Croatia (+385)'),
    ('+53', 'Cuba (+53)'), ('+357', 'Cyprus (+357)'), ('+420', 'Czech Republic (+420)'),
    ('+45', 'Denmark (+45)'), ('+20', 'Egypt (+20)'), ('+372', 'Estonia (+372)'),
    ('+251', 'Ethiopia (+251)'), ('+679', 'Fiji (+679)'), ('+358', 'Finland (+358)'),
    ('+33', 'France (+33)'), ('+995', 'Georgia (+995)'), ('+49', 'Germany (+49)'),
    ('+233', 'Ghana (+233)'), ('+30', 'Greece (+30)'), ('+502', 'Guatemala (+502)'),
    ('+852', 'Hong Kong (+852)'), ('+36', 'Hungary (+36)'), ('+354', 'Iceland (+354)'),
    ('+91', 'India (+91)'), ('+62', 'Indonesia (+62)'), ('+98', 'Iran (+98)'),
    ('+964', 'Iraq (+964)'), ('+353', 'Ireland (+353)'), ('+972', 'Israel (+972)'),
    ('+39', 'Italy (+39)'), ('+81', 'Japan (+81)'), ('+962', 'Jordan (+962)'),
    ('+7', 'Kazakhstan (+7)'), ('+254', 'Kenya (+254)'), ('+965', 'Kuwait (+965)'),
    ('+856', 'Laos (+856)'), ('+371', 'Latvia (+371)'), ('+961', 'Lebanon (+961)'),
    ('+218', 'Libya (+218)'), ('+423', 'Liechtenstein (+423)'), ('+370', 'Lithuania (+370)'),
    ('+352', 'Luxembourg (+352)'), ('+853', 'Macau (+853)'), ('+60', 'Malaysia (+60)'),
    ('+960', 'Maldives (+960)'), ('+356', 'Malta (+356)'), ('+52', 'Mexico (+52)'),
    ('+377', 'Monaco (+377)'), ('+976', 'Mongolia (+976)'), ('+382', 'Montenegro (+382)'),
    ('+212', 'Morocco (+212)'), ('+95', 'Myanmar (+95)'), ('+977', 'Nepal (+977)'),
    ('+31', 'Netherlands (+31)'), ('+64', 'New Zealand (+64)'), ('+234', 'Nigeria (+234)'),
    ('+47', 'Norway (+47)'), ('+968', 'Oman (+968)'), ('+92', 'Pakistan (+92)'),
    ('+507', 'Panama (+507)'), ('+595', 'Paraguay (+595)'), ('+51', 'Peru (+51)'),
    ('+63', 'Philippines (+63)'), ('+48', 'Poland (+48)'), ('+351', 'Portugal (+351)'),
    ('+974', 'Qatar (+974)'), ('+40', 'Romania (+40)'), ('+7', 'Russia (+7)'),
    ('+250', 'Rwanda (+250)'), ('+966', 'Saudi Arabia (+966)'), ('+381', 'Serbia (+381)'),
    ('+65', 'Singapore (+65)'), ('+421', 'Slovakia (+421)'), ('+386', 'Slovenia (+386)'),
    ('+27', 'South Africa (+27)'), ('+82', 'South Korea (+82)'), ('+34', 'Spain (+34)'),
    ('+94', 'Sri Lanka (+94)'), ('+249', 'Sudan (+249)'), ('+46', 'Sweden (+46)'),
    ('+41', 'Switzerland (+41)'), ('+886', 'Taiwan (+886)'), ('+255', 'Tanzania (+255)'),
    ('+66', 'Thailand (+66)'), ('+216', 'Tunisia (+216)'), ('+90', 'Turkey (+90)'),
    ('+256', 'Uganda (+256)'), ('+380', 'Ukraine (+380)'), ('+971', 'United Arab Emirates (+971)'),
    ('+44', 'United Kingdom (+44)'), ('+1', 'United States (+1)'), ('+598', 'Uruguay (+598)'),
    ('+998', 'Uzbekistan (+998)'), ('+58', 'Venezuela (+58)'), ('+84', 'Vietnam (+84)'),
    ('+967', 'Yemen (+967)'), ('+260', 'Zambia (+260)'), ('+263', 'Zimbabwe (+263)'),
]

NATIONALITIES = [
    ('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'),
    ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), ('Argentine', 'Argentine'),
    ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'),
    ('Azerbaijani', 'Azerbaijani'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'),
    ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'),
    ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'),
    ('Motswana', 'Motswana'), ('Brazilian', 'Brazilian'), ('Bruneian', 'Bruneian'),
    ('Bulgarian', 'Bulgarian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'),
    ('Canadian', 'Canadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'),
    ('Colombian', 'Colombian'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'),
    ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'),
    ('Danish', 'Danish'), ('Egyptian', 'Egyptian'), ('Estonian', 'Estonian'),
    ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), ('Finnish', 'Finnish'),
    ('French', 'French'), ('Georgian', 'Georgian'), ('German', 'German'),
    ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), ('Guatemalan', 'Guatemalan'),
    ('Hong Konger', 'Hong Konger'), ('Hungarian', 'Hungarian'), ('Icelandic', 'Icelandic'),
    ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'),
    ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'),
    ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'),
    ('Kazakhstani', 'Kazakhstani'), ('Kenyan', 'Kenyan'), ('Kuwaiti', 'Kuwaiti'),
    ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'),
    ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), ('Lithuanian', 'Lithuanian'),
    ('Luxembourgish', 'Luxembourgish'), ('Macanese', 'Macanese'), ('Malaysian', 'Malaysian'),
    ('Maldivian', 'Maldivian'), ('Maltese', 'Maltese'), ('Mexican', 'Mexican'),
    ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Montenegrin', 'Montenegrin'),
    ('Moroccan', 'Moroccan'), ('Burmese', 'Burmese'), ('Nepalese', 'Nepalese'),
    ('Dutch', 'Dutch'), ('New Zealander', 'New Zealander'), ('Nigerian', 'Nigerian'),
    ('Norwegian', 'Norwegian'), ('Omani', 'Omani'), ('Pakistani', 'Pakistani'),
    ('Panamanian', 'Panamanian'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'),
    ('Filipino', 'Filipino'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'),
    ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'),
    ('Rwandan', 'Rwandan'), ('Saudi Arabian', 'Saudi Arabian'), ('Serbian', 'Serbian'),
    ('Singaporean', 'Singaporean'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'),
    ('South African', 'South African'), ('South Korean', 'South Korean'), ('Spanish', 'Spanish'),
    ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Swedish', 'Swedish'),
    ('Swiss', 'Swiss'), ('Taiwanese', 'Taiwanese'), ('Tanzanian', 'Tanzanian'),
    ('Thai', 'Thai'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'),
    ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Emirati', 'Emirati'),
    ('British', 'British'), ('American', 'American'), ('Uruguayan', 'Uruguayan'),
    ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'),
    ('Yemeni', 'Yemeni'), ('Zambian', 'Zambian'), ('Zimbabwean', 'Zimbabwean'),
]

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Enter exactly 10 digits, without the country code (e.g. 0771234567 or 7712345678).'
)


class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100, choices=NATIONALITIES)
    passport_number = encrypt(models.CharField(max_length=50))

    emergency_contact_name = models.CharField(max_length=200, blank=True)
    emergency_contact_country_code = models.CharField(
        max_length=5, choices=COUNTRY_CODES, blank=True, default='+94'
    )
    emergency_contact_phone = models.CharField(
        max_length=10, blank=True, validators=[phone_validator]
    )
    emergency_contact_relationship = models.CharField(max_length=100, blank=True)

    notes = models.TextField(blank=True, help_text="Any additional details about this tourist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.nationality})"

    class Meta:
        ordering = ['-created_at']