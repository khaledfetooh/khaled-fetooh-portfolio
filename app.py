from flask import Flask, render_template_string, request, redirect, url_for, send_file
from pathlib import Path
import json
from datetime import datetime

app = Flask(__name__)

# =========================================================
# CONFIG
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

CV_FILE_PATH = BASE_DIR / (
    "Khaled _Ebraheem Ahmed fetooh _JUNIOR SOC ANALYST _ IT  CYBERSECURITY_.pdf"
)

MESSAGES_FILE = BASE_DIR / "messages.json"

PROFILE_IMAGE = "/static/680255439_122288477030220135_281971630508430026_n.jpg"


# =========================================================
# HTML
# =========================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>
        Khaled Fetooh | Junior SOC Analyst
    </title>

    <meta
        name="description"
        content="Khaled Fetooh - Junior SOC Analyst | IT & Cybersecurity"
    >

    <script src="https://cdn.tailwindcss.com"></script>

    <script src="https://unpkg.com/lucide@latest"></script>


    <style>

        html {
            scroll-behavior: smooth;
        }

        body {
            background:
                radial-gradient(
                    circle at top left,
                    rgba(6,182,212,.10),
                    transparent 30%
                ),
                radial-gradient(
                    circle at bottom right,
                    rgba(59,130,246,.08),
                    transparent 30%
                ),
                #020617;
        }

        .glass {
            background: rgba(15,23,42,.72);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(148,163,184,.12);
        }

        .grid-bg {
            background-image:
                linear-gradient(
                    rgba(148,163,184,.05) 1px,
                    transparent 1px
                ),
                linear-gradient(
                    90deg,
                    rgba(148,163,184,.05) 1px,
                    transparent 1px
                );
            background-size: 35px 35px;
        }

        .glow {
            box-shadow:
                0 0 30px rgba(6,182,212,.10),
                0 0 80px rgba(59,130,246,.05);
        }

        .terminal {
            font-family:
                Consolas,
                Monaco,
                monospace;
        }

        .profile-ring {
            background:
                linear-gradient(
                    135deg,
                    rgba(34,211,238,.8),
                    rgba(59,130,246,.3),
                    transparent
                );
            padding: 3px;
        }

        .profile-image {
            object-fit: cover;
            object-position: center;
            background: #0f172a;
        }

        .skill {
            display: inline-flex;
            align-items: center;
            padding: .42rem .72rem;
            border-radius: .6rem;
            background: rgba(30,41,59,.75);
            border: 1px solid rgba(71,85,105,.5);
            color: #cbd5e1;
            font-size: .78rem;
            transition: .2s ease;
        }

        .skill:hover {
            border-color: rgba(34,211,238,.5);
            color: #67e8f9;
        }

    </style>

</head>


<body class="text-slate-200">


<!-- ===================================================== -->
<!-- NAVBAR -->
<!-- ===================================================== -->

<header class="fixed top-0 left-0 right-0 z-50">

    <nav class="glass">

        <div
            class="
                max-w-7xl
                mx-auto
                px-5
                py-4
                flex
                items-center
                justify-between
            "
        >

            <a
                href="#home"
                class="
                    font-black
                    text-xl
                    tracking-wide
                    text-white
                "
            >
                K<span class="text-cyan-400">.</span>F
            </a>


            <div
                class="
                    hidden
                    lg:flex
                    items-center
                    gap-6
                    text-sm
                "
            >

                <a href="#home"
                   class="hover:text-cyan-400 transition">
                    Home
                </a>

                <a href="#about"
                   class="hover:text-cyan-400 transition">
                    About
                </a>

                <a href="#skills"
                   class="hover:text-cyan-400 transition">
                    Skills
                </a>

                <a href="#experience"
                   class="hover:text-cyan-400 transition">
                    Experience
                </a>

                <a href="#projects"
                   class="hover:text-cyan-400 transition">
                    Projects
                </a>

                <a href="#education"
                   class="hover:text-cyan-400 transition">
                    Education
                </a>

                <a href="#contact"
                   class="hover:text-cyan-400 transition">
                    Contact
                </a>

            </div>


            <a
                href="/download-cv"

                class="
                    px-4
                    py-2
                    rounded-lg
                    bg-cyan-500
                    text-slate-950
                    font-bold
                    text-sm
                    hover:bg-cyan-400
                    transition
                    flex
                    items-center
                    gap-2
                "
            >

                <i
                    data-lucide="download"
                    class="w-4 h-4"
                ></i>

                Download CV

            </a>

        </div>

    </nav>

</header>



<!-- ===================================================== -->
<!-- HERO -->
<!-- ===================================================== -->

<section
    id="home"

    class="
        min-h-screen
        flex
        items-center
        relative
        overflow-hidden
        grid-bg
    "
