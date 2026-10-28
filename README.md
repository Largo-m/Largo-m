<div align="center">
  <img src="assets/banner.png" alt="Largo-m — security and privacy tooling with honest interfaces" width="100%" />
</div>

<h3 align="center">Security and privacy tooling that is honest about what it does</h3>

<p align="center">
  <b>Python</b> · <b>Qt / PySide6</b> · <b>Windows internals</b> · <b>networking</b> · <b>developer tooling</b>
</p>

<p align="center">
  <a href="https://github.com/Largo-m?tab=followers"><img alt="GitHub followers" src="https://img.shields.io/github/followers/Largo-m?label=Followers&style=for-the-badge&labelColor=0d1117&color=38bdf8"></a>
  <a href="https://github.com/Largo-m?tab=repositories"><img alt="Public repositories" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FLargo-m&query=public_repos&label=Repositories&style=for-the-badge&labelColor=0d1117&color=63e6a5"></a>
  <a href="https://github.com/sponsors/Largo-m"><img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?style=for-the-badge&labelColor=0d1117"></a>
</p>

---

## ⚡ What I am building

<table>
<tr>
<td width="55%" valign="top">

### [ExploitFA](https://github.com/Largo-m/ExploitFA)

An English-first, left-to-right **PySide6** desktop client for Xray **VLESS** on
Windows. A real Qt interface, strict JSON configuration, checksum-verified
builds, and a demo mode that never pretends your traffic is protected.

`Reality` · `TLS` · `TCP` · `WebSocket` · `gRPC` · live core · SOCKS5 + HTTP

<a href="https://github.com/Largo-m/ExploitFA/stargazers"><img alt="ExploitFA stars" src="https://img.shields.io/github/stars/Largo-m/ExploitFA?style=flat-square&labelColor=0d1117&color=38bdf8"></a>
<a href="https://github.com/Largo-m/ExploitFA/releases/latest"><img alt="ExploitFA release" src="https://img.shields.io/github/v/release/Largo-m/ExploitFA?style=flat-square&labelColor=0d1117&color=63e6a5"></a>
<a href="https://github.com/Largo-m/ExploitFA/actions/workflows/ci.yml"><img alt="ExploitFA CI" src="https://github.com/Largo-m/ExploitFA/actions/workflows/ci.yml/badge.svg"></a>

</td>
<td width="45%" valign="top">

<a href="https://github.com/Largo-m/ExploitFA"><img src="https://raw.githubusercontent.com/Largo-m/ExploitFA/main/docs/screenshots/dashboard-dark.png" alt="ExploitFA dashboard" width="100%" /></a>

</td>
</tr>
</table>

<table>
<tr>
<td width="50%" valign="top">

### [vless-toolkit](https://github.com/Largo-m/vless-toolkit)

Parse, validate, build, convert, **sort** and **redact** VLESS / VMess / Trojan /
Shadowsocks share links and base64 subscriptions. Pure standard library, no
network code, safe to drop into CI.

```console
$ vless-toolkit summary links.txt
total: 4  unique hosts: 4
by protocol:
  vless: 1  vmess: 1
  trojan: 1  shadowsocks: 1
by country:
  DE: 1  NL: 1  JP: 1  SG: 1
```

<a href="https://github.com/Largo-m/vless-toolkit/stargazers"><img alt="vless-toolkit stars" src="https://img.shields.io/github/stars/Largo-m/vless-toolkit?style=flat-square&labelColor=0d1117&color=38bdf8"></a>
<a href="https://github.com/Largo-m/vless-toolkit/releases/latest"><img alt="vless-toolkit release" src="https://img.shields.io/github/v/release/Largo-m/vless-toolkit?sort=semver&style=flat-square&labelColor=0d1117&color=63e6a5"></a>

</td>
<td width="50%" valign="top">

### [SecuSploitX](https://github.com/Largo-m/SecuSploitX)

All-in-one AI-powered security toolkit: web, network and phishing tests with a
modular CLI and GUI.

