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
  .news-info {
    display: inline;
    text-decoration: underline dotted;
    text-underline-offset: 3px;
    cursor: help;
    position: relative;
  }
  .news-info:focus-visible {
    outline: none;
  }
  .news-info::after {
    content: attr(data-tooltip);
    display: block;
    position: absolute;
    bottom: calc(100% + 6px);
    left: 50%;
    transform: translateX(-50%);
    width: 380px;
    padding: 6px 10px;
    background: rgba(30, 30, 30, 0.88);
    color: #f0f0f0;
    font-size: 0.78rem;
    font-weight: 400;
    line-height: 1.45;
    border-radius: 5px;
    pointer-events: none;
    white-space: normal;
    text-decoration: none;
    opacity: 0;
    transition: opacity 0.15s ease 0s;
    z-index: 100;
  }
  .news-info:hover::after,
  .news-info:focus-visible::after {
    opacity: 1;
    transition-delay: 0.1s;
  }
  html[data-theme=dark] .news-info::after {
    background: rgba(220, 220, 220, 0.92);
    color: #1a1a1a;
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
