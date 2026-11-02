🛡️ Largo-m — Security & Privacy Tooling with Honest Interfaces
<div align="center"><img src="assets/banner.png" alt="Largo-m — security and privacy tooling with honest interfaces" width="100%" />
Security and privacy tooling that is honest about what it does
Python · Qt / PySide6 · Windows internals · networking · developer tooling · threat modeling · reproducible builds · CI/CD


<a href="https://github.com/Largo-m?tab=followers"> <img alt="GitHub followers" src="https://img.shields.io/github/followers/Largo-m?label=Followers&style=for-the-badge&labelColor=0d1117&color=38bdf8"> </a> <a href="https://github.com/Largo-m?tab=repositories"> <img alt="Public repositories" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2FLargo-m&query=public_repos&label=Repositories&style=for-the-badge&labelColor=0d1117&color=63e6a5"> </a> <a href="https://github.com/sponsors/Largo-m"> <img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?style=for-the-badge&labelColor=0d1117"> </a> <a href="https://github.com/Largo-m?tab=achievements"> <img alt="Achievements" src="https://img.shields.io/badge/Achievements-4%20earned-f59e0b?style=for-the-badge&labelColor=0d1117"> </a></div>
📖 دربارهٔ من — About Me
<div dir="rtl">
من Largo-m هستم؛ توسعه‌دهنده‌ای که روی مرز میان امنیت، حریم خصوصی و تجربهٔ کاربری صادقانه کار می‌کند. باور دارم ابزار امنیتی باید همان‌قدر که در برابر مهاجم مقاوم است، در برابر توهم امنیت هم مقاوم باشد. اگر برنامه‌ای می‌گوید «متصل هستی» ولی در واقع ترافیک تو محافظت نمی‌شود، آن برنامه نه ابزار امنیتی است و نه حتی ابزار — یک دروغ رابط کاربری است.

</div>
I am Largo-m — a developer working at the intersection of security, privacy, and honest user experience. I believe a security tool must be as resistant to false senses of safety as it is to actual adversaries. If an application says "you are connected" while your traffic is unprotected, it is neither a security tool nor a tool at all — it is a UI lie.

My work spans desktop clients for proxy protocols, pure-standard-library parsers for share links and subscriptions, safe behaviour simulators for malware analysis, authorised phishing simulation platforms, and local-first developer tooling. Every project follows the same philosophy:

If it does not exist, the README says so, and the UI says so.

⚡ What I Am Building — Projects
🚀 ExploitFA — A PySide6 desktop client for Xray VLESS
<div align="center"><a href="https://github.com/Largo-m/ExploitFA"> <img src="https://raw.githubusercontent.com/Largo-m/ExploitFA/main/docs/screenshots/dashboard-dark.png" alt="ExploitFA dashboard" width="90%" /> </a>



<a href="https://github.com/Largo-m/ExploitFA/stargazers"> <img alt="ExploitFA stars" src="https://img.shields.io/github/stars/Largo-m/ExploitFA?style=flat-square&labelColor=0d1117&color=38bdf8"> </a> <a href="https://github.com/Largo-m/ExploitFA/releases/latest"> <img alt="ExploitFA release" src="https://img.shields.io/github/v/release/Largo-m/ExploitFA?style=flat-square&labelColor=0d1117&color=63e6a5"> </a> <a href="https://github.com/Largo-m/ExploitFA/actions/workflows/ci.yml"> <img alt="ExploitFA CI" src="https://github.com/Largo-m/ExploitFA/actions/workflows/ci.yml/badge.svg"> </a> <a href="https://github.com/Largo-m/ExploitFA/blob/main/LICENSE"> <img alt="ExploitFA license" src="https://img.shields.io/github/license/Largo-m/ExploitFA?style=flat-square&labelColor=0d1117&color=f59e0b"> </a></div>
An English-first, left-to-right PySide6 desktop client for Xray VLESS on Windows. This is not a wrapper around a CLI — it is a real Qt interface with strict JSON configuration, checksum-verified builds, live core supervision, and a demo mode that never pretends your traffic is protected.

