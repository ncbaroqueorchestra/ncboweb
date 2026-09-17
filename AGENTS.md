# Repository Guidelines

## Project Overview
- This is the static website for the North Carolina Baroque Orchestra (NCBO), built with Jekyll.
- Site data flows from Airtable through the root-level Python refresh scripts into `_data/*.yml`, then through Jekyll/Liquid templates into static HTML.

## Project Structure & Module Organization
- `index.md`, `about.html`, and other pages are top-level entry points; shared layouts live in `_layouts/`, while reusable snippets sit in `_includes/`.
- Long-form updates belong in `_posts/` (dated Markdown) or `posts/` for evergreen pages; keep supporting data in `_data/` (YAML) so templates can load it.
- Static assets reside in `assets/` (CSS/JS bundles), `img/` (optimized images), and `forms/` for embeddable HTML forms; keep third-party libraries under `node_modules/`.
- Airtable automation scripts (`refresh_event_data.py`, `refresh_donors.py`, and `refresh_board.py`) live at the repository root; deployment helpers live in `bin/`. Avoid mixing site content into utility directories.

## Build, Test, and Development Commands
- `bundle install` — installs the Ruby gems listed in `Gemfile`; rerun after gem updates.
- `bundle exec jekyll serve --livereload` — launches the local dev server at `http://127.0.0.1:4000` and watches for file changes.
- `bundle exec jekyll build` — produces the static site in `_site/`; run before committing to confirm a clean build.
- `npm install` — syncs front-end libraries in `assets/` when package versions change; rarely needed for routine content edits.

## Coding Style & Naming Conventions
- Use 2-space indentation for HTML, Liquid, and YAML blocks; favor readable multiline Liquid tags over dense one-liners.
- Front matter must declare `layout`, `title`, and other template keys; keep keys lowercase with hyphenated names (e.g., `event-date`).
- Name Markdown files with lowercase and hyphens (`ncbo-history.md`), and align image filenames with their referencing post IDs to simplify updates.
- Run `bundle exec jekyll serve` before pushing to catch Liquid or front matter syntax errors early.

## Testing Guidelines
- There is no automated test suite; rely on `bundle exec jekyll build` and manual page review in the dev server.
- Verify navigation, event listings, and data-driven sections against `_data/*.yml` after edits, especially when updating structured content.
- For scripts in `bin/`, execute them in a virtualenv and confirm they refresh the expected YAML files without introducing formatting drift.

## Architecture & Deployment
- `_layouts/home.html` is the primary page layout; `_includes/` contains the reusable event, donor, board, footer, and notice fragments.
- Treat `_data/events.yml`, `_data/past_events.yml`, `_data/donors.yml`, and `_data/board.yml` as generated output. Refresh them with the corresponding Python script instead of hand-editing them.
- GitHub Actions fetches Airtable data and commits the generated YAML to `main`.
- The staging workflow builds and pushes the site to the `staging` branch for `test.ncbaroqueorchestra.org`.
- Production deployment is manually triggered and publishes to the separate `ncboweb-production` repository for `www.ncbaroqueorchestra.org`.

## Commit & Pull Request Guidelines
- Follow the repository’s short, descriptive summary style (e.g., `Update NCBO events`, `Enhance deployment workflow`); keep subject lines under 72 characters.
- Squash or rebase to present a tidy history; link related issues in the PR description and note any data sources or scripts touched.
- Include before/after screenshots for visible UI changes and enumerate manual verification steps (local build, relevant scripts) in the PR checklist.

## Content Refresh & Data Workflow
- When updating data, run `python refresh_donors.py`, `python refresh_event_data.py`, or `python refresh_board.py` from the repo root. These require `AIRTABLE_BASE_ID` and `AIRTABLE_API_KEY`; inspect diffs to ensure YAML keys stay sorted.
- Document external data sources in the PR, and store credentials or API tokens outside the repo—use environment variables or organization secrets instead.