>

    <div
        class="
            absolute
            w-72
            h-72
            bg-cyan-500/10
            rounded-full
            blur-3xl
            top-20
            left-10
        "
    ></div>


    <div
        class="
            absolute
            w-96
            h-96
            bg-blue-500/10
            rounded-full
            blur-3xl
            bottom-10
            right-10
        "
    ></div>


    <div
        class="
            max-w-7xl
            mx-auto
            px-5
            pt-28
            pb-16
            relative
            z-10
            w-full
        "
    >

        <div
            class="
                grid
                lg:grid-cols-2
                gap-14
                items-center
            "
        >


            <!-- LEFT -->

            <div>

                <div
                    class="
                        inline-flex
                        items-center
                        gap-2
                        px-3
                        py-2
                        rounded-full
                        border
                        border-cyan-400/20
                        bg-cyan-400/5
                        text-cyan-300
                        text-sm
                        mb-6
                    "
                >

                    <span
                        class="
                            w-2
                            h-2
                            bg-cyan-400
                            rounded-full
                            animate-pulse
                        "
                    ></span>

                    Junior SOC Analyst

                </div>


                <p
                    class="
                        text-cyan-400
                        font-mono
                        text-sm
                        mb-3
                    "
                >
                    HELLO, I'M
                </p>


                <h1
                    class="
                        text-4xl
                        md:text-6xl
                        font-black
                        leading-tight
                        text-white
                    "
                >

                    KHALED

                    <span class="text-cyan-400">
                        FETOOH
                    </span>

                </h1>


                <h2
                    class="
                        mt-5
                        text-xl
                        md:text-2xl
                        font-semibold
                        text-slate-300
                    "
                >

                    Junior SOC Analyst

                    <span class="text-cyan-400">
                        |
                    </span>

                    IT & Cybersecurity

                </h2>


                <p
                    class="
                        mt-6
                        text-slate-400
                        max-w-2xl
                        leading-8
                    "
                >

                    Junior cybersecurity professional focused on
                    Security Operations, SIEM, Log Analysis,
                    Incident Response, Windows Security,
                    Linux Administration and Network Security.

                </p>


                <div
                    class="
                        mt-8
                        flex
                        flex-wrap
                        gap-4
                    "
                >

                    <a
                        href="#projects"

                        class="
                            px-6
                            py-3
                            rounded-xl
                            bg-cyan-500
                            text-slate-950
                            font-bold
                            hover:bg-cyan-400
                            transition
                            flex
                            items-center
                            gap-2
                        "
                    >

                        <i
                            data-lucide="shield-check"
                            class="w-5 h-5"
                        ></i>

                        View Projects

                    </a>


                    <a
                        href="#contact"

                        class="
                            px-6
                            py-3
                            rounded-xl
                            border
                            border-slate-700
                            hover:border-cyan-400
                            hover:text-cyan-400
                            transition
                            flex
                            items-center
                            gap-2
                        "
                    >

                        <i
                            data-lucide="mail"
                            class="w-5 h-5"
                        ></i>

                        Contact Me

                    </a>

                </div>


                <div
                    class="
                        mt-8
                        flex
                        flex-wrap
                        gap-5
                        text-sm
                        text-slate-400
                    "
                >

                    <span
                        class="flex items-center gap-2"
                    >

                        <i
                            data-lucide="map-pin"
                            class="w-4 h-4 text-cyan-400"
                        ></i>

                        Egypt

                    </span>


                    <span
                        class="flex items-center gap-2"
                    >

                        <i
                            data-lucide="mail"
                            class="w-4 h-4 text-cyan-400"
                        ></i>

                        khaledfetoh266@gmail.com

                    </span>

                </div>

            </div>



            <!-- RIGHT -->

            <div
                class="
                    flex
                    flex-col
                    items-center
                    lg:items-end
                "
            >


                <!-- PROFILE -->

                <div
                    class="
                        profile-ring
                        rounded-full
                        w-60
                        h-60
                        md:w-72
                        md:h-72
                        glow
                        mb-8
                    "
                >

                    <div
                        class="
                            w-full
                            h-full
                            rounded-full
                            overflow-hidden
                            bg-slate-900
                        "
                    >

                        <img
                            src="/static/680255439_122288477030220135_281971630508430026_n.jpg"

                            alt="Khaled Fetooh"

                            class="
                                profile-image
                                w-full
                                h-full
                            "
                        >

                    </div>

                </div>



                <!-- TERMINAL -->

                <div
                    class="
                        glass
                        rounded-2xl
                        overflow-hidden
                        glow
                        w-full
                        max-w-xl
                    "
                >

                    <div
                        class="
                            flex
                            items-center
                            gap-2
                            px-5
                            py-3
                            border-b
                            border-slate-700/50
                        "
                    >

                        <span
                            class="
                                w-3
                                h-3
                                rounded-full
                                bg-red-400
                            "
                        ></span>

                        <span
                            class="
                                w-3
                                h-3
                                rounded-full
                                bg-yellow-400
                            "
                        ></span>

                        <span
                            class="
                                w-3
                                h-3
                                rounded-full
                                bg-green-400
                            "
                        ></span>


                        <span
                            class="
                                ml-3
                                text-xs
                                text-slate-500
                                terminal
                            "
                        >
                            khaled@soc:~
                        </span>

                    </div>


                    <div
                        class="
                            p-6
                            terminal
                            text-sm
                            leading-8
                        "
                    >

                        <p>

                            <span class="text-cyan-400">
                                khaled@soc
                            </span>:

                            <span class="text-blue-400">
                                ~
                            </span>$

                            whoami

                        </p>


                        <p class="text-green-400">
                            Khaled Fetooh
                        </p>


                        <p class="mt-3">

                            <span class="text-cyan-400">
                                khaled@soc
                            </span>:

                            <span class="text-blue-400">
                                ~
                            </span>$

                            role

                        </p>


                        <p class="text-white">
                            Junior SOC Analyst
                        </p>


                        <p class="mt-3">

                            <span class="text-cyan-400">
                                khaled@soc
                            </span>:

                            <span class="text-blue-400">
                                ~
                            </span>$

                            tools

                        </p>


                        <p class="text-yellow-300">
                            Splunk | Windows Logs | Linux
                        </p>


                        <p class="mt-3">

                            <span class="text-cyan-400">
                                khaled@soc
                            </span>:

                            <span class="text-blue-400">
                                ~
                            </span>$

                            focus

                        </p>


                        <p class="text-slate-300">
                            SIEM / Monitoring / Incident Response
                        </p>


                        <p class="mt-3">

                            <span class="text-cyan-400">
                                khaled@soc
                            </span>:

                            <span class="text-blue-400">
                                ~
                            </span>$

                            status

                        </p>


                        <p class="text-green-400">
                            ● Learning & Building
                        </p>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- ABOUT -->
