---
layout: page
permalink: /people/
title: people
description: Members of the research group.
nav: true
nav_order: 4
---

<style>
  .people-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 1.5rem; margin: 1rem 0 2.5rem; }
  .person-card { border: 1px solid var(--global-divider-color); border-radius: 0.25rem; overflow: hidden; background: var(--global-card-bg-color); }
  .person-card img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; object-position: center; }
  .person-card-body { padding: 1rem; }
  .person-card h3 { font-size: 1.05rem; margin: 0 0 0.2rem; }
  .person-card .role { color: var(--global-text-color-light); margin-bottom: 0.65rem; }
  .person-card .research-area { border-top: 1px solid var(--global-divider-color); font-size: 0.9rem; margin: 0; padding: 0.7rem 1rem; }
</style>

{% assign sections = "PhD Students,Master Students,Alumni" | split: "," %}
{% for section in sections %}
## {{ section }}

<div class="people-grid">
  {% assign members = site.data.people | where: "section", section %}
  {% for person in members %}
    <article class="person-card">
      <img src="{{ person.photo | relative_url }}" alt="Photo of {{ person.name }}">
      <div class="person-card-body">
        <h3><a href="{{ person.link }}">{{ person.name }}</a></h3>
        <div class="role">{{ person.role }}</div>
      </div>
      <p class="research-area">{{ person.research_area }}</p>
    </article>
  {% endfor %}
</div>
{% endfor %}
