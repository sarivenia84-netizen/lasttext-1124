from pathlib import Path

# Joke: the phone's shutdown accidentally gives the user's ex the closure they wanted.
message = '1%: I turned off your location sharing to save power. Your ex just texted, “why did the blue dot stop?” I’m dying; at least one of us finally got closure.'
Path('/output').mkdir(parents=True, exist_ok=True)
Path('/output/entry.txt').write_text(message, encoding='utf-8')
