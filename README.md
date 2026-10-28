<div align="center">

# Exploitfa

**I build security and privacy tooling that is honest about what it does.**

Python · Qt/PySide6 · Windows internals · networking · developer tooling

[![GitHub followers](https://img.shields.io/github/followers/Largo-m?label=Followers&style=flat&color=2f81f7)](https://github.com/Largo-m?tab=followers)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-2f81f7)](https://github.com/sponsors/Largo-m)

</div>

---

## What I am working on

### [ExploitFA](https://github.com/Largo-m/ExploitFA) — a desktop VPN client you can read

An English-first, left-to-right **PySide6** client for Xray **VLESS** on Windows.
Real Qt interface, strict JSON configuration, checksum-verified builds, and a
demo mode that never pretends your traffic is protected.

[![ExploitFA stars](https://img.shields.io/github/stars/Largo-m/ExploitFA?style=flat&label=ExploitFA&color=63e6a5)](https://github.com/Largo-m/ExploitFA)
[![Release](https://img.shields.io/github/v/release/Largo-m/ExploitFA?sort=semver&label=release)](https://github.com/Largo-m/ExploitFA/releases)
[![CI](https://github.com/Largo-m/ExploitFA/actions/workflows/ci.yml/badge.svg)](https://github.com/Largo-m/ExploitFA/actions/workflows/ci.yml)

```text
Reality / TLS / plaintext  ·  TCP / WebSocket / gRPC
Live Xray core with SOCKS5 + HTTP inbounds
Hot-reloaded servers.json  ·  VLESS share-link import
92 tests  ·  CI on Ubuntu + Windows (Python 3.11-3.13)
```

### [vless-toolkit](https://github.com/Largo-m/vless-toolkit) — link tooling with zero dependencies

Parse, validate, build, convert and **redact** VLESS / VMess / Trojan /
Shadowsocks share links and base64 subscriptions. Pure standard library, no
network code, safe to run in CI.

[![vless-toolkit stars](https://img.shields.io/github/stars/Largo-m/vless-toolkit?style=flat&label=vless-toolkit&color=63e6a5)](https://github.com/Largo-m/vless-toolkit)
[![Release](https://img.shields.io/github/v/release/Largo-m/vless-toolkit?sort=semver&label=release)](https://github.com/Largo-m/vless-toolkit/releases)

```text
8 CLI commands  ·  subscription codecs  ·  semantic dedupe
country statistics  ·  ASCII QR  ·  207 tests
install: pip install vless-toolkit
```

---

## Featured projects

| Project | What it is | Stars |
| --- | --- | --- |
| [SecuSploitX](https://github.com/Largo-m/SecuSploitX) | All-in-one AI-powered security toolkit: web, network and phishing tests. Modular, Docker-ready, GUI + CLI. | ![stars](https://img.shields.io/github/stars/Largo-m/SecuSploitX?style=flat&color=2f81f7) |
| [GhostTrace](https://github.com/Largo-m/GhostTrace) | Multi-hop proxy-chain orchestration with validation, identity rotation and live monitoring. | ![stars](https://img.shields.io/github/stars/Largo-m/GhostTrace?style=flat&color=2f81f7) |
| [cyphisher](https://github.com/Largo-m/cyphisher) | Phishing simulation and awareness platform for authorised security training. | ![stars](https://img.shields.io/github/stars/Largo-m/cyphisher?style=flat&color=2f81f7) |
| [security-tools-hacking](https://github.com/Largo-m/security-tools-hacking) | Modular Windows penetration-testing framework. | ![stars](https://img.shields.io/github/stars/Largo-m/security-tools-hacking?style=flat&color=2f81f7) |
| [Ransomware-Analyzer](https://github.com/Largo-m/Ransomware-Analyzer) | Safe, controlled ransomware behaviour simulation for researchers. | ![stars](https://img.shields.io/github/stars/Largo-m/Ransomware-Analyzer?style=flat&color=2f81f7) |
| [AutoCaption](https://github.com/Largo-m/AutoCaption) | Fully automated, local-first video subtitle generation. | ![stars](https://img.shields.io/github/stars/Largo-m/AutoCaption?style=flat&color=2f81f7) |

---

## How I build

- **Honest interfaces.** If a feature does not exist, the README says so and the
  UI says so. No fake "connected" states, no implied protection.
- **Tests before features.** Validation, parsing and process supervision are pure
  functions with real test coverage — 92 tests in ExploitFA, 207 in
  vless-toolkit, running headless in CI on every push.
- **Small, boring dependencies.** Standard library first. When a dependency is
  unavoidable it is pinned, licensed and explained.
- **Reproducible builds.** Checksum manifests, `SHA256SUMS.txt` next to every
  artifact, and release workflows that build from a tag instead of a laptop.
- **Readable documentation.** Long READMEs with real screenshots and real command
  output, plus architecture notes that explain trade-offs instead of hiding them.

---

## Toolbox

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Qt](https://img.shields.io/badge/Qt%20%2F%20PySide6-41CD52?style=flat&logo=qt&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?style=flat&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-261230?style=flat&logo=ruff&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)

---

## GitHub

<!-- This line is intentional: it renders live counters without third-party services. -->

[![Followers](https://img.shields.io/github/followers/Largo-m?style=social)](https://github.com/Largo-m?tab=followers)
[![Stars given](https://img.shields.io/github/stars/Largo-m?style=social)](https://github.com/Largo-m?tab=stars)
[![Profile views](https://komarev.com/ghpvc/?username=Largo-m&color=2f81f7&style=flat)](https://github.com/Largo-m)

> Security tooling is for **authorised** testing only. Use it on systems you own
> or have explicit written permission to assess.

---

<div align="center">

**If something here saves you time, a star on the repo is the best thank-you.**

</div>
