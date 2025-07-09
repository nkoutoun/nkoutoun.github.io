# Hugo Academic Website Update Handbook

## Overview

This handbook explains how to update your Hugo Academic website hosted on GitHub Pages.

**Your Website:** https://nkoutoun.github.io/  
**Framework:** Hugo with Hugo Blox Builder (Academic CV theme)  
**Hosting:** GitHub Pages  
**Repository:** https://github.com/nkoutoun/nkoutoun.github.io

## Project Structure

```
nkoutoun.github.io/
├── content/                 # Your website content
│   ├── authors/            # Author profiles
│   ├── publication/        # Individual publication pages
│   ├── project/           # Project pages  
│   ├── talk/              # Talk/presentation pages
│   └── _index.md          # Homepage content
├── config/                 # Configuration files
│   ├── _default/          # Default configuration
│   └── params.yaml        # Site parameters
├── assets/                 # CSS, JS, images
├── static/                 # Static files (PDFs, images)
├── layouts/               # HTML templates (rarely modified)
├── public/                # Generated site (auto-generated)
├── resources/             # Hugo cache (auto-generated)
├── go.mod                 # Go module file
├── hugoblox.yaml          # Hugo Blox configuration
└── netlify.toml          # Deployment configuration
```

## Basic Workflow

### 1. Make Changes Locally
- Edit files in `content/`, `config/`, `assets/`, or `static/`
- Test changes locally (optional)
- Commit and push to GitHub

### 2. GitHub Pages Deployment
- GitHub automatically rebuilds your site when you push changes
- Live site updates within 1-2 minutes
- Check GitHub Actions tab for build status

## Common Updates

### Update Personal Information

**File:** `content/authors/admin/_index.md`
```yaml
---
title: Nikolaos Koutounidis
first_name: Nikolaos
last_name: Koutounidis
email: nikolaos.koutounidis@ugent.be
highlight_name: true

# Status emoji
status:
  icon: ☕️

# Organizations/Affiliations
organizations:
  - name: Ghent University
    url: https://www.ugent.be/

# Short bio (displayed in user profile at end of posts)
bio: PhD candidate in Economics focusing on Empirical Macroeconomics...

# Interests to show in About widget
interests:
  - Empirical Macroeconomics
  - Household Consumption & Finance
  - Oil Markets
  - Applied Econometrics

# Education to show in About widget
education:
  courses:
    - course: PhD in Economics
      institution: Ghent University
      year: 2020-Present
    - course: MSc in Economics and Business
      institution: Erasmus University Rotterdam
      year: 2018
---

Your main bio text goes here...
```

### Add a New Publication

**Method 1: Using Hugo Blox Builder (Recommended)**
1. Navigate to `content/publication/`
2. Create a new folder: `your-paper-name/`
3. Create `index.md` in that folder:

```yaml
---
title: 'Your Paper Title'
authors:
  - admin
  - Second Author
date: '2024-01-01'
publishDate: '2024-01-01'
publication_types:
  - article-journal
publication: '*Journal Name*'
abstract: 'Your abstract here...'
url_pdf: 'https://link-to-pdf.com'
url_code: 'https://github.com/your-repo'
url_project: 'https://project-page.com'
featured: true
---
```

**Method 2: Quick Add**
1. Go to `content/publication/`
2. Copy an existing publication folder
3. Rename it and edit the `index.md` file

### Add Working Papers

Similar to publications, but in `content/publication/` with:
```yaml
publication_types:
  - manuscript  # For working papers
```

### Update CV

1. Replace `static/uploads/resume.pdf` with your new CV
2. Or update the link in `content/authors/admin/_index.md`:
```yaml
social:
  - icon: cv
    icon_pack: ai
    link: uploads/resume.pdf
```

### Add News Items

**File:** `content/_index.md`
```yaml
# News section
news:
  - date: '2024-01-15'
    text: 'New paper accepted at Journal of Economics'
  - date: '2024-01-10'
    text: 'Presented at Eastern Economic Association Conference'
```

### Update Contact Information

**File:** `config/_default/params.yaml`
```yaml
# Contact info
contact:
  email: nikolaos.koutounidis@ugent.be
  phone: '+32 9 264 XXXX'
  address:
    street: Sint-Pietersnieuwstraat 25
    city: Ghent
    region: East Flanders
    postcode: '9000'
    country: Belgium
```

### Add Projects

1. Create folder: `content/project/project-name/`
2. Add `index.md`:
```yaml
---
title: Project Title
summary: Brief project description
date: '2024-01-01'
external_link: 'https://project-website.com'
image:
  filename: featured.jpg
---

Detailed project description...
```

