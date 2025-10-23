---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/cv_koutounidis.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: mathematical-background.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  # - block: collection
  #   id: featured-publications
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #       publication_type: "article-journal"
  #   design:
  #     view: article-grid
  #     columns: 2
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
      title: Publications
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