<!-- ===================================================== -->

<section
    id="about"
    class="py-24"
>

    <div
        class="
            max-w-6xl
            mx-auto
            px-5
        "
    >

        <div class="text-center mb-14">

            <p
                class="
                    text-cyan-400
                    font-mono
                    text-sm
                "
            >
                01 / ABOUT
            </p>


            <h2
                class="
                    text-3xl
                    md:text-4xl
                    font-black
                    text-white
                    mt-2
                "
            >
                About Me
            </h2>

        </div>



        <div
            class="
                grid
                md:grid-cols-2
                gap-8
            "
        >


            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                "
            >

                <div
                    class="
                        flex
                        items-center
                        gap-3
                        mb-5
                    "
                >

                    <div
                        class="
                            p-3
                            rounded-xl
                            bg-cyan-400/10
                        "
                    >

                        <i
                            data-lucide="shield"
                            class="text-cyan-400"
                        ></i>

                    </div>


                    <h3
                        class="
                            text-xl
                            font-bold
                            text-white
                        "
                    >
                        Cybersecurity Focus
                    </h3>

                </div>


                <p
                    class="
                        text-slate-400
                        leading-8
                    "
                >

                    I am a Junior SOC Analyst focused on
                    Security Monitoring, SIEM, Log Analysis,
                    Incident Response, Windows Security
                    and Linux Administration.

                </p>

            </div>



            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                "
            >

                <div
                    class="
                        flex
                        items-center
                        gap-3
                        mb-5
                    "
                >

                    <div
                        class="
                            p-3
                            rounded-xl
                            bg-blue-400/10
                        "
                    >

                        <i
                            data-lucide="monitor-search"
                            class="text-blue-400"
                        ></i>

                    </div>


                    <h3
                        class="
                            text-xl
                            font-bold
                            text-white
                        "
                    >
                        SOC & Systems
                    </h3>

                </div>


                <p
                    class="
                        text-slate-400
                        leading-8
                    "
                >

                    Practical experience with Splunk,
                    Windows Event Logs, Event Viewer,
                    Group Policy, log collection,
                    Windows administration and Red Hat Linux.

                </p>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- SKILLS -->
<!-- ===================================================== -->

<section
    id="skills"
    class="
        py-24
        bg-slate-950/50
    "
