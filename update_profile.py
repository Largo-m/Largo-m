from pathlib import Path

path = Path("README.md")
text = path.read_text(encoding="utf-8")
replacements = [
    ("`vless-toolkit` — link tooling with zero dependencies", "`vless-toolkit` — link tooling with zero dependencies"),
    ("Parse, validate, build, convert and **redact** VLESS", "Parse, validate, build, convert, **sort** and **redact** VLESS"),
    ("```console\n$ vless-toolkit summary links.txt", "```console\n$ vless-toolkit sort --by country links.txt\nvless://11111111-1111-4111-8111-111111111111@de.example.com:443?security=tls#Germany%20Frankfurt\ntrojan://secret-password@jp.example.com:443?security=tls#Japan%20Tokyo\n\n$ vless-toolkit summary links.txt"),
    ("101 tests in ExploitFA, 207 in vless-toolkit", "108 tests in ExploitFA, 214 in vless-toolkit"),
    ("<td align=\"center\"><b>101</b><br><sub>tests · ExploitFA</sub></td>", "<td align=\"center\"><b>108</b><br><sub>tests · ExploitFA</sub></td>"),
    ("<td align=\"center\"><b>207</b><br><sub>tests · vless-toolkit</sub></td>", "<td align=\"center\"><b>214</b><br><sub>tests · vless-toolkit</sub></td>"),
]
missing = [old for old, _ in replacements if old not in text]
if missing:
    raise SystemExit(f"missing anchors: {missing}")
for old, new in replacements:
    text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8", newline="\n")
print("profile README updated")
