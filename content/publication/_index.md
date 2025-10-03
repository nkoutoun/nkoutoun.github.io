---
title: Publications
cms_exclude: true
type: landing

design:
  spacing: "1rem"

sections:
  # Research Overview Section
  - block: markdown
    content:
      title: Research Note
      text: |
        <div style="font-size: 0.7em; margin-bottom: 20px;">
          My research investigates how aggregate shocks transmit through the economy by combining novel microdata with credible causal identification. A central feature of my work is bridging academic research with industry data, exemplified by a four-year collaboration I established with <a href="https://www.bnpparibasfortis.com/" target="_blank"><strong>BNP Paribas Fortis</strong></a>. This "micro-to-macro" approach has allowed me to analyze the heterogeneous impacts of oil and income shocks, pandemics, and wealth taxation. My work is informed by wide reading across many economic fields, as illustrated by the JEL codes from my research library. Reflecting my particular enjoyment of coding and data visualization, I am committed to producing open-source, replicable work; for instance, I developed an <a href="https://covid-belgium-dashboard.onrender.com" target="_blank">interactive public dashboard</a> visualizing municipal COVID-19 data in Belgium for my first publication.
        </div>
        
        <div style="text-align: center; margin: 20px 0 30px 0;">
          <img src="/media/wordcloud_jel.png" alt="Research Word Cloud JEL" style="max-width: 100%; height: auto; border-radius: 8px;">
          <p style="margin-top: 8px; font-size: 0.8em; color: #666; font-style: italic;">
            A word cloud of JEL codes from my research library
          </p>
        </div>
    design:
      columns: '1'

  # Job Market Paper
  - block: collection
    id: job-market-paper
    content:
      title: Job Market Paper
      filters:
        folders:
          - publication
        featured_only: true
        publication_type: "article"
    design:
      view: citation
      spacing:
        padding: ['20px', '0', '40px', '0']
  
  # Published Papers
  - block: collection
    id: published-papers
    content:
      title: Publications
      filters:
        folders:
          - publication
        exclude_featured: false
        publication_type: "article-journal"
    design:
      view: citation
      spacing:
        padding: ['20px', '0', '40px', '0']
  
  # Work in Progress
  - block: collection
    id: work-in-progress
    content:
      title: Work in Progress
      filters:
        folders:
          - publication
        exclude_featured: true
        publication_type: "article"
    design:
      view: citation
      spacing:
        padding: ['20px', '0', '20px', '0']
---
