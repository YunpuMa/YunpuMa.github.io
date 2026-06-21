---
layout: page
permalink: /publications/
title: publications
description: Selected research publications.
nav: true
nav_order: 3
---

For the full list, see my [Google Scholar page]({{ site.google_scholar_url }}).

<style>
  .publications .links { display: flex; gap: 0.25rem; }
  .publications .links .bibtex { order: 2; }
</style>

{% include bib_search.liquid %}

<div class="publications">
{% bibliography %}
</div>
