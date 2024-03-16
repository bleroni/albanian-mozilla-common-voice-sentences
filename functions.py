def fix_split_word(input_text, output_text):
    pairs = [
        (" aditur", "paditur"),
        (" jyk at", "gjyk at"),
        (' randaj', 'prandaj'),
        (' DPZ', ''),
        (' SHPK',''),
        (' TVSH', ''),
    ]
    return "split word"


def fix_abbreviations(input_text, output_text):
    # AKP
    pairs = [
        ("AKP", "Agjencia Kosovare e Privatizimit"),
    ]
    pass


def fix_abbreviations_reges(input_text, output_text):
    # AKP
    pairs = [
        ("AKP", "Agjencia Kosovare e Privatizimit"),
    ]
    pass