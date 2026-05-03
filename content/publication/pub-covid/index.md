---
title: "Assessing the heterogeneous impact of COVID-19 on consumption using bank transactions"
authors:
- "Selien De Schryder"
- admin
- "Koen Schoors"
- "Johannes Weytjens"
author_notes:
- ""
- ""
- ""
- ""
date: "2025-04-13T00:00:00Z"
# doi: "10.1016/j.jmacro.2025.103677"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Macroeconomics, 84*, 103677"
# publication_short: "J. Macroeconomics"



abstract: The transmission of the pandemic shock to the macroeconomy through the prism of consumer heterogeneity is the focal point of this paper. Based on a rich bank account and transactions micro dataset, we assess the roles of local COVID-19 severity, government measures against the spread of the virus, and vaccination rates for households’ consumption behavior in Belgium. We find that households living in areas that experienced high COVID-19 positivity rates and more stringent containment measures, decreased their consumption more. The relevance of these effects, however, shifted over the course of the pandemic. Higher local vaccination rates significantly counteracted these negative impacts on household consumption. Furthermore, our study highlights that the impact of these factors on consumption varied distinctly across households with different income, liquid wealth, and age characteristics.

# Summary. An optional shortened abstract.
summary: This paper uses detailed bank transaction data to examine how COVID-19 affected household consumption patterns, revealing significant heterogeneity across demographic groups.

tags:
- COVID-19
- Pandemic
- Lockdown
- Transactions data
- Heterogeneity

featured: false

links:
- name: "Interactive Dashboard"
  url: '/html/covid_belgium_dashboard.html'
  icon: chart-bar
  icon_pack: fas
url_pdf: ''
url_code: 'https://github.com/nkoutoun/covid_paper'
url_dataset: 'https://github.com/nkoutoun/covid_paper/tree/main/data'
url_poster: ''
url_project: ''
url_slides: ''
url_source: 'https://www.sciencedirect.com/science/article/abs/pii/S016407042500014X'
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'Figure: Rolling window estimation. Evolution of cases-to-tests and stringency index parameters over time. The dark gray-shaded areas indicate the periods of the seven COVID-19 waves, and the light gray-shaded areas signify the two periods between waves.'
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

{{< jel "E21, E32, D12, I18" >}}

<!-- # Static Image
<div style="margin-bottom: 1rem;">
<img src="covid-figure.png" alt="Rolling window estimation" style="width: 100%; margin-bottom: 0;">
<p style="font-style: italic; text-align: left; margin-top: 0; margin-bottom: 0; color: #6b7280; font-size: 0.875rem;"><strong>Figure:</strong> Rolling window estimation. Evolution of cases-to-tests and stringency index parameters over time. The dark gray-shaded areas indicate the periods of the seven COVID-19 waves, and the light gray-shaded areas signify the two periods between waves.</p>
</div> -->

## Interactive Dashboard

Explore the data interactively with the COVID-19 Belgium dashboard:

<div style="position:relative; left:50%; transform:translateX(-50%); width:95vw; max-width:1200px;">
<iframe class="autosize-iframe"
        src="/html/covid_belgium_dashboard.html"
        width="100%" 
        height="900" 
        scrolling="no"
        style="border: 1px solid #e5e7eb; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); display:block;"
        title="COVID-19 Belgium Consumption Dashboard">
</iframe>
<p style="font-style: italic; text-align: center; margin-top: 0.5rem; color: #6b7280; font-size: 0.875rem;">
<strong>Interactive Dashboard:</strong> Explore the heterogeneous impact of COVID-19 on consumption patterns across Belgian households.
</p>
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
      var ticks = 0;
      var t = setInterval(function () {
        update();
        if (++ticks > 60) clearInterval(t);
      }, 500);
    });
    window.addEventListener('resize', update);
  }
  document.querySelectorAll('iframe.autosize-iframe').forEach(autosize);
})();
</script>

<!-- This research provides novel insights into the heterogeneous economic effects of the COVID-19 pandemic using granular household-level transaction data. The findings have important implications for understanding crisis responses and designing targeted policy interventions.

## Key Findings

1. **Heterogeneous Responses**: Consumption impacts varied significantly across demographic groups
2. **Sectoral Differences**: Contact-intensive sectors experienced larger declines
3. **Age Effects**: Younger households showed more pronounced consumption reductions
4. **Policy Implications**: Results inform targeted support measure design

## Data and Methodology

The analysis leverages a unique dataset from a major Belgian bank covering:
- Over 200,000 households
- Detailed transaction-level data
- Full pandemic period coverage
- Granular spending category information

{{% callout note %}}
This paper represents collaborative research between Ghent University and BNP Paribas Fortis.
{{% /callout %}}  -->