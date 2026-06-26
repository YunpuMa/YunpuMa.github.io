---
layout: page
title: News
permalink: /news/
description: Selected news from the group.
nav: true
nav_order: 2
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
    color: var(--global-text-color-light);
    margin: 0.4rem 0 0;
  }
  .post-header {
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 2rem;
  }
  .news table th {
    color: rgba(78, 111, 163, 0.72);
    font-size: 0.9rem;
    font-weight: 500;
    line-height: 1.45;
  }
  html[data-theme=dark] .news table th {
    color: rgba(124, 160, 197, 0.78);
  }
</style>

<div class="news">
  <div class="table-responsive">
    <table class="table table-sm table-borderless">
      {% assign news_items = site.news | sort: "date" | reverse %}
      {% for item in news_items %}
        <tr>
          <th scope="row" style="width: 20%">
            {{ item.date | date: "%b %Y" }}
          </th>
          <td>{{ item.content | markdownify }}</td>
        </tr>
      {% endfor %}
    </table>
  </div>
</div>
