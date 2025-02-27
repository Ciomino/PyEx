def modificaStringa(testo: str):
    return testo.strip().lower().replace(" ","_")

test = "  hello, ciaoei, dfnjdsf    "
print(modificaStringa(test))