Supported transports and security layers:

Layer	Options
Security	Reality · TLS
Transport	TCP · WebSocket · gRPC
Core	Live Xray core with process supervision
Local proxy	SOCKS5 + HTTP
Configuration	Strict JSON schema, validated before launch
Key engineering decisions:

✅ 122 tests covering validation, parsing, process supervision, and UI state machines — all run headless in CI

✅ Checksum-verified core binaries — every release ships with SHA256SUMS.txt

✅ Reproducible builds — releases are built by a workflow from a git tag, never from a developer's machine

✅ Demo mode — a first-class feature that explicitly tells the user "no traffic is being protected" so nobody mistakes a screenshot for a guarantee

✅ No telemetry endpoints — zero phone-home behaviour, verifiable in the source

🧰 vless-toolkit — Parse, validate, build, convert, sort and redact share links
<div align="center"><a href="https://github.com/Largo-m/vless-toolkit/stargazers"> <img alt="vless-toolkit stars" src="https://img.shields.io/github/stars/Largo-m/vless-toolkit?style=flat-square&labelColor=0d1117&color=38bdf8"> </a> <a href="https://github.com/Largo-m/vless-toolkit/releases/latest"> <img alt="vless-toolkit release" src="https://img.shields.io/github/v/release/Largo-m/vless-toolkit?sort=semver&style=flat-square&labelColor=0d1117&color=63e6a5"> </a> <a href="https://github.com/Largo-m/vless-toolkit/actions/workflows/ci.yml"> <img alt="vless-toolkit CI" src="https://github.com/Largo-m/vless-toolkit/actions/workflows/ci.yml/badge.svg"> </a></div>
A pure standard library toolkit that parses, validates, builds, converts, sorts, and redacts VLESS / VMess / Trojan / Shadowsocks share links and base64 subscriptions. No network code. No third-party dependencies. Safe to drop into any CI pipeline without supply-chain anxiety.

console
$ vless-toolkit summary links.txt
total: 4  unique hosts: 4
by protocol:
  vless: 1  vmess: 1
  trojan: 1  shadowsocks: 1
by country:
  DE: 1  NL: 1  JP: 1  SG: 1
What it does:

🔍 Parse share links and base64-encoded subscription blobs

✅ Validate scheme, credentials, transport parameters, and port ranges

🏗️ Build canonical share links from structured data

🔄 Convert between protocols and between link / subscription formats

📊 Sort entries by protocol, country, latency hint, or custom keys

🕵️ Redact sensitive fields for safe sharing in issues and screenshots

🧪 214 tests — headless, hermetic, and run on every PR

🛡️ SecuSploitX — All-in-one AI-powered security toolkit
<div align="center"><a href="https://github.com/Largo-m/SecuSploitX/stargazers"> <img alt="SecuSploitX stars" src="https://img.shields.io/github/stars/Largo-m/SecuSploitX?style=flat-square&labelColor=0d1117&color=f59e0b"> </a> <a href="https://github.com/Largo-m/SecuSploitX/releases/latest"> <img alt="SecuSploitX release" src="https://img.shields.io/github/v/release/Largo-m/SecuSploitX?style=flat-square&labelColor=0d1117&color=63e6a5"> </a></div>
An all-in-one, AI-assisted security toolkit covering web, network, and phishing testing with a modular CLI and GUI. Designed for authorised assessments only, with clear scope prompts and audit logging.

🌐 Web testing — endpoint discovery, header analysis, misconfiguration checks

📡 Network testing — port and service enumeration with safe defaults

🎣 Phishing simulation — authorised campaigns with consent tracking

🧩 Modular architecture — every module is independently loadable and testable

