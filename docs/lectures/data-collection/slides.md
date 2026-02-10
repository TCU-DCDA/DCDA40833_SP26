---
theme: default
title: Web Scraping & Data Ethics
info: |
  DCDA · Spring 2026
  Digital Culture & Data Analytics
class: text-center
drawings:
  persist: false
transition: slide-left
routerMode: hash
mdc: true
---

# Web Scraping & Data Ethics

<div class="mt-4 opacity-70 font-mono text-sm tracking-widest">DCDA · SPRING 2026</div>

<div class="abs-br m-6">
  <img src="/images/title.png" class="w-32 rounded-full shadow-xl shadow-teal-500/20" />
</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Web Scraping!

**Web scraping** (web harvesting, web data extraction) is data scraping used for extracting data from websites. Web scraping software may directly access the World Wide Web using HTTP or a web browser.

While web scraping can be done manually, the term typically refers to *automated processes* using a bot or web crawler. Specific data is gathered and copied from the web into a local database or spreadsheet for later retrieval or analysis.

<div class="font-mono text-xs text-teal-400 mt-4 opacity-70">
  <a href="https://en.wikipedia.org/wiki/Web_scraping" target="_blank">en.wikipedia.org/wiki/Web_scraping</a>
</div>

::right::

<img src="/images/web-scraping.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Robots.txt

<span class="font-mono text-teal-400 bg-teal-500/10 px-2 py-1 rounded text-sm">robots.txt</span> is the filename used for implementing the **Robots Exclusion Protocol**, a standard used by websites to *request* that visiting web crawlers and other web robots avoid certain portions of the website.

<div class="bg-amber-500/10 border-l-3 border-amber-400 pl-4 py-2 rounded-r mt-4 text-sm">
  ⚠️ Compliance is <strong>voluntary</strong> — legitimate crawlers like Googlebot typically honor robots.txt, but malicious bots may ignore it entirely.
</div>

<div class="font-mono text-xs text-teal-400 mt-4 opacity-70">
  <a href="https://en.wikipedia.org/wiki/Robots.txt" target="_blank">en.wikipedia.org/wiki/Robots.txt</a>
</div>

::right::

<img src="/images/robots-txt.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Robots.txt <span class="text-teal-400">in the wild</span>

Try visiting these yourself:

<div class="font-mono text-sm mt-4 space-y-2">
  <a href="https://addran.tcu.edu/robots.txt" target="_blank" class="block text-teal-400 hover:text-teal-300 border-b border-teal-500/10 pb-2">addran.tcu.edu/robots.txt</a>
  <a href="https://schieffercollege.tcu.edu/robots.txt" target="_blank" class="block text-teal-400 hover:text-teal-300 border-b border-teal-500/10 pb-2">schieffercollege.tcu.edu/robots.txt</a>
  <a href="https://www.imdb.com/robots.txt" target="_blank" class="block text-teal-400 hover:text-teal-300 border-b border-teal-500/10 pb-2">www.imdb.com/robots.txt</a>
  <a href="https://www.rottentomatoes.com/robots.txt" target="_blank" class="block text-teal-400 hover:text-teal-300 border-b border-teal-500/10 pb-2">www.rottentomatoes.com/robots.txt</a>
  <a href="https://gofrogs.com/robots.txt" target="_blank" class="block text-teal-400 hover:text-teal-300 pb-2">gofrogs.com/robots.txt</a>
</div>

::right::

<img src="/images/robots-examples.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Tarpitting <span class="text-teal-400">(I)</span>

A **tarpit** is a service on a computer system (usually a server) that purposely delays incoming connections.

The technique was originally developed as a defense against *spam and computer worms*. The idea: network abuses such as spamming or broad scanning are less effective — and therefore less attractive — if they take too long.

The concept is analogous with a **tar pit**, in which animals can get bogged down and slowly sink under the surface.

<div class="font-mono text-xs text-teal-400 mt-4 opacity-70">
  <a href="https://en.wikipedia.org/wiki/Tarpit_(networking)" target="_blank">en.wikipedia.org/wiki/Tarpit_(networking)</a>
</div>

::right::

