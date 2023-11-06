temp = float(input('Ange temperaturen utomhus i Celsius: '))
if temp < 0:
    print('Det är jättekalt ute!')
elif 0 <= temp <= 10:
    print('Det är rätt så kallt ute!')
elif 10 < temp <= 20:
    print('Vi kankse överlever!')
else:
    print('Nästan som att vi kan ju tro att det är sommar!')