>

    <div
        class="
            max-w-6xl
            mx-auto
            px-5
        "
    >

        <div class="text-center mb-14">

            <p
                class="
                    text-cyan-400
                    font-mono
                    text-sm
                "
            >
                02 / SKILLS
            </p>


            <h2
                class="
                    text-3xl
                    md:text-4xl
                    font-black
                    text-white
                    mt-2
                "
            >
                Technical Skills
            </h2>

        </div>



        <div
            class="
                grid
                md:grid-cols-2
                lg:grid-cols-3
                gap-6
            "
        >


            <!-- SOC -->

            <div class="glass rounded-2xl p-6">

                <i
                    data-lucide="shield-alert"
                    class="
                        text-cyan-400
                        w-8
                        h-8
                        mb-5
                    "
                ></i>


                <h3
                    class="
                        text-lg
                        font-bold
                        text-white
                        mb-4
                    "
                >
                    SOC & SIEM
                </h3>


                <div
                    class="flex flex-wrap gap-2"
                >

                    <span class="skill">
                        SOC Operations
                    </span>

                    <span class="skill">
                        Splunk
                    </span>

                    <span class="skill">
                        SPL
                    </span>

                    <span class="skill">
                        SIEM
                    </span>

                    <span class="skill">
                        Log Analysis
                    </span>

                    <span class="skill">
                        Security Monitoring
                    </span>

                    <span class="skill">
                        Alert Analysis
                    </span>

                    <span class="skill">
                        Incident Response
                    </span>

                </div>

            </div>



            <!-- WINDOWS -->

            <div class="glass rounded-2xl p-6">

                <i
                    data-lucide="monitor"
                    class="
                        text-cyan-400
                        w-8
                        h-8
                        mb-5
                    "
                ></i>


                <h3
                    class="
                        text-lg
                        font-bold
                        text-white
                        mb-4
                    "
                >
                    Windows Security
                </h3>


                <div
                    class="flex flex-wrap gap-2"
                >

                    <span class="skill">
                        Windows
                    </span>

                    <span class="skill">
                        Windows Event Logs
                    </span>

                    <span class="skill">
                        Event Viewer
                    </span>

                    <span class="skill">
                        Group Policy
                    </span>

                    <span class="skill">
                        GPO
                    </span>

                    <span class="skill">
                        Security Logs
                    </span>

                    <span class="skill">
                        Log Collection
                    </span>

                    <span class="skill">
                        Windows Administration
                    </span>

                    <span class="skill">
                        Troubleshooting
                    </span>

                </div>

            </div>



            <!-- LINUX -->

            <div class="glass rounded-2xl p-6">

                <i
                    data-lucide="terminal"
                    class="
                        text-cyan-400
                        w-8
                        h-8
                        mb-5
                    "
                ></i>


                <h3
                    class="
                        text-lg
                        font-bold
                        text-white
                        mb-4
                    "
                >
                    Linux Administration
                </h3>


                <div
                    class="flex flex-wrap gap-2"
                >

                    <span class="skill">
                        Red Hat Enterprise Linux
                    </span>

                    <span class="skill">
                        RHEL
                    </span>

                    <span class="skill">
                        System Administration I
                    </span>

                    <span class="skill">
                        System Administration II
                    </span>

                    <span class="skill">
                        Users & Groups
                    </span>

                    <span class="skill">
                        Storage
                    </span>

                    <span class="skill">
                        LVM
                    </span>

                    <span class="skill">
                        SELinux
                    </span>

                    <span class="skill">
                        Firewall
                    </span>

                    <span class="skill">
                        SSH
                    </span>

                    <span class="skill">
                        NFS
                    </span>

                    <span class="skill">
                        Autofs
                    </span>

                </div>

            </div>



            <!-- NETWORKING -->

            <div class="glass rounded-2xl p-6">

                <i
                    data-lucide="network"
                    class="
                        text-cyan-400
                        w-8
                        h-8
                        mb-5
                    "
                ></i>


                <h3
                    class="
                        text-lg
                        font-bold
                        text-white
                        mb-4
                    "
                >
                    Networking
                </h3>


                <div
                    class="flex flex-wrap gap-2"
                >

                    <span class="skill">
                        TCP/IP
                    </span>

                    <span class="skill">
                        OSI Model
                    </span>

                    <span class="skill">
                        VLAN
                    </span>

                    <span class="skill">
                        Routing
                    </span>

                    <span class="skill">
                        Switching
                    </span>

                    <span class="skill">
                        DHCP
                    </span>

                    <span class="skill">
                        DNS
                    </span>

                    <span class="skill">
                        Physical Routers
                    </span>

                    <span class="skill">
                        Physical Switches
                    </span>

                    <span class="skill">
                        Network Troubleshooting
                    </span>

                </div>

            </div>



            <!-- SECURITY -->

            <div class="glass rounded-2xl p-6">

                <i
                    data-lucide="lock-keyhole"
                    class="
                        text-cyan-400
                        w-8
                        h-8
                        mb-5
                    "
                ></i>


                <h3
                    class="
                        text-lg
                        font-bold
                        text-white
                        mb-4
                    "
                >
                    Network Security
                </h3>


                <div
                    class="flex flex-wrap gap-2"
                >

                    <span class="skill">
                        Fortinet
                    </span>

                    <span class="skill">
                        Huawei Security
                    </span>

                    <span class="skill">
                        Firewall
                    </span>

                    <span class="skill">
                        AAA
                    </span>

                    <span class="skill">
                        Kerberos
                    </span>

                    <span class="skill">
                        DHCP Snooping
                    </span>

                    <span class="skill">
                        Dynamic ARP Inspection
                    </span>

                </div>

            </div>



            <!-- TOOLS -->

            <div class="glass rounded-2xl p-6">

                <i
                    data-lucide="code-2"
                    class="
                        text-cyan-400
                        w-8
                        h-8
                        mb-5
                    "
                ></i>


                <h3
                    class="
                        text-lg
                        font-bold
                        text-white
                        mb-4
                    "
                >
                    Programming & Tools
                </h3>


                <div
                    class="flex flex-wrap gap-2"
                >

                    <span class="skill">
                        Python
                    </span>

                    <span class="skill">
                        Flask
                    </span>

                    <span class="skill">
                        SQL
                    </span>

                    <span class="skill">
                        SQLite
                    </span>

                    <span class="skill">
                        Scapy
                    </span>

                    <span class="skill">
                        Wireshark
                    </span>

                    <span class="skill">
                        VMware
                    </span>

                    <span class="skill">
                        pfSense
                    </span>

                </div>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- EXPERIENCE & TRAINING -->
<!-- ===================================================== -->

<section
    id="experience"
    class="py-24"