### Add Talks/Presentations

1. Create folder: `content/talk/talk-name/`
2. Add `index.md`:
```yaml
---
title: 'Talk Title'
event: 'Conference Name'
event_url: 'https://conference-website.com'
location: 'Conference Location'
date: '2024-01-01'
abstract: 'Talk abstract...'
url_slides: 'slides.pdf'
url_pdf: 'paper.pdf'
---
```

## Site Configuration

### Main Configuration

**File:** `config/_default/config.yaml`
```yaml
title: 'Nikolaos Koutounidis'
baseURL: 'https://nkoutoun.github.io'
```

### Site Parameters

**File:** `config/_default/params.yaml`
```yaml
# Theme
appearance:
  theme_day: minimal
  theme_night: minimal
  font: minimal
  font_size: L

# SEO
marketing:
  seo:
    site_type: Person
    local_business_type: ''
    org_name: ''
    description: 'PhD candidate in Economics at Ghent University'
    twitter: ''
```

### Navigation Menu

**File:** `config/_default/menus.yaml`
```yaml
main:
  - name: Home
    url: '/'
    weight: 10
  - name: Publications
    url: '/publication/'
    weight: 20
  - name: Projects
    url: '/project/'
    weight: 30
  - name: Talks
    url: '/talk/'
    weight: 40
  - name: Contact
    url: '/#contact'
    weight: 60
```

## Working with Git

### Basic Git Commands

```bash
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Update publications"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

### Recommended Workflow

1. **Before making changes:**
   ```bash
   git pull origin main
   ```

2. **After making changes:**
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   git push origin main
   ```

3. **Check build status:**
   - Visit: https://github.com/nkoutoun/nkoutoun.github.io/actions
   - Look for green checkmarks (success) or red X (failure)

## Local Development (Optional)

### Prerequisites
- Hugo Extended (v0.112.0+)
- Go (v1.19+)
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/nkoutoun/nkoutoun.github.io.git
cd nkoutoun.github.io

# Install dependencies
hugo mod get -u ./...

# Start local server
hugo server
```

### Local Testing
- Visit: http://localhost:1313
- Changes auto-reload
- Press Ctrl+C to stop

## Troubleshooting

### Common Issues

**1. Site not updating after push**
- Check GitHub Actions: https://github.com/nkoutoun/nkoutoun.github.io/actions
- Wait 2-3 minutes for build completion
- Clear browser cache (Ctrl+F5)

**2. Build failures**
- Check GitHub Actions for error messages
- Common issues:
  - Invalid YAML syntax
  - Missing required fields
  - Incorrect file paths

**3. Images not showing**
- Images should be in `static/` directory
- Reference as: `![Alt text](image.jpg)`
- Or use `assets/` for processed images

**4. PDF links broken**
- PDFs should be in `static/uploads/`
- Reference as: `url_pdf: uploads/filename.pdf`

### Getting Help

**Hugo Documentation:**
- https://gohugo.io/documentation/
- https://docs.hugoblox.com/

**Common Hugo Commands:**
```bash
hugo help              # Show help
hugo server            # Start local server
hugo server -D         # Include draft content
hugo mod get -u ./...  # Update dependencies
hugo mod clean         # Clean module cache
```

## Best Practices

### Content Management
- Use descriptive file names
- Keep images under 1MB
- Use markdown for formatting
- Preview changes locally when possible

### Git Practices
- Make small, focused commits
- Use descriptive commit messages
- Pull before pushing
- Don't commit generated files (public/, resources/)

### Site Maintenance
- Regular backups (git handles this)
- Check for broken links periodically
- Update Hugo modules occasionally:
  ```bash
  hugo mod get -u ./...
  ```

## Quick Reference

### File Extensions
- `.md` - Markdown content files
- `.yaml` - Configuration files
- `.toml` - Alternative config format
- `.html` - Template files (layouts/)

### Important URLs
- **Live Site:** https://nkoutoun.github.io/
- **Repository:** https://github.com/nkoutoun/nkoutoun.github.io
- **GitHub Actions:** https://github.com/nkoutoun/nkoutoun.github.io/actions
- **Hugo Blox Docs:** https://docs.hugoblox.com/

### Emergency Recovery
If something goes wrong:
1. Check GitHub Actions for error details
2. Revert to last working commit:
   ```bash
   git log --oneline
   git reset --hard <commit-hash>
   git push --force origin main
   ```
3. Contact repository admin for help

---

**Created:** January 2025  
**For:** Nikolaos Koutounidis  
**Website:** https://nkoutoun.github.io/ 