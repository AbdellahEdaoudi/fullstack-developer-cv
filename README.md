# Full Stack Developer CV

A ready-to-use, **multi-language CV system** for Full Stack Developers.

Simply **edit the HTML files** with your information, then **run one command** to automatically generate professional PDF versions in all 8 languages - no browser needed.

Built with pure HTML & CSS. Print-ready, ATS-friendly, and fully customizable.

---

## Available Languages

| Language | File | PDF Output |
|----------|------|------------|
| English | `cv_en.html` | `cv-your-name-en.pdf` |
| French | `cv_fr.html` | `cv-your-name-fr.pdf` |
| Spanish | `cv_es.html` | `cv-your-name-es.pdf` |
| German | `cv_de.html` | `cv-your-name-de.pdf` |
| Dutch | `cv_nl.html` | `cv-your-name-nl.pdf` |
| Italian | `cv_it.html` | `cv-your-name-it.pdf` |
| Portuguese | `cv_pt.html` | `cv-your-name-pt.pdf` |
| Arabic (RTL) | `cv_ar.html` | `cv-your-name-ar.pdf` |

---

## Features

- **8 languages** including full RTL support (Arabic)
- **ATS-friendly** - clean semantic HTML, no tables, no images for content
- **Print-ready** - pixel-perfect A4 layout with `@media print` rules
- **FAANG-style** design - inspired by top tech industry CVs
- **Automated PDF generation** - one command generates all 8 PDFs
- **No CSS framework** - pure vanilla CSS for full control
- **Professional typography** - Times New Roman for Latin, Cairo for Arabic
- **Fully customizable** - just edit the HTML files

---

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) installed
- [Google Chrome](https://www.google.com/chrome/) installed

### 1. Clone the repository

```sh
git clone https://github.com/AbdellahEdaoudi/fullstack-developer-cv.git
cd fullstack-developer-cv
```

### 2. Install dependencies

```sh
npm install
```

### 3. Update your name in the scripts

> **Important:** Open both `generate_pdfs.js` and `build_all_cvs.py` and replace `abdellah-edaoudi` with your own full name in all 8 entries.

```js
// Before:
{ html: 'cv_en.html', pdf: 'cv-abdellah-edaoudi-en.pdf' },

// After - use your own name:
{ html: 'cv_en.html', pdf: 'cv-your-name-en.pdf' },
```

### 4. Edit the HTML files

Open any `cv_*.html` file and update:

- Your **name**, **title**, and **contact info**
- Your **professional summary**
- Your **skills**, **experience**, **projects**, and **education**

### 5. Generate PDFs

```sh
node generate_pdfs.js
```

Or using Python:

```sh
python build_all_cvs.py
```

Both commands generate all 8 PDF files in the project folder.

---

## Print / Export Manually

Open any `cv_*.html` in **Google Chrome**, press `Ctrl+P`, set margins to **None**, then **Save as PDF**.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| HTML5 + CSS3 | CV structure and styling |
| Puppeteer Core | Headless Chrome PDF generation |
| Python + subprocess | Alternative PDF generation script |
| Google Fonts (Cairo) | Arabic typography |

---

## Other Customization Tips

1. **Profile photo**: Replace `assets/profile.jpg` with your own photo (keep the same filename or update the `src` in the HTML files).
2. **Colors**: The primary accent color is `#1d4ed8` (blue) - easy to change in the CSS.
3. **Font size**: Adjust `font-size` in `body` to fit more or less content.
4. **Adding sections**: Follow the existing `<section>` pattern.

---

## Author

**Abdellah Edaoudi**
Full Stack Web Developer

- GitHub: [AbdellahEdaoudi](https://github.com/AbdellahEdaoudi)
- LinkedIn: [abdellah-edaoudi](https://linkedin.com/in/abdellah-edaoudi)
- Portfolio: [abdellah-edaoudi.vercel.app](https://abdellah-edaoudi.vercel.app)