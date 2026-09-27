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
  .people-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 1rem 0 2.75rem;
  }
  @media (min-width: 992px) {
    .people-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .people-grid.logo-grid { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  }
  .person-card {
    display: flex;
    flex-direction: column;
    min-height: 11rem;
    border: 1px solid rgba(78, 111, 163, 0.13);
    border-top: 3px solid rgba(78, 111, 163, 0.62);
    border-radius: 0.6rem;
    overflow: hidden;
    background: linear-gradient(145deg, rgba(78, 111, 163, 0.065), rgba(78, 111, 163, 0.025));
    box-shadow: 0 5px 18px rgba(78, 111, 163, 0.07);
    transition: border-color 0.22s ease, box-shadow 0.22s ease, transform 0.22s ease;
  }
  .person-card.logo-card {
    min-height: 0;
    border: none;
    background: #fff;
  }
  .person-card img.logo { width: 100%; aspect-ratio: 4 / 3; object-fit: contain; padding: 1.25rem; }
  .person-card-body {
    padding: 1.15rem 1.2rem 0.9rem;
  }
  .person-card h3 { font-size: 1.08rem; line-height: 1.3; margin: 0; }
  .person-card h3 a {
    color: var(--global-text-color);
    text-decoration: none;
    text-underline-offset: 0.18em;
  }
  .person-card h3 a:hover,
  .person-card h3 a:focus-visible {
    color: var(--global-theme-color);
    text-decoration: underline;
  }
  .person-card .role {
    color: var(--global-text-color-light);
    font-size: 0.78rem;
    font-weight: 400;
    line-height: 1.45;
    margin: 0.55rem 0 0;
  }
  .person-card .role.empty { display: none; }
  .person-card .role .person-supervisor { display: block; white-space: nowrap; }
  .person-card .role a { color: rgba(54, 86, 138, 0.92); font-weight: 500; text-decoration: none; }
  .person-card .role a:hover,
  .person-card .role a:focus-visible { color: rgba(54, 86, 138, 0.92); text-decoration: none; opacity: 0.82; }
  .person-card .research-area {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.6rem;
    align-items: baseline;
    margin: auto 0 0;
    padding: 0.8rem 1.2rem 0.9rem;
    border-top: 1px solid rgba(78, 111, 163, 0.1);
    background: rgba(78, 111, 163, 0.03);
    font-size: 0.82rem;
    line-height: 1.4;
  }
  .person-card .research-area::before {
    content: "Research";
    color: var(--global-text-color-light);
    font-size: 0.67rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  .person-card .research-area.empty {
    display: none;
  }
  .person-card:hover {
    border-color: rgba(78, 111, 163, 0.32);
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(78, 111, 163, 0.13);
  }
  html[data-theme=dark] .person-card {
    background: rgba(122, 159, 196, 0.08);
    border-color: rgba(255, 255, 255, 0.1);
    border-top-color: rgba(122, 159, 196, 0.75);
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.18);
  }
  html[data-theme=dark] .person-card.logo-card {
    background: rgba(255, 255, 255, 0.94);
    border: none;
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

<div class="people-grid{% if section == 'Industry Collaborators' %} logo-grid{% endif %}">
  {% for person in members %}
    <article class="person-card{% if person.logo %} logo-card{% endif %}">
      {% if person.logo and person.photo %}
        <img
          class="logo"
          src="{{ person.photo | relative_url | bust_file_cache }}"
          alt="{{ person.name }} logo"
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
      <p class="research-area{% unless person.research_area %} empty{% endunless %}">
        {% if person.research_area %}{{ person.research_area }}{% endif %}
      </p>
      {% endunless %}
    </article>
  {% endfor %}
</div>
{% endif %}
{% endfor %}
