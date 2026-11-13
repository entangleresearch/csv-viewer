# CSV by eRL — Research Paper Explorer

**A bilingual, offline-capable research dataset explorer by [Entangle Research Lab](https://www.entangleresearch.com/).**

Search publication records, combine advanced filters, choose table columns, inspect paper details, and export precisely the results you need. Built with plain HTML, CSS, and JavaScript: **no server, database, account, API key, or build step needed**.

[Lab website](https://www.entangleresearch.com/) · [eRL GitHub organization](https://github.com/entangleresearch)

## Features

| Feature | Details |
| --- | --- |
| **English / বাংলা** | Switch the interface and built-in guide between English and Bengali. Original dataset cell contents are not machine-translated. |
| **Light / dark** | Use the circular theme toggle in the header; preference is remembered where browser storage is available. |
| **Flexible search** | Search research content, all columns, displayed columns, or any particular field. Use `"exact phrases"`. |
| **Advanced conditions** | Combine `AND` / `OR`, contains / excludes / equals / begins / ends, empty / not empty, and numeric operators. |
| **Column control** | Essential / Research / All presets, individual checkboxes, and column-name search. The full column list expands with the page, without its own vertical scrollbar. |
| **Paper details** | Open a record to see abstracts, authors, affiliations, keywords, and other metadata; follow DOI/PDF links. |
| **Sort and browse** | Sort by clicking headers; choose page size and navigate results. The results table grows vertically with the page, while horizontal scrolling is available for wide tables. |
| **CSV export** | Export filtered records using only selected columns; includes spreadsheet-formula safety mitigation. |
| **New CSV import** | Load another CSV from your device or drag and drop it. Import is temporary for the current page session. |
| **Built-in guide** | Top navigation → **How to use** for a six-step tutorial, search example, tips, and privacy notes. |

## Quick start

1. Download or clone this repository.
2. Open **`index.html`** in a modern browser (Chrome, Edge, Firefox, or Safari).
3. Use the **Explorer** menu, or select **How to use** to read the guide.
4. Use the header **EN / বাং** segmented control to change language, and the **moon/sun icon** to switch between light and dark mode.
5. Enter a search, choose columns, add conditions, then click **Export results**.

The page uses **one natural vertical page scroll** instead of independent scrollbars inside the column sidebar and results table. Tables with many visible columns may still scroll horizontally.

The included example dataset is already embedded in `index.html` (**1,000 paper records; 28 fields**). No internet connection is necessary for local exploration. Clicking external DOI/PDF links requires access to their websites.

### বাংলায় শুরু করুন

`index.html` ফাইলটি ব্রাউজারে খুলুন। উপরের ভাষা মেনু থেকে **বাংলা** নির্বাচন করুন। **অনুসন্ধান** মেনুতে গবেষণাপত্র খুঁজতে পারবেন, **ব্যবহারবিধি** অংশে ধাপে ধাপে নির্দেশনা পাবেন। প্রয়োজনীয় কলাম বেছে নিয়ে ফলাফল **এক্সপোর্ট** করুন। **ডার্ক / লাইট** থিমও পরিবর্তন করা যায়।

## How to search

**Keyword search:** Enter `quantum machine learning` to require all three words, or `"quantum machine learning"` to match the entire phrase. Searches are case-insensitive.

**Search scope:** The dropdown beside the search bar supports:

- **Research content**: title, authors, affiliations, abstracts, keywords, IEEE terms, and funding details (where present).
- **All columns**: full dataset search, including IDs, dates, and metadata.
- **Visible columns**: search the columns you selected on the left.
- **Specific field**: search only one column, e.g., `Document Title`.

**Advanced filters:** Expand **Advanced filters**, add a condition, and choose a column, operator, and value. For example, filter `Publication Year` with `number ≥` and value `2024`. When multiple conditions are added, choose **AND** (all must match) or **OR** (at least one must match). The main keyword query is combined with the filter group using AND.

**Column selection:** Choose a preset or toggle fields individually. Sort by clicking a table header; click any paper row for its details. **Export results** includes every matching row (not just the current page) but only the visible columns. Exported headers use the original CSV field names, irrespective of the interface language, to preserve compatibility.

**Keyboard shortcut:** `Ctrl+K` (Windows/Linux) or `Cmd+K` (macOS) focuses search. `Esc` closes the paper-detail panel.

## Update the built-in dataset

Loading a CSV through the interface is **session-only**; it does not edit `index.html`. To change the default dataset deployed from GitHub, run the included Python script:

```bash
python scripts/embed_csv.py path/to/your_export.csv
```

It rewrites the embedded data in `index.html` (UTF-8 CSV, comma delimiter, first row contains headers, unique column names), without changing the original CSV. Commit the updated `index.html` to your repository. It uses Python's standard library and has no dependencies.

> **Important:** The original dataset includes publication metadata and abstracts. Before pushing to a **public** GitHub repository or deploying a public website, confirm you have permission to republish all bundled data. Alternatively, replace it with appropriately licensed records via `embed_csv.py`. Any data embedded in a public `index.html` is publicly retrievable.

## Deploy on GitHub Pages

1. Create a GitHub repository in your account or the [`entangleresearch`](https://github.com/entangleresearch) organization (for example, `csv-by-erl`).
2. Push **`index.html`**, **`README.md`**, **`scripts/`**, and **`assets/`** to the repository's `main` branch.
3. Open **Settings → Pages** in the GitHub repository.
4. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and **`/(root)`**, then save.
5. When GitHub Pages completes deployment, the project URL generally looks like:

   `https://entangleresearch.github.io/csv-by-erl/`

   This URL is an **example**, not an already-published live site; the actual URL depends on your repository name and Pages settings.

You can similarly upload `index.html` to Vercel, Netlify, or any other static web host. No backend environment variables are needed.

## Repository structure

```text
csv-by-erl/
├── index.html             # Standalone website, including default paper records
├── README.md              # Usage, development, and deployment instructions
├── scripts/
│   └── embed_csv.py       # Replace bundled records with a new CSV
└── .gitignore
```

## Data, privacy, and limitations

- Filtering, sorting, rendering, and CSV import/export all run **locally in the browser**. This app does not upload datasets to a server or use tracking scripts.
- The default dataset is **embedded in the HTML page**. It will be available to anyone who can access a deployed copy of `index.html`.
- Imported CSV files remain in browser memory, **not** in the deployed website and **not** in the repository. Reloading the page restores the built-in dataset.
- Display-column, theme, and language settings are stored using browser `localStorage` when permitted. Clearing site data removes the preferences.
- File imports use a comma-delimited CSV parser; embedded newlines, commas, and double-quoted fields are supported. Other encodings and large files may need conversion. Import size limit: **80 MB**.
- Export prefixes cells that resemble spreadsheet formulas to reduce the risk of formula execution in spreadsheet applications. Exports preserve original header names and use UTF-8 with BOM for Excel compatibility.
- The interface can be translated; the source publication content itself is displayed exactly as supplied.
- This is an **independent eRL research utility**. It is not affiliated with or endorsed by IEEE.

## Lab / attribution

Built for **[Entangle Research Lab](https://www.entangleresearch.com/)**, working across AI, computer vision, physical AI, IoT, quantum machine learning, and intelligent systems.

- Website: https://www.entangleresearch.com/
- GitHub organization: https://github.com/entangleresearch

**License:** No blanket software/data license is granted by this package. The lab should choose an appropriate code license and separately verify data redistribution rights before open-source release.