>

    <div
        class="
            max-w-6xl
            mx-auto
            px-5
        "
    >

        <div class="text-center mb-14">

            <p
                class="
                    text-cyan-400
                    font-mono
                    text-sm
                "
            >
                03 / EXPERIENCE
            </p>


            <h2
                class="
                    text-3xl
                    md:text-4xl
                    font-black
                    text-white
                    mt-2
                "
            >
                Experience & Training
            </h2>

        </div>



        <div class="space-y-6">


            <!-- DEPI -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            DEPI
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            Cyber Security Incident Response Analyst
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        2026 – Present
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Professional cybersecurity training focused on
                    Incident Response, SOC Operations,
                    Security Monitoring, Networking and
                    practical security concepts.

                </p>

            </div>



            <!-- CIB -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            CIB Egypt
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            Summer Internship – The Green Leap
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        2025
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Internship experience covering banking
                    environment, sustainability, AI ethics,
                    cybersecurity concepts and professional
                    development.

                </p>

            </div>



            <!-- FORTINET -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            Fortinet Cybersecurity Training
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            NTI / DEPI
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        Oct – Dec 2025
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    120-hour cybersecurity training covering
                    Fortinet security technologies,
                    networking and security fundamentals.

                </p>


                <div class="mt-4">

                    <span
                        class="
                            inline-flex
                            px-3
                            py-1
                            rounded-full
                            bg-green-400/10
                            text-green-400
                            text-sm
                        "
                    >
                        Final Score: 98%
                    </span>

                </div>

            </div>



            <!-- HUAWEI -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            Huawei HCIA-Security V4.0
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            NTI
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        2026
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Security training covering network security
                    concepts and Huawei security technologies.

                </p>

            </div>



            <!-- RED HAT I -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            Red Hat System Administration I
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            RH124
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        Certificate of Attendance
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Red Hat Enterprise Linux administration
                    training covering command-line administration,
                    users and groups, permissions, networking,
                    services and system management.

                </p>

            </div>



            <!-- RED HAT II -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            Red Hat System Administration II
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            RH134
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        Certificate of Attendance
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Advanced Red Hat Enterprise Linux
                    administration training covering
                    storage, LVM, networking, services,
                    security, SELinux and system administration.

                </p>

            </div>



            <!-- NTI RED HAT -->

            <div class="glass rounded-2xl p-7">

                <div
                    class="
                        flex
                        flex-col
                        md:flex-row
                        md:justify-between
                        gap-4
                    "
                >

                    <div>

                        <h3
                            class="
                                text-xl
                                font-bold
                                text-white
                            "
                        >
                            Red Hat Linux Administration
                        </h3>


                        <p class="text-cyan-400 mt-1">
                            National Telecommunication Institute (NTI)
                        </p>

                    </div>


                    <span
                        class="
                            text-sm
                            text-slate-500
                        "
                    >
                        Certificate / Training
                    </span>

                </div>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Practical Linux administration training
                    covering Red Hat Enterprise Linux,
                    command-line administration, networking,
                    storage and system management.

                </p>

            </div>



            <!-- CCNA -->

            <div class="glass rounded-2xl p-7">

                <h3
                    class="
                        text-xl
                        font-bold
                        text-white
                    "
                >
                    CCNA 200-301 Corporate Training
                </h3>


                <p class="text-cyan-400 mt-1">
                    Practical Networking Training
                </p>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Hands-on networking training using
                    physical routers and switches,
                    covering routing, switching,
                    VLANs, TCP/IP and network troubleshooting.

                </p>

            </div>



            <!-- WINDOWS -->

            <div class="glass rounded-2xl p-7">

                <h3
                    class="
                        text-xl
                        font-bold
                        text-white
                    "
                >
                    Windows Administration & Security
                </h3>


                <p class="text-cyan-400 mt-1">
                    Practical System Administration
                </p>


                <p
                    class="
                        text-slate-400
                        mt-5
                        leading-8
                    "
                >

                    Hands-on work with Windows administration,
                    Group Policy, Windows Event Logs,
                    Event Viewer, security logs,
                    log collection and troubleshooting.

                </p>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- PROJECTS -->
<!-- ===================================================== -->

<section
    id="projects"
    class="
        py-24
        bg-slate-950/50
    "
