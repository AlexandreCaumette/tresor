import pathlib

import segno

for puzzle_id in range(1, 10):
    qrcode = segno.make_qr(content=puzzle_id)

    qrcode_path = (
        pathlib.Path("src") / "assets" / "qrcodes" / f"qr_code_{puzzle_id}.png"
    )

    qrcode.save(out=str(qrcode_path.resolve()), scale=10, border=2)
