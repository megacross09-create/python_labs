pr, disc, vat = float(input('price (₽): ')), float(input('discount (%): ')), float(input('vat (%): '))
base = pr * (1-disc/100)
vat_am = base * (vat/100)
tot = base + vat_am
print(f'База после скидки: {(base):.2f} ₽\n'
      f'НДС:               {(vat_am):.2f} ₽\n'
      f'Итого к оплате:    {(tot):.2f} ₽')