>

    <div
        class="
            max-w-6xl
            mx-auto
            px-5
        "
    >

        <div class="text-center mb-14">

            <p
                class="
                    text-cyan-400
                    font-mono
                    text-sm
                "
            >
                04 / PROJECTS
            </p>


            <h2
                class="
                    text-3xl
                    md:text-4xl
                    font-black
                    text-white
                    mt-2
                "
            >
                Security Projects
            </h2>

        </div>



        <div
            class="
                grid
                md:grid-cols-2
                gap-7
            "
        >


            <!-- SOS -->

            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                    hover:border-cyan-400/30
                    transition
                "
            >

                <div
                    class="
                        flex
                        items-start
                        justify-between
                        gap-4
                    "
                >

                    <div
                        class="
                            p-3
                            rounded-xl
                            bg-cyan-400/10
                        "
                    >

                        <i
                            data-lucide="shield-alert"
                            class="
                                text-cyan-400
                                w-7
                                h-7
                            "
                        ></i>

                    </div>


                    <span
                        class="
                            text-xs
                            px-3
                            py-1
                            rounded-full
                            bg-cyan-400/10
                            text-cyan-300
                        "
                    >
                        SOC Project
                    </span>

                </div>


                <h3
                    class="
                        text-2xl
                        font-bold
                        text-white
                        mt-6
                    "
                >
                    Security Operating System (SOS)
                </h3>


                <p
                    class="
                        text-slate-400
                        mt-4
                        leading-8
                    "
                >

                    SOC Monitoring & Incident Response Platform
                    designed to collect security information,
                    classify network activity and display
                    security alerts through a centralized dashboard.

                </p>


                <div
                    class="
                        mt-6
                        flex
                        flex-wrap
                        gap-2
                    "
                >

                    <span class="skill">
                        Python
                    </span>

                    <span class="skill">
                        Flask
                    </span>

                    <span class="skill">
                        SQLite
                    </span>

                    <span class="skill">
                        Scapy
                    </span>

                    <span class="skill">
                        UDP
                    </span>

                    <span class="skill">
                        SOC
                    </span>

                </div>


                <div
                    class="
                        mt-6
                        text-sm
                        text-slate-500
                    "
                >

                    Security Agent
                    →
                    UDP JSON
                    →
                    Flask
                    →
                    SQLite
                    →
                    Dashboard

                </div>

            </div>



            <!-- CYBERSHIELD -->

            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                    hover:border-cyan-400/30
                    transition
                "
            >

                <div
                    class="
                        flex
                        items-start
                        justify-between
                        gap-4
                    "
                >

                    <div
                        class="
                            p-3
                            rounded-xl
                            bg-blue-400/10
                        "
                    >

                        <i
                            data-lucide="scan-search"
                            class="
                                text-blue-400
                                w-7
                                h-7
                            "
                        ></i>

                    </div>


                    <span
                        class="
                            text-xs
                            px-3
                            py-1
                            rounded-full
                            bg-blue-400/10
                            text-blue-300
                        "
                    >
                        Security Tool
                    </span>

                </div>


                <h3
                    class="
                        text-2xl
                        font-bold
                        text-white
                        mt-6
                    "
                >
                    CyberShield Analyzer
                </h3>


                <p
                    class="
                        text-slate-400
                        mt-4
                        leading-8
                    "
                >

                    Flask-based security analysis project
                    for URL scanning and classification
                    using machine-learning techniques.

                </p>


                <div
                    class="
                        mt-6
                        flex
                        flex-wrap
                        gap-2
                    "
                >

                    <span class="skill">
                        Python
                    </span>

                    <span class="skill">
                        Flask
                    </span>

                    <span class="skill">
                        PostgreSQL
                    </span>

                    <span class="skill">
                        Machine Learning
                    </span>

                    <span class="skill">
                        Web Security
                    </span>

                </div>


                <div
                    class="
                        mt-6
                        text-sm
                        text-slate-500
                    "
                >

                    Reported model accuracy:
                    85.47%

                </div>

            </div>



            <!-- WINDOWS LOGS -->

            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                    hover:border-cyan-400/30
                    transition
                "
            >

                <div
                    class="
                        p-3
                        rounded-xl
                        bg-purple-400/10
                        w-fit
                    "
                >

                    <i
                        data-lucide="file-search"
                        class="
                            text-purple-400
                            w-7
                            h-7
                        "
                    ></i>

                </div>


                <h3
                    class="
                        text-2xl
                        font-bold
                        text-white
                        mt-6
                    "
                >
                    Windows Security Log Analysis
                </h3>


                <p
                    class="
                        text-slate-400
                        mt-4
                        leading-8
                    "
                >

                    Practical work with Windows Security Logs,
                    Event Viewer and Group Policy concepts
                    for understanding authentication activity,
                    security events and log collection
                    used in SOC monitoring.

                </p>


                <div
                    class="
                        mt-6
                        flex
                        flex-wrap
                        gap-2
                    "
                >

                    <span class="skill">
                        Windows
                    </span>

                    <span class="skill">
                        Event Viewer
                    </span>

                    <span class="skill">
                        Security Logs
                    </span>

                    <span class="skill">
                        Group Policy
                    </span>

                    <span class="skill">
                        Log Analysis
                    </span>

                </div>

            </div>



            <!-- SPLUNK -->

            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                    hover:border-cyan-400/30
                    transition
                "
            >

                <div
                    class="
                        p-3
                        rounded-xl
                        bg-orange-400/10
                        w-fit
                    "
                >

                    <i
                        data-lucide="bar-chart-3"
                        class="
                            text-orange-400
                            w-7
                            h-7
                        "
                    ></i>

                </div>


                <h3
                    class="
                        text-2xl
                        font-bold
                        text-white
                        mt-6
                    "
                >
                    Splunk SIEM & Log Analysis
                </h3>


                <p
                    class="
                        text-slate-400
                        mt-4
                        leading-8
                    "
                >

                    Hands-on experience with Splunk for
                    searching and analyzing security events,
                    working with logs and investigating
                    suspicious activity within a SIEM workflow.

                </p>


                <div
                    class="
                        mt-6
                        flex
                        flex-wrap
                        gap-2
                    "
                >

                    <span class="skill">
                        Splunk
                    </span>

                    <span class="skill">
                        SIEM
                    </span>

                    <span class="skill">
                        SPL
                    </span>

                    <span class="skill">
                        Log Analysis
                    </span>

                    <span class="skill">
                        Security Monitoring
                    </span>

                </div>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- EDUCATION -->
<!-- ===================================================== -->

<section
    id="education"
    class="py-24"
