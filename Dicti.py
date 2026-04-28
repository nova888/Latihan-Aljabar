pengguna = {"nama": "Ani", "email": "ani@example.com"}
template_email = "Kepada {nama},\n\nTerima kasih telah mendaftar.\n\nSalam,\nTim Kami"

isi_email = template_email.format(**pengguna)
print(isi_email)
