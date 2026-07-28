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
    top: calc(100% + 6px);
    left: 50%;
    transform: translateX(-50%);
    width: min(380px, calc(100vw - 2rem));
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
    z-index: 1050;
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
  .news-media-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    border: 0;
    background: transparent;
    color: var(--global-theme-color);
    font-size: 1rem;
    line-height: 1;
    cursor: pointer;
  }
  .news-media-toggle:hover,
  .news-media-toggle:focus-visible {
    color: var(--global-theme-color);
  }
  .news-media {
    display: grid;
    grid-template-rows: 0fr;
    opacity: 0;
    transition:
      grid-template-rows 240ms ease,
      opacity 180ms ease,
      margin-top 240ms ease;
    margin-top: 0;
  }
  .news-media.is-open {
    grid-template-rows: 1fr;
    opacity: 1;
    margin-top: 0.85rem;
  }
  .news-media-inner {
    overflow: hidden;
  }
  .news-media img {
    display: block;
    width: min(100%, 560px);
    height: auto;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
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

<script>
  document.querySelectorAll(".news-media-toggle").forEach((button) => {
    const media = document.getElementById(button.getAttribute("aria-controls"));

    if (!media) return;

    button.addEventListener("click", () => {
      const isOpen = media.classList.toggle("is-open");

      button.setAttribute("aria-expanded", String(isOpen));
      button.setAttribute("aria-label", `${isOpen ? "Hide" : "Show"} image for BAY.AI PI Meeting`);
    });
  });
</script>