>

    <div
        class="
            max-w-6xl
            mx-auto
            px-5
        "
    >

        <div class="text-center mb-14">

            <p
                class="
                    text-cyan-400
                    font-mono
                    text-sm
                "
            >
                05 / EDUCATION
            </p>


            <h2
                class="
                    text-3xl
                    md:text-4xl
                    font-black
                    text-white
                    mt-2
                "
            >
                Education
            </h2>

        </div>



        <div
            class="
                glass
                rounded-2xl
                p-8
            "
        >

            <div
                class="
                    flex
                    flex-col
                    md:flex-row
                    gap-6
                "
            >

                <div
                    class="
                        p-4
                        rounded-2xl
                        bg-cyan-400/10
                        h-fit
                    "
                >

                    <i
                        data-lucide="graduation-cap"
                        class="
                            w-9
                            h-9
                            text-cyan-400
                        "
                    ></i>

                </div>


                <div class="flex-1">

                    <div
                        class="
                            flex
                            flex-col
                            md:flex-row
                            md:justify-between
                            gap-3
                        "
                    >

                        <div>

                            <h3
                                class="
                                    text-2xl
                                    font-bold
                                    text-white
                                "
                            >
                                Bachelor of Artificial Intelligence
                            </h3>


                            <p
                                class="
                                    text-cyan-400
                                    mt-1
                                "
                            >
                                Delta University for Science & Technology
                            </p>

                        </div>


                        <span
                            class="
                                text-sm
                                text-slate-500
                            "
                        >
                            2023 – 2026
                        </span>

                    </div>


                    <p
                        class="
                            text-slate-400
                            mt-5
                            leading-8
                        "
                    >

                        Academic background in Artificial Intelligence
                        with a professional focus on cybersecurity,
                        networking, systems and Security Operations.

                    </p>


                    <div class="mt-5">

                        <span
                            class="
                                inline-flex
                                px-3
                                py-1
                                rounded-full
                                bg-slate-800
                                text-slate-300
                                text-sm
                            "
                        >
                            GPA: 2.74
                        </span>

                    </div>

                </div>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- CONTACT -->
<!-- ===================================================== -->

<section
    id="contact"
    class="
        py-24
        bg-slate-950/50
    "
>

    <div
        class="
            max-w-5xl
            mx-auto
            px-5
        "
    >

        <div class="text-center mb-14">

            <p
                class="
                    text-cyan-400
                    font-mono
                    text-sm
                "
            >
                06 / CONTACT
            </p>


            <h2
                class="
                    text-3xl
                    md:text-4xl
                    font-black
                    text-white
                    mt-2
                "
            >
                Let's Connect
            </h2>


            <p
                class="
                    text-slate-400
                    mt-4
                "
            >
                Interested in cybersecurity,
                SOC operations or collaboration?
            </p>

        </div>



        <div
            class="
                grid
                md:grid-cols-2
                gap-7
            "
        >


            <!-- CONTACT INFO -->

            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                "
            >

                <h3
                    class="
                        text-xl
                        font-bold
                        text-white
                        mb-7
                    "
                >
                    Contact Information
                </h3>


                <div class="space-y-6">


                    <!-- EMAIL -->

                    <a
                        href="mailto:khaledfetoh266@gmail.com"
                        class="
                            flex
                            items-center
                            gap-4
                            group
                        "
                    >

                        <div
                            class="
                                p-3
                                rounded-xl
                                bg-cyan-400/10
                            "
                        >

                            <i
                                data-lucide="mail"
                                class="text-cyan-400"
                            ></i>

                        </div>


                        <div>

                            <p
                                class="
                                    text-xs
                                    text-slate-500
                                "
                            >
                                Email
                            </p>


                            <p
                                class="
                                    text-slate-200
                                    group-hover:text-cyan-400
                                    transition
                                "
                            >
                                khaledfetoh266@gmail.com
                            </p>

                        </div>

                    </a>



                    <!-- PHONE -->

                    <a
                        href="tel:+201005059033"
                        class="
                            flex
                            items-center
                            gap-4
                            group
                        "
                    >

                        <div
                            class="
                                p-3
                                rounded-xl
                                bg-cyan-400/10
                            "
                        >

                            <i
                                data-lucide="phone"
                                class="text-cyan-400"
                            ></i>

                        </div>


                        <div>

                            <p
                                class="
                                    text-xs
                                    text-slate-500
                                "
                            >
                                Phone
                            </p>


                            <p
                                class="
                                    text-slate-200
                                    group-hover:text-cyan-400
                                    transition
                                "
                            >
                                +20 100 505 9033
                            </p>

                        </div>

                    </a>



                    <!-- LINKEDIN -->

                    <a
                        href="https://linkedin.com/in/khaled-fetooh-6312852bb"
                        target="_blank"

                        class="
                            flex
                            items-center
                            gap-4
                            group
                        "
                    >

                        <div
                            class="
                                p-3
                                rounded-xl
                                bg-cyan-400/10
                            "
                        >

                            <i
                                data-lucide="linkedin"
                                class="text-cyan-400"
                            ></i>

                        </div>


                        <div>

                            <p
                                class="
                                    text-xs
                                    text-slate-500
                                "
                            >
                                LinkedIn
                            </p>


                            <p
                                class="
                                    text-slate-200
                                    group-hover:text-cyan-400
                                    transition
                                "
                            >
                                Khaled Fetooh
                            </p>

                        </div>

                    </a>

                </div>

            </div>



            <!-- FORM -->

            <div
                class="
                    glass
                    rounded-2xl
                    p-7
                "
            >

                <h3
                    class="
                        text-xl
                        font-bold
                        text-white
                        mb-6
                    "
                >
                    Send a Message
                </h3>


                <form
                    method="POST"
                    action="/contact"
                    class="space-y-5"
                >


                    <div>

                        <label
                            class="
                                block
                                text-sm
                                text-slate-400
                                mb-2
                            "
                        >
                            Name
                        </label>


                        <input
                            type="text"
                            name="name"
                            required

                            class="
                                w-full
                                px-4
                                py-3
                                rounded-xl
                                bg-slate-950
                                border
                                border-slate-700
                                focus:border-cyan-400
                                outline-none
                                transition
                            "

                            placeholder="Your name"
                        >

                    </div>



                    <div>

                        <label
                            class="
                                block
                                text-sm
                                text-slate-400
                                mb-2
                            "
                        >
                            Email
                        </label>


                        <input
                            type="email"
                            name="email"
                            required

                            class="
                                w-full
                                px-4
                                py-3
                                rounded-xl
                                bg-slate-950
                                border
                                border-slate-700
                                focus:border-cyan-400
                                outline-none
                                transition
                            "

                            placeholder="you@example.com"
                        >

                    </div>



                    <div>

                        <label
                            class="
                                block
                                text-sm
                                text-slate-400
                                mb-2
                            "
                        >
                            Message
                        </label>


                        <textarea
                            name="message"
                            rows="5"
                            required

                            class="
                                w-full
                                px-4
                                py-3
                                rounded-xl
                                bg-slate-950
                                border
                                border-slate-700
                                focus:border-cyan-400
                                outline-none
                                transition
                                resize-none
                            "

                            placeholder="Write your message..."
                        ></textarea>

                    </div>



                    <button
                        type="submit"

                        class="
                            w-full
                            py-3
                            rounded-xl
                            bg-cyan-500
                            text-slate-950
                            font-bold
                            hover:bg-cyan-400
                            transition
                            flex
                            justify-center
                            items-center
                            gap-2
                        "
                    >

                        <i
                            data-lucide="send"
                            class="w-5 h-5"
                        ></i>

                        Send Message

                    </button>

                </form>

            </div>

        </div>

    </div>

