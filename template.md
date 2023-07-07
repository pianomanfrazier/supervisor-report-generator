## {{ date }}
---

### Accomplished the Following this Week

**Monday** &mdash;

**Tuesday** &mdash;

**Wednesday** &mdash;

**Thursday** &mdash;

**Friday** &mdash;

### Goals for the following week

### Work Travel

### Planned Time Off

- Aug 4, 7 (Friday, Monday) --- Yellowstone trip
- Aug 18 (Friday) --- Fishing trip

### Weekly Commit History

{% for report in reports %}

#### {{ report[0] }}	
{% for line in report[1] %}
{% if line %}
- {{ line }}
{% else %}
No Weekly Commits
{% endif %}
{% endfor %}

{% endfor %}

