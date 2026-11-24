from pathlib import Path

message = '1%. Pesan terakhir: aku memindahkan 47 foto blur ke folder “Kenangan”. Ternyata semuanya screenshot tiket konser yang tak pernah kamu beli. Aku ikut malu, jadi aku padam duluan.'
Path('/output').mkdir(parents=True, exist_ok=True)
Path('/output/entry.txt').write_text(message, encoding='utf-8')