🖥️ Dual interface — CLI for automation, GUI for guided assessments

👻 GhostTrace — Multi-hop proxy chains
Chain multiple proxies into a single controlled route with explicit hop accounting, failure isolation, and honest reporting of what each hop actually guarantees. Built for researchers who need reproducible routing, not magic.

🔗 Multi-hop chaining — SOCKS5 / HTTP proxies with per-hop validation

🧾 Hop accounting — every hop is logged, timed, and health-checked

🛑 Failure isolation — a dead hop never silently degrades to direct connection

📊 Reproducible routes — exportable chain definitions for repeatable tests

🎣 cyphisher — Authorised phishing simulation
A phishing simulation platform built for authorised red-team exercises and security-awareness programs. Consent-first design: no target is contacted without an explicit, logged authorisation record.

📝 Authorisation records — every campaign is tied to a signed scope

📬 Template engine — realistic, localisable simulation emails

📈 Awareness metrics — report click rates without collecting unnecessary PII

🔒 Local-first — campaign data stays on your infrastructure

🧪 Ransomware-Analyzer — Safe behaviour simulation
A safe behaviour simulator for understanding ransomware-like file operations without ever encrypting real user data. Everything runs inside a sandboxed, disposable workspace with explicit guard rails.

🧱 Sandboxed workspace — no writes outside the designated directory

📋 Behaviour traces — file operations, renames, and deletions are logged

🛡️ Hard guard rails — the simulator refuses to run outside a disposable root

📚 Educational output — traces are explained, not just dumped

🎬 AutoCaption — Local-first subtitles
A local-first subtitle generator: your media never leaves your machine. Built for people who want captions without uploading personal videos to a third-party service.

🏠 Local-first — no uploads, no cloud dependency

🎞️ Batch processing — queue multiple files with consistent settings

🌍 Multi-language output — configurable target languages

🔇 Offline capable — runs without a network connection once models are present

🧭 How I Build — Engineering Principles
Principle	What it means in practice
Honest interfaces	If a feature does not exist, the README says so and the UI says so. No fake "connected" states, no implied protection. Demo modes are labelled as demo modes.
Tests before features	Validation, parsing, and process supervision are pure functions with real coverage — 122 tests in ExploitFA, 214 in vless-toolkit, all headless in CI. A feature without a test is a rumour.
Small, boring dependencies	Standard library first. Every unavoidable dependency is pinned, licensed, and explained in the README. No dependency is added "just in case".
Reproducible builds	Checksums for core binaries, SHA256SUMS.txt next to every artifact, releases built by a workflow from a tag — never from a developer's laptop.
Documentation as a feature	Long READMEs with real screenshots and real command output, architecture notes that explain trade-offs, and tests that fail when a documentation link breaks.
Privacy by default	Zero telemetry endpoints. No analytics SDKs. No "anonymous usage statistics". If a project needs data, it asks first and stores it locally.
Authorised use only	Security tooling is for authorised testing only. Every repository states this clearly, and simulation tools include guard rails that refuse to run outside an authorised scope.
📈 By the Numbers
<div align="center"><table> <tr> <td align="center"><b>122</b><br><sub>tests · ExploitFA</sub></td> <td align="center"><b>214</b><br><sub>tests · vless-toolkit</sub></td> <td align="center"><b>34</b><br><sub>merged pull requests</sub></td> <td align="center"><b>3</b><br><sub>CI jobs · every PR</sub></td> <td align="center"><b>0</b><br><sub>telemetry endpoints</sub></td> <td align="center"><b>7</b><br><sub>public repositories</sub></td> </tr> </table></div>
🧰 Toolbox — Languages, Frameworks & Tools
<div align="center"><p> <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="Qt" src="https://img.shields.io/badge/Qt%20%2F%20PySide6-41CD52?style=flat-square&logo=qt&logoColor=white"> <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white"> <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"> <img alt="PowerShell" src="https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white"> <img alt="Bash" src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white"> <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white"> <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"> <img alt="Ruff" src="https://img.shields.io/badge/Ruff-261230?style=flat-square&logo=ruff&logoColor=white"> <img alt="pytest" src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"> <img alt="PyInstaller" src="https://img.shields.io/badge/PyInstaller-FFD43B?style=flat-square&logo=python&logoColor=black"> <img alt="JSON" src="https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white"> <img alt="YAML" src="https://img.shields.io/badge/YAML-CB171E?style=flat-square&logo=yaml&logoColor=white"> <img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"> </p></div>
🏆 Achievements
<div align="center"><p> <a href="https://github.com/Largo-m?tab=achievements"> <img alt="Starstruck" src="https://img.shields.io/badge/Starstruck-16%2B_stars-ea4aaa?style=flat-square&labelColor=0d1117"> </a> <a href="https://github.com/Largo-m?tab=achievements"> <img alt="Quickdraw" src="https://img.shields.io/badge/Quickdraw-closed_within_5_minutes-63e6a5?style=flat-square&labelColor=0d1117"> </a> <a href="https://github.com/Largo-m?tab=achievements"> <img alt="YOLO" src="https://img.shields.io/badge/YOLO-merged_without_review-f59e0b?style=flat-square&labelColor=0d1117"> </a> <a href="https://github.com/Largo-m?tab=achievements"> <img alt="Pull Shark" src="https://img.shields.io/badge/Pull_Shark-in_progress-38bdf8?style=flat-square&labelColor=0d1117"> </a> </p>
<sub>Next up: <b>Pull Shark</b> (merged pull requests) and <b>Pair Extraordinaire</b> (co-authored commits).</sub>

