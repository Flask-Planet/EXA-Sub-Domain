# EXA-Sub-Domain
(EXA, Example)

Contains a working example of using Sub Domains.

![](https://github.com/creativecommons/cc-assets/blob/main/license_badges/small/cc_zero.svg)

### Attribution

[CheeseCake87 (David Carmichael)](https://github.com/CheeseCake87)

### Setup

(This assumes you have Python installed)

1. Download or Clone this repository.
2. Open terminal (Linux) / powershell (Windows) and cd to the directory of the project.

```text
# Linux
cd /path/to/EXA-Sub-Domain

# Windows
cd C:\path\to\EXA-Sub-Domain
```

---

### Linux

**Create a virtual environment and activate it.**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

**run**

```bash
flask run
```
or
```bash
python3 run.py
```

---

### Windows


**Create a virtual environment and activate it.**

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

**run**

```bash
flask run
```
or
```bash
python run.py
```

---

### Post Setup
Add the following to your `hosts` file:

```bash
127.0.0.1       site.local
127.0.0.1       subdomain.site.local
```

Visit `http://site.local:5000` and `http://subdomain.site.local:5000` to see the results.

**Linux most common `hosts` file location**

`/etc/hosts`

(open with sudo if needed, edit, then save)

**Windows `hosts` file location**

`c:\Windows\System32\drivers\etc\hosts`

(copy to desktop, edit, then paste back to folder)