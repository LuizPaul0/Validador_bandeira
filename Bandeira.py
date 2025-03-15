def get_card_brand(card_number):
    card_number = str(card_number)
    length = len(card_number)

    if length == 16 and (card_number.startswith('51') or card_number.startswith('52') or 
                         card_number.startswith('53') or card_number.startswith('54') or 
                         card_number.startswith('55') or 222100 <= int(card_number[:6]) <= 272099):
        return "Mastercard"
    elif (length == 13 or length == 16 or length == 19) and card_number.startswith('4'):
        return "Visa"
    elif length == 15 and (card_number.startswith('34') or card_number.startswith('37')):
        return "American Express (Amex)"
    elif length == 14 and (300000 <= int(card_number[:6]) <= 305999 or 
                           card_number.startswith('36') or card_number.startswith('38')):
        return "Diners Club"
    elif length == 16 and (card_number.startswith('6011') or 
                           622126 <= int(card_number[:6]) <= 622925 or 
                           644000 <= int(card_number[:6]) <= 649999 or 
                           card_number.startswith('65')):
        return "Discover"
    elif length == 15 and (card_number.startswith('2014') or card_number.startswith('2149')):
        return "EnRoute"
    elif length == 16 and (352800 <= int(card_number[:6]) <= 359999):
        return "JCB"
    elif length == 15 and card_number.startswith('8699'):
        return "Voyager"
    elif (length == 13 or length == 16 or length == 19) and (card_number.startswith('606282') or card_number.startswith('3841')):
        return "Hipercard"
    elif length == 16 and card_number.startswith('50'):
        return "Aura"
    else:
        return "Unknown"

# Exemplo de uso
card_number = "5066135578604088"
print(f"A bandeira do cartão é: {get_card_brand(card_number)}")
