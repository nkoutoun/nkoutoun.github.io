---
title: Publications
cms_exclude: true
type: landing

design:
  spacing: "2rem"

sections:
  - block: collection
    id: job-market-paper
    content:
      title: Job Market Paper
      text: ""
      filters:
        folders:
          - publication
        featured_only: true
        publication_type: "article"
    design:
      view: citation
  - block: collection
    id: published-papers
    content:
      title: Published Papers
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: false
        publication_type: "article-journal"
    design:
      view: citation
  - block: collection
    id: work-in-progress
    content:
      title: Work in Progress
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: true
        publication_type: "article"
    design:
      view: citation
---
