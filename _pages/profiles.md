---
layout: page
permalink: /people/
title: People
description: Members of the research group and collaborators.
nav: true
nav_order: 5
---

<style>
  .post-title {
    font-family: 'Libre Baskerville', serif;
    font-weight: 700;
    letter-spacing: 0.01em;
  }
  .post-description {
    font-size: 0.82rem;
    font-variant: small-caps;
    letter-spacing: 0.1em;
    color: rgba(64, 68, 76, 0.92);
    margin: 0.4rem 0 0;
  }
  .post-header {
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 2rem;
  }
  .people-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 1rem; margin: 1rem 0 2.5rem; }
  @media (min-width: 992px) {
    .people-grid { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  }
  .person-card {
    display: flex;
    flex-direction: column;
    border: none;
    border-radius: 0.5rem;
    overflow: hidden;
    background: rgba(78, 111, 163, 0.06);
    box-shadow: 0 4px 20px rgba(78, 111, 163, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.65);
    transition: box-shadow 0.22s ease, transform 0.22s ease;
  }
  .person-card img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; object-position: center; }
  .person-card img.logo { aspect-ratio: 4 / 3; object-fit: contain; padding: 1.25rem; background: #fff; }
  .person-card-body {
    padding: 0.75rem;
    background: transparent;
  }
  .person-card h3 { font-size: 0.95rem; line-height: 1.25; margin: 0; }
  .person-card .role {
    color: var(--global-text-color-light);
    font-size: 0.72rem;
    font-weight: 400;
    line-height: 1.25;
    margin: 0.4rem 0 0;
  }
  .person-card .role.empty { display: none; }
  .person-card .role .person-supervisor { display: block; white-space: nowrap; }
  .person-card .role a { color: rgba(54, 86, 138, 0.92); font-weight: 500; text-decoration: none; }
  .person-card .role a:hover,
  .person-card .role a:focus-visible { color: rgba(54, 86, 138, 0.92); text-decoration: none; opacity: 0.82; }
  .person-card .research-area {
    display: flex;
    flex: 0 0 4rem;
    align-items: flex-start;
    margin: auto 0 0;
    padding: 0.65rem 0.75rem 0.7rem;
    border-top: 1px solid rgba(78, 111, 163, 0.1);
    background: rgba(78, 111, 163, 0.035);
    font-size: 0.8rem;
    line-height: 1.3;
  }
  .person-card:hover {
    transform: translateZ(0) scale(1.03);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
  html[data-theme=dark] .person-card {
    background: rgba(122, 159, 196, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.07);
  }
  html[data-theme=dark] .person-card .research-area {
    border-top-color: rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.025);
  }
  html[data-theme=dark] .person-card:hover {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  }
  h2 { border-left: 4px solid var(--global-theme-color); padding-left: 0.75rem; }
</style>


{% assign sections = "PhD Students,Master Students,Industry Collaborators,Alumni" | split: "," %}
{% for section in sections %}
{% assign members = site.data.people | where: "section", section %}
{% if members.size > 0 %}
## {{ section }}

<div class="people-grid">
  {% for person in members %}
    <article class="person-card">
      {% if person.photo %}
        <img
          class="{% if person.logo %}logo{% endif %}"
          src="{{ person.photo | relative_url | bust_file_cache }}"
          alt="{% if person.logo %}{{ person.name }} logo{% else %}Photo of {{ person.name }}{% endif %}"
          {% if person.photo_position %}style="object-position: {{ person.photo_position }};"{% endif %}
        >
      {% endif %}
      {% unless person.logo %}
      <div class="person-card-body">
        <h3>
          {% if person.link %}
            <a href="{{ person.link | relative_url }}">{{ person.name }}</a>
          {% else %}
            {{ person.name }}
          {% endif %}
        </h3>
        <div class="role{% unless person.supervisor or person.description or person.left or person.joined %} empty{% endunless %}">
          {%- if person.supervisor -%}
            co-supervisor:
            <span class="person-supervisor">
              {%- if person.supervisor_link -%}
                <a href="{{ person.supervisor_link }}">{{ person.supervisor }}</a>
              {%- else -%}
                {{ person.supervisor }}
              {%- endif -%}
            </span>
          {%- elsif person.description -%}
            {{ person.description }}
          {%- elsif person.left -%}
            {{ person.joined }} – {{ person.left }}
          {%- elsif person.joined -%}
            Joined {{ person.joined }}
          {%- endif -%}
        </div>
      </div>
      {% endunless %}
      {% unless person.logo %}
      <p class="research-area"{% unless person.research_area %} aria-hidden="true"{% endunless %}>
        {% if person.research_area %}{{ person.research_area }}{% else %}&nbsp;{% endif %}
      </p>
      {% endunless %}
    </article>
  {% endfor %}
</div>
{% endif %}
{% endfor %}
