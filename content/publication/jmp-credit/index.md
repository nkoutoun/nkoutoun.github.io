---
title: "The heterogeneous reactions of household credit to income shocks"
authors:
- admin
- "Elena Loutskina"
- "Daniel Murphy"
author_notes:
- ""
- ""
- ""
date: "2026-04-08T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2026-04-08T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
# publication: "Working Paper"
# publication_short: "Job Market Paper"

abstract: >
  We study how household debt portfolios—aggregated at the ZIP code level—respond to local income shocks in the United States. We implement two separate identification strategies: (i) a Bartik-style instrument that shifts local earnings via national industry trends, and (ii) a novel instrument utilizing the timing and location of shale oil and gas well discoveries. Across both designs, positive income shocks are, on average, associated with deleveraging. This average, however, masks a sharp bifurcation in financial behavior. Deleveraging in total credit is driven by financially healthier households—those with higher credit scores, higher incomes, or lower leverage—who restrain the growth of credit-card and auto debt. In contrast, financially vulnerable households often treat the windfall as a gateway to new auto credit while still deleveraging credit-card and typically mortgage debt. Looking at mixed-profile households, we find strong mortgage leveraging among households with high income and high debt or low credit scores. These results show that the same income shock can trigger balance-sheet repair for some households and additional leverage for others—varying by both borrower type and debt category—underscoring substantial underlying heterogeneity and highlighting barriers to broad-based financial stability.

# Summary. An optional shortened abstract.
# summary: 

tags:
- Consumer Credit
- Household Debt
- Heterogeneity
- Income Shocks
- Local Labor Demand
- Job Market Paper

# JEL Classification codes
jel_codes:
- "D14"  # Household Saving; Personal Finance
- "D15"  # Intertemporal Household Choice; Life Cycle Models and Saving
- "G51"  # Household Finance: Household Saving, Borrowing, Debt, and Wealth
- "H31"  # Fiscal Policies and Behavior of Economic Agents: Household

featured: true

# links:
# - name: ""
#   url: ""
url_pdf: 'uploads/jmp_koutounidis.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5861763'
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'Household credit response heterogeneity'
#   focal_point: ""
#   preview_only: true

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

{{< jel "D14, D15, G51, H31" >}}

## Interactive Visualization: Bartik Instrument

The map below shows variation in our Bartik (shift-share) instrument across US counties from 2005 to 2020. The instrument predicts local earnings shocks based on national industry trends weighted by each county's pre-period industry composition.

{{< rawhtml >}}
<div style="position:relative; left:50%; transform:translateX(-50%); width:95vw; max-width:1200px;">
<iframe 
    class="autosize-iframe"
    src="/html/bartik_map.html" 
    width="100%" 
    height="900" 
    frameborder="0"
    scrolling="no"
    style="border:none; border-radius:8px; box-shadow:0 4px 20px rgba(0,0,0,0.12); display:block;">
</iframe>
</div>
{{< /rawhtml >}}

## Interactive Visualization: Credit Response to Local Income Shocks

The heatmaps below summarize how household credit responds to local income shocks across borrower segments and debt categories, revealing the bifurcation between deleveraging and additional borrowing documented in the paper.

{{< rawhtml >}}
<div style="position:relative; left:50%; transform:translateX(-50%); width:95vw; max-width:1200px;">
<iframe 
    class="autosize-iframe"
    src="/html/heatmaps.html" 
    width="100%" 
    height="900" 
    frameborder="0"
    scrolling="no"
    style="border:none; border-radius:8px; box-shadow:0 4px 20px rgba(0,0,0,0.12); display:block;">
</iframe>
</div>

<script>
(function () {
  function autosize(iframe) {
    function neutralizeFlex(doc) {
      if (!doc || !doc.body) return;
      doc.body.style.minHeight = '0';
      doc.body.style.display = 'block';
      doc.documentElement.style.minHeight = '0';
    }
    function measure(doc) {
      if (!doc) return 0;
      var de = doc.documentElement, b = doc.body;
      return Math.max(
        de ? de.scrollHeight : 0,
        de ? de.offsetHeight : 0,
        b ? b.scrollHeight : 0,
        b ? b.offsetHeight : 0
      );
    }
    function update() {
      try {
        var doc = iframe.contentDocument;
        if (!doc) return;
        neutralizeFlex(doc);
        var h = measure(doc);
        if (h > 0) iframe.style.height = h + 'px';
      } catch (e) {}
    }
    iframe.addEventListener('load', function () {
      update();
      try {
        var doc = iframe.contentDocument;
        if (doc && doc.body && 'ResizeObserver' in window) {
          var ro = new ResizeObserver(update);
          ro.observe(doc.body);
          ro.observe(doc.documentElement);
        }
      } catch (e) {}
      // Bundled visualizations unpack asynchronously — keep checking for a while.
      var ticks = 0;
      var t = setInterval(function () {
        update();
        if (++ticks > 60) clearInterval(t); // 30s
      }, 500);
    });
    window.addEventListener('resize', update);
  }
  document.querySelectorAll('iframe.autosize-iframe').forEach(autosize);
})();
</script>
{{< /rawhtml >}}