<a href="https://github.com/Largo-m/SecuSploitX/stargazers"><img alt="SecuSploitX stars" src="https://img.shields.io/github/stars/Largo-m/SecuSploitX?style=flat-square&labelColor=0d1117&color=f59e0b"></a>

### Also on GitHub

[GhostTrace](https://github.com/Largo-m/GhostTrace) — multi-hop proxy chains ·
[cyphisher](https://github.com/Largo-m/cyphisher) — authorised phishing simulation ·
[Ransomware-Analyzer](https://github.com/Largo-m/Ransomware-Analyzer) — safe behaviour simulation ·
[AutoCaption](https://github.com/Largo-m/AutoCaption) — local-first subtitles

</td>
</tr>
</table>

---

## 🧭 How I build

| Principle | What it means in practice |
| :-- | :-- |
| **Honest interfaces** | If a feature does not exist, the README says so and the UI says so. No fake "connected" states, no implied protection. |
| **Tests before features** | Validation, parsing and process supervision are pure functions with real coverage — 122 tests in ExploitFA, 214 in vless-toolkit, headless in CI. |
| **Small, boring dependencies** | Standard library first. Every unavoidable dependency is pinned, licensed and explained. |
| **Reproducible builds** | Checksums for core binaries, `SHA256SUMS.txt` next to every artifact, releases built by a workflow from a tag. |
| **Documentation as a feature** | Long READMEs with real screenshots and real command output, architecture notes that explain trade-offs, and tests that fail when a link breaks. |

---

## 📈 By the numbers

<table>
<tr>
<td align="center"><b>122</b><br><sub>tests · ExploitFA</sub></td>
<td align="center"><b>214</b><br><sub>tests · vless-toolkit</sub></td>
<td align="center"><b>34</b><br><sub>merged pull requests</sub></td>
<td align="center"><b>3</b><br><sub>CI jobs · every PR</sub></td>
<td align="center"><b>0</b><br><sub>telemetry endpoints</sub></td>
</tr>
</table>

---

## 🧰 Toolbox

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Qt" src="https://img.shields.io/badge/Qt%20%2F%20PySide6-41CD52?style=flat-square&logo=qt&logoColor=white">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white">
  <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
  <img alt="PowerShell" src="https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white">
  <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img alt="Ruff" src="https://img.shields.io/badge/Ruff-261230?style=flat-square&logo=ruff&logoColor=white">
  <img alt="pytest" src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white">
  <img alt="PyInstaller" src="https://img.shields.io/badge/PyInstaller-FFD43B?style=flat-square&logo=python&logoColor=black">
</p>

---

## 🏆 Achievements

<p>
  <a href="https://github.com/Largo-m?tab=achievements"><img alt="Starstruck" src="https://img.shields.io/badge/Starstruck-16%2B_stars-ea4aaa?style=flat-square&labelColor=0d1117"></a>
  <a href="https://github.com/Largo-m?tab=achievements"><img alt="Quickdraw" src="https://img.shields.io/badge/Quickdraw-closed_within_5_minutes-63e6a5?style=flat-square&labelColor=0d1117"></a>
  <a href="https://github.com/Largo-m?tab=achievements"><img alt="YOLO" src="https://img.shields.io/badge/YOLO-merged_without_review-f59e0b?style=flat-square&labelColor=0d1117"></a>
</p>

<sub>Next up: Pull Shark (merged pull requests) and Pair Extraordinaire (co-authored commits).</sub>

---

## 📫 Reach me

- **GitHub:** [@Largo-m](https://github.com/Largo-m)
- **Work with me:** open an issue or a [discussion](https://github.com/Largo-m/ExploitFA/discussions) on any project
- **Support:** [GitHub Sponsors](https://github.com/sponsors/Largo-m) · a ⭐ on a repository you use is just as welcome

<div align="center">
  <sub>Security tooling is for <b>authorised</b> testing only. Use it on systems you own or have explicit written permission to assess.</sub>
</div>
