---
title: Teaching
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
  # Teaching Note Section
  - block: markdown
    content:
      title: Teaching Note
      text: |
        <div style="font-size: 0.7em; margin-bottom: 20px;">
          My teaching philosophy is built on bridging economic theory with real-world policy and equipping students with modern computational tools. As a teaching assistant at Ghent University, I draw on my experience at the European Central Bank to transform the classroom into a dynamic policy-briefing environment. I develop open-source tools, including a <a href="https://www.nikolaoskoutounidis.com/teaching/ecb-rates/" target="_blank" rel="noopener">Python application</a> that allows students to programmatically analyze official ECB data, turning abstract concepts into hands-on skills. Ultimately, I aim to empower students to not just consume research, but to produce it, mentoring them through the entire research pipeline to become independent thinkers.
        </div>
    design:
      columns: '1'

  # My Courses Section
  - block: markdown
    content:
      title: Courses
      text: |
        <div style="font-size: 0.85em;">
          As part of my role as Assistant Academic Personnel at Ghent University, I have served as a teaching assistant for the following courses:
        </div>
        
        <div style="font-size: 0.85em; margin-top: 20px;">
          <p style="margin-bottom: 20px;">
            <strong>2022-25 Teaching Assistant</strong>, Ghent University<br>
            <a href="https://studiekiezer.ugent.be/2024/studiefiche/en/F000568" target="_blank">Monetary Policy</a> (Master level)<br>
            <em>Instructors: Prof. Gert Peersman, Prof. Selien De Schryder</em>
          </p>
          <p style="margin-bottom: 20px;">
            <strong>2021-25 Teaching Assistant</strong>, Ghent University<br>
            <a href="https://studiekiezer.ugent.be/2024/studiefiche/en/F000946" target="_blank">Monetary Economics</a> (Master level)<br>
            <em>Instructor: Prof. Selien De Schryder</em>
          </p>
          <p style="margin-bottom: 20px;">
            <strong>2021 Teaching Assistant</strong>, Ghent University<br>
            International Financial Management (Master level)<br>
            <em>Instructor: Prof. Martien Lammers</em>
          </p>
        </div>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['20px', '0', '40px', '0']

  # Interactive Teaching Material Section
  - block: collection
    id: interactive-materials
    content:
      title: Interactive Teaching Material
      filters:
        folders:
          - teaching
    design:
      view: article-grid
      fill_image: false
      columns: 2
      spacing:
        padding: ['20px', '0', '20px', '0']
---
