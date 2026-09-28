---
layout: page
permalink: /people/
title: People
description: Members of the research group and collaborators.
nav: true
nav_order: 5
---

<style>
  .people-list {
    list-style: none;
    margin: 0 0 2.5rem;
    padding: 0;
  }
  .people-list li {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 0.35rem 1.25rem;
    padding: 0.8rem 0;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .people-list .person-name {
    min-width: 12rem;
    font-weight: 600;
  }
  .people-list a {
    color: var(--global-theme-color);
  }
  .people-list .person-meta {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
  }
  .people-list .person-research {
    margin-left: auto;
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    text-align: right;
  }
  .industry-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    margin: 1rem 0 2.75rem;
  }
  .industry-card {
    overflow: hidden;
    border-radius: 0.6rem;
    background: #fff;
  }
  .industry-card img {
    display: block;
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: contain;
    padding: 1.25rem;
  }
  @media (min-width: 992px) {
    .industry-grid { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  }
  html[data-theme=dark] .industry-card {
    background: rgba(255, 255, 255, 0.94);
  }
  @media (max-width: 640px) {
    .people-list .person-research {
      width: 100%;
      margin-left: 0;
      text-align: left;
    }
  }
  h2 { border-left: 4px solid var(--global-theme-color); padding-left: 0.75rem; }
</style>


{% assign sections = "PhD Students,Master Students,Industry Collaborators,Alumni" | split: "," %}
{% for section in sections %}
{% assign members = site.data.people | where: "section", section %}
{% if members.size > 0 %}
## {{ section }}

{% if section == 'Industry Collaborators' %}
<div class="industry-grid">
  {% for person in members %}
    <article class="industry-card">
      {% if person.photo %}
        <img
          src="{{ person.photo | relative_url | bust_file_cache }}"
          alt="{{ person.name }} logo"
        >
      {% endif %}
    </article>
  {% endfor %}
</div>
{% else %}
<ul class="people-list">
  {% for person in members %}
    <li>
      <span class="person-name">
        {% if person.link %}
          <a href="{{ person.link | relative_url }}">{{ person.name }}</a>
        {% else %}
          {{ person.name }}
        {% endif %}
      </span>
      {% if person.joined or person.left %}
        <span class="person-meta">{{ person.joined }}{% if person.joined and person.left %} – {% endif %}{{ person.left }}</span>
      {% endif %}
      {% if person.research_area %}
        <span class="person-research">{{ person.research_area }}</span>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% endif %}
{% endif %}
{% endfor %}
