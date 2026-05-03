---
title: Code
cms_exclude: true
type: landing

cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true

design:
  spacing: "1rem"

sections:
  # Intro Section
  - block: markdown
    content:
      title: Open-Source Software
      text: |
        <div style="font-size: 0.7em; margin-bottom: 20px;">
          I develop and maintain open-source tools that make modern econometric methods easier to use in empirical research. Each package is designed to be lightweight, well-documented, and reproducible, so that fellow researchers and students can apply the same techniques I use in my own work.
        </div>
    design:
      columns: '1'

  # Packages Section
  - block: collection
    id: packages
    content:
      title: Packages
      filters:
        folders:
          - code
    design:
      view: article-grid
      fill_image: false
      columns: 2
      spacing:
        padding: ['20px', '0', '20px', '0']
---