<img src="/images/tarpitting.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Tarpitting <span class="text-teal-400">(II)</span>

### Historical origin

Tom Liston developed **LaBrea** in 2001 as a response to the *Code Red worm*. It could protect an entire network by claiming unused IP addresses and trapping scanners in fake TCP connections.

### Modern use

Tarpits have been adapted to counter **AI web scrapers** by trapping them in prolonged interactions that waste computational resources without yielding useful data. Some tarpits now serve crawlers incoherent text generated with Markov chains to poison their training datasets.

<div class="font-mono text-xs text-teal-400 mt-4 opacity-70">
  <a href="https://en.wikipedia.org/wiki/Tarpit_(networking)" target="_blank">en.wikipedia.org/wiki/Tarpit_(networking)</a>
</div>

::right::

<img src="/images/tarpitting.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Data Poisoning <span class="text-teal-400">(I)</span>

In the context of web scraping, **data poisoning** refers to techniques website owners use to deliberately serve incorrect or misleading data to detected scrapers while providing normal content to regular users.

Rather than blocking scrapers outright, the goal is to make harvested data *unreliable or unusable*.

<div class="bg-blue-500/10 border-l-3 border-blue-400 pl-4 py-2 rounded-r mt-4 text-sm">
  📝 <strong>Note:</strong> This is distinct from <em>data poisoning in machine learning</em>, where adversarial data is injected into training sets to corrupt model behavior.
</div>

::right::

<img src="/images/poisoning.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Data Poisoning <span class="text-teal-400">(II)</span>

### Common techniques

- Serving **randomized or fake data** when detecting scraper behavior patterns
- Injecting invisible **honeypot elements** that only scrapers would collect
- Adding **random delays or errors** to automated requests
- Returning **subtly corrupted data** like swapped fields or modified values
- Serving different content based on detected user-agent or behavioral signals (**cloaking**)

<div class="text-sm opacity-70 mt-4">
This is different from simply blocking scrapers — the goal is to make the scraped data unreliable or unusable.
</div>

::right::

<img src="/images/poisoning.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Data Poisoning <span class="text-teal-400">(III)</span>

### How scrapers get detected

- Request patterns and timing
- Missing or unusual browser fingerprints
- Lack of normal user behaviors (mouse movements, page scrolling)
- IP addresses associated with hosting providers
- Unusual traffic volumes from single sources

<div class="font-mono text-xs opacity-40 text-right mt-6">
—generated by Claude (Anthropic), verified against industry sources
</div>

::right::

<img src="/images/poisoning-detect2.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: two-cols
layoutClass: gap-8 items-center
---

# APIs

<span class="font-mono text-teal-400 bg-teal-500/10 px-2 py-1 rounded text-sm">Application Programming Interface</span>

It's a set of rules and protocols that allows different software applications to communicate and share data with each other in a structured way.

In data collection, APIs provide a *controlled, secure method* to request and receive specific data from a service, rather than having to scrape or manually extract information from websites.

<div class="font-mono text-xs opacity-40 text-right mt-6">
—generated by Claude (Anthropic)
</div>

::right::

<img src="/images/apis.png" class="rounded-xl shadow-2xl shadow-teal-500/10 w-80" />

---
layout: center
class: text-center
---

# Try It: <span class="text-teal-400">No-Code Web Scraping</span>

Chrome extensions for point-and-click data extraction

<div class="font-mono text-sm text-teal-400 mt-6">
  <a href="https://chromewebstore.google.com/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah" target="_blank">
    Instant Data Scraper ↗
  </a>
</div>

<div class="font-mono text-sm text-teal-400 mt-4">
  <a href="https://easyscraper.com/" target="_blank">
    Easy Scraper ↗
  </a>
</div>

---
layout: center
class: text-center
---

# Lab 4: <span class="text-teal-400">Data Sources</span>

A curated list of repositories for your Tableau visualization project

<div class="font-mono text-sm text-teal-400 mt-8">
  <a href="https://tcu-dcda.github.io/DCDA40833_SP26/labs/lab04.html#data-sources" target="_blank">
    Lab 4 — Data Sources ↗
  </a>
</div>
