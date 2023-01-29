# EXA-Sub-Domain
(EXA, Example)

Contains a working example of using Sub Domains.

![](https://github.com/creativecommons/cc-assets/blob/main/license_badges/small/cc_zero.svg)

### Attribution

[CheeseCake87 (David Carmichael)](https://github.com/CheeseCake87)

### Setup

Add the following to your `hosts` file:

```bash
127.0.0.1       site.local
127.0.0.1       subdomain.site.local
```

Once you have set up the Flask project visit `http://site.local:5000` and `http://subdomain.site.local:5000` to see the results.

(This assumes you have Python installed)

#### Linux

1. Download or Clone this repository.
2. Open terminal and cd to the directory of the project.

```text
cd /path/to/FAS-3-Package
```

3. Create a virtual environment and activate it.

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

4. Install the requirements.

```bash
pip install -r requirements.txt
```

### run

```bash
flask run
```
or
```bash
python3 run.py
```