</div>
🗺️ Roadmap — What Comes Next
<div dir="rtl">
افق	تمرکز
کوتاه‌مدت	تکمیل تست‌های رابط کاربری ExploitFA، افزودن حالت روشن/تاریک خودکار، و مستندسازی معماری هستهٔ Xray
میان‌مدت	انتشار vless-toolkit به‌صورت بستهٔ قابل نصب، افزودن پشتیبانی از پروتکل‌های بیشتر، و ساخت داشبورد سلامت زنجیرهٔ پروکسی در GhostTrace
بلندمدت	یکپارچه‌سازی ابزارها در یک جعبه‌ابزار ماژولار با گزارش‌های قابل‌بازتولید و امضاشده
</div>
Horizon	Focus
Short term	Complete ExploitFA UI tests, add automatic light/dark mode, document the Xray core architecture
Mid term	Publish vless-toolkit as an installable package, add support for more protocols, build a proxy-chain health dashboard in GhostTrace
Long term	Unify the toolset into a modular toolbox with reproducible, signed reports
📫 Reach Me
<div align="center"><table> <tr> <td align="center" width="25%">
GitHub

@Largo-m

</td> <td align="center" width="25%">
Work with me

Open an issue or a discussion on any project

</td> <td align="center" width="25%">
Support

GitHub Sponsors · a ⭐ on a repository you use is just as welcome

</td> <td align="center" width="25%">
Explore

All repositories · Achievements

</td> </tr> </table></div>
⚠️ Responsible Use
<div align="center">
Security tooling is for authorised testing only.
Use it on systems you own or have explicit written permission to assess.
Simulation tools include guard rails that refuse to run outside an authorised scope.
If you are unsure whether you have permission — you do not have permission.

</div>
<div align="center">
<sub>Built with care, tested in CI, and documented honestly. — Largo-m</sub>




<a href="https://github.com/Largo-m"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Largo--m-0d1117?style=for-the-badge&logo=github&logoColor=white"> </a> <a href="https://github.com/sponsors/Largo-m"> <img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?style=for-the-badge&labelColor=0d1117"> </a></div> ```
📌 راهنمای استفاده
<div dir="rtl">
