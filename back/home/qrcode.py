from django.utils.timezone import now
from qrcodegen import *


def to_svg_str(qr, border):
    parts = []
    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                parts.append("M{},{}h1v1h-1z".format(x + border, y + border))
    svg = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {0} {0}" stroke="none"><rect width="100%" height="100%" fill="#FFFFFF"/><path d="{1}" fill="#000000"/></svg>'
    return svg.format(qr.get_size() + border * 2, " ".join(parts))


# https://www.upn-qr.si/uploads/files/NavodilaZaProgramerjeUPNQR.pdf


def generate_upn_qr(
    name, address1, address2, iban, reference, purpose, amount, date=now()
):
    name = name.strip()[:33]
    address1 = address1.strip()[:33]
    address2 = address2.strip()[:33]
    iban = iban.replace(" ", "")
    reference = reference.replace(" ", "")
    purpose = purpose.strip()[:42]
    amount = str(int(amount * 100)).zfill(11)
    date = date.strftime("%d.%m.%Y")

    lines = [
        "UPNQR",  # Vodilni slog
        "",  # IBAN plačnika
        "",  # Polog
        "",  # Dvig
        "",  # Referenca plačnika
        "",  # Ime plačnika
        "",  # Ulica in št. plačnika
        "",  # Kraj plačnika
        amount,  # Znesek
        "",  # Datum plačila
        "",  # Nujno
        "CHAR",  # Koda namena
        purpose,  # Namen plačila
        date,  # Rok plačila
        iban,  # IBAN prejemnika
        reference,  # Referenca prejemnika
        name,  # Ime prejemnika
        address1,  # Ulica in št. prejemnika
        address2,  # Kraj prejemnika
    ]

    print(lines)

    encoded_text = ("\n".join(lines) + "\n").encode("iso-8859-2", errors="ignore")
    encoded_length = str(len(encoded_text)).zfill(3)
    encoded_text += (encoded_length + "\n").encode("iso-8859-2", errors="ignore")

    eci_segment = QrSegment.make_eci(4)  # eci 4 = ISO-8859-2
    text_segment = QrSegment.make_bytes(encoded_text)

    qr_code = QrCode.encode_segments(
        [eci_segment, text_segment], QrCode.Ecc.MEDIUM, 15, 15, 2, False
    )

    return to_svg_str(qr_code, 2)