</section>



<!-- ===================================================== -->
<!-- FOOTER -->
<!-- ===================================================== -->

<footer
    class="
        border-t
        border-slate-800
    "
>

    <div
        class="
            max-w-6xl
            mx-auto
            px-5
            py-8
        "
    >

        <div
            class="
                flex
                flex-col
                md:flex-row
                justify-between
                items-center
                gap-4
            "
        >

            <p
                class="
                    text-sm
                    text-slate-500
                "
            >
                © 2026 Khaled Fetooh.
                All rights reserved.
            </p>


            <p
                class="
                    text-sm
                    text-slate-600
                    terminal
                "
            >
                Built with Flask
            </p>

        </div>

    </div>

</footer>



<script>

    lucide.createIcons();

</script>


</body>

</html>
"""


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template_string(HTML)


# =========================================================
# DOWNLOAD CV
# =========================================================

@app.route("/download-cv")
def download_cv():

    if not CV_FILE_PATH.exists():

        return (
            "CV file not found on server.<br><br>"
            f"Expected file:<br>"
            f"{CV_FILE_PATH.name}",
            404
        )


    if CV_FILE_PATH.suffix.lower() != ".pdf":

        return (
            "The CV file must have a .pdf extension.",
            400
        )


    # Verify that the file is actually a PDF

    try:

        with open(
            CV_FILE_PATH,
            "rb"
        ) as f:

            file_header = f.read(5)


        if file_header != b"%PDF-":

            return (
                "The CV file is not a valid PDF file.<br><br>"
                "Please export your CV as a real PDF file.",
                400
            )


    except Exception as e:

        return (
            f"Could not read CV file: {e}",
            500
        )


    return send_file(

        CV_FILE_PATH,

        as_attachment=True,

        download_name="Khaled_Fetooh_CV.pdf",

        mimetype="application/pdf"

    )


# =========================================================
# CONTACT
# =========================================================

@app.route(
    "/contact",
    methods=["POST"]
)
def contact():

    name = request.form.get(
        "name",
        ""
    ).strip()


    email = request.form.get(
        "email",
        ""
    ).strip()


    message = request.form.get(
        "message",
        ""
    ).strip()


    if not name or not email or not message:

        return redirect(
            url_for("home") + "#contact"
        )


    new_message = {

        "name": name,

        "email": email,

        "message": message,

        "date": datetime.now().isoformat()

    }


    messages = []


    if MESSAGES_FILE.exists():

        try:

            with open(
                MESSAGES_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                messages = json.load(f)


            if not isinstance(
                messages,
                list
            ):

                messages = []


        except Exception:

            messages = []


    messages.append(
        new_message
    )


    with open(
        MESSAGES_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            messages,
            f,
            ensure_ascii=False,
            indent=4
        )


    return redirect(
        url_for("home") + "#contact"
    )


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )