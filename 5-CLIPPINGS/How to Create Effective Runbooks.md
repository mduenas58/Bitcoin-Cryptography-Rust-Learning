---
title: "How to Create Effective Runbooks"
source: "https://oneuptime.com/blog/post/2026-02-02-effective-runbooks/view"
author:
  - "[[Nawaz Dhandala]]"
published: 2026-02-01
created: 2026-04-12
description: "A complete guide to creating runbooks that reduce incident response time, including templates, automation strategies, and real-world examples for common operational scenarios."
tags:
  - "clippings"
---
---

Every minute during an incident costs money, reputation, and team morale. Runbooks are your first line of defense against prolonged outages. They transform chaos into structured response, enabling any engineer to resolve issues quickly, even at 3 AM when the original system author is unavailable.

This guide walks you through creating runbooks that actually work. Not the kind that gather dust in a wiki, but living documents that your team reaches for during every incident.

## What is a Runbook?

A runbook is a documented procedure for completing a specific operational task. Unlike general documentation, runbooks are action-oriented. They guide an operator through a series of steps to achieve a defined outcome.

<svg id="mermaid-1776012253110" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="max-width: 1295px;" viewBox="-8 -8 1295 55" role="graphics-document document" aria-roledescription="flowchart-v2"><g><marker id="mermaid-1776012253110_flowchart-pointEnd" viewBox="0 0 10 10" refX="6" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253110_flowchart-pointStart" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253110_flowchart-circleEnd" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-1776012253110_flowchart-circleStart" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-1776012253110_flowchart-crossEnd" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253110_flowchart-crossStart" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><g><g></g><g><path d="M91.32,19.5L95.487,19.5C99.654,19.5,107.987,19.5,115.437,19.5C122.887,19.5,129.454,19.5,132.737,19.5L136.02,19.5" id="L-A-B-0" style="fill:none;" marker-end="url(#mermaid-1776012253110_flowchart-pointEnd)" stroke="currentColor"></path><path d="M347.016,19.5L351.182,19.5C355.349,19.5,363.682,19.5,371.132,19.5C378.582,19.5,385.149,19.5,388.432,19.5L391.716,19.5" id="L-B-C-0" style="fill:none;" marker-end="url(#mermaid-1776012253110_flowchart-pointEnd)" stroke="currentColor"></path><path d="M657.594,19.5L661.76,19.5C665.927,19.5,674.26,19.5,681.71,19.5C689.16,19.5,695.727,19.5,699.01,19.5L702.294,19.5" id="L-C-D-0" style="fill:none;" marker-end="url(#mermaid-1776012253110_flowchart-pointEnd)" stroke="currentColor"></path><path d="M872.313,19.5L876.479,19.5C880.646,19.5,888.979,19.5,896.429,19.5C903.879,19.5,910.446,19.5,913.729,19.5L917.013,19.5" id="L-D-E-0" style="fill:none;" marker-end="url(#mermaid-1776012253110_flowchart-pointEnd)" stroke="currentColor"></path><path d="M1063.953,19.5L1068.12,19.5C1072.286,19.5,1080.62,19.5,1088.07,19.5C1095.52,19.5,1102.086,19.5,1105.37,19.5L1108.653,19.5" id="L-E-F-0" style="fill:none;" marker-end="url(#mermaid-1776012253110_flowchart-pointEnd)" stroke="currentColor"></path></g><g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g></g><g><g id="flowchart-A-0" data-node="true" data-id="A" transform="translate(45.66015625, 19.5)"><rect style="" rx="0" ry="0" x="-45.66015625" y="-19.5" width="91.3203125" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-38.16015625, -12)"><rect></rect><foreignObject width="76.3203125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Alert Fires</div></foreignObject></g></g><g id="flowchart-B-1" data-node="true" data-id="B" transform="translate(244.16796875, 19.5)"><rect style="" rx="0" ry="0" x="-102.84765625" y="-19.5" width="205.6953125" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-95.34765625, -12)"><rect></rect><foreignObject width="190.6953125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Operator Opens Runbook</div></foreignObject></g></g><g id="flowchart-C-3" data-node="true" data-id="C" transform="translate(527.3046875, 19.5)"><rect style="" rx="0" ry="0" x="-130.2890625" y="-19.5" width="260.578125" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-122.7890625, -12)"><rect></rect><foreignObject width="245.578125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Follow Step-by-Step Instructions</div></foreignObject></g></g><g id="flowchart-D-5" data-node="true" data-id="D" transform="translate(789.953125, 19.5)"><rect style="" rx="0" ry="0" x="-82.359375" y="-19.5" width="164.71875" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-74.859375, -12)"><rect></rect><foreignObject width="149.71875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Execute Commands</div></foreignObject></g></g><g id="flowchart-E-7" data-node="true" data-id="E" transform="translate(993.1328125, 19.5)"><rect style="" rx="0" ry="0" x="-70.8203125" y="-19.5" width="141.640625" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-63.3203125, -12)"><rect></rect><foreignObject width="126.640625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Verify Resolution</div></foreignObject></g></g><g id="flowchart-F-9" data-node="true" data-id="F" transform="translate(1196.4765625, 19.5)"><rect style="" rx="0" ry="0" x="-82.5234375" y="-19.5" width="165.046875" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-75.0234375, -12)"><rect></rect><foreignObject width="150.046875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Document Outcome</div></foreignObject></g></g></g></g></g></svg>

Runbooks differ from other documentation types:

| Document Type | Purpose | When Used |
| --- | --- | --- |
| Runbook | Step-by-step operational procedure | During incidents or routine operations |
| Playbook | Strategic guidance for scenarios | Planning and decision-making |
| Wiki Page | General knowledge and context | Learning and onboarding |
| README | Project overview and setup | Development and deployment |

## Types of Runbooks You Need

Organizations typically need runbooks in four categories.

### Diagnostic Runbooks

These help operators investigate and identify the root cause of an issue. They do not fix the problem directly but guide the investigation process.

<svg id="mermaid-1776012253195" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="max-width: 828.1015625px;" viewBox="-8 -8 828.1015625 1091.0859375" role="graphics-document document" aria-roledescription="flowchart-v2"><g><marker id="mermaid-1776012253195_flowchart-pointEnd" viewBox="0 0 10 10" refX="6" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253195_flowchart-pointStart" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253195_flowchart-circleEnd" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-1776012253195_flowchart-circleStart" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-1776012253195_flowchart-crossEnd" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253195_flowchart-crossStart" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><g><g></g><g><path d="M412.912,39L412.912,43.167C412.912,47.333,412.912,55.667,412.978,63.2C413.044,70.734,413.176,77.467,413.242,80.834L413.308,84.201" id="L-A-B-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M413.412,252.117L413.329,256.201C413.245,260.284,413.079,268.451,413.061,275.901C413.044,283.351,413.176,290.085,413.242,293.451L413.308,296.818" id="L-B-C-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M361.988,385.772L314.879,400.426C267.77,415.08,173.551,444.387,126.441,478.836C79.332,513.285,79.332,552.875,79.332,592.465C79.332,632.055,79.332,671.645,79.332,708.01C79.332,744.376,79.332,777.518,79.332,810.66C79.332,843.802,79.332,876.944,79.332,898.798C79.332,920.653,79.332,931.219,79.332,936.503L79.332,941.786" id="L-C-D-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M449.455,401.153L463.302,413.243C477.149,425.334,504.844,449.514,518.763,466.972C532.682,484.429,532.825,495.162,532.897,500.529L532.968,505.896" id="L-C-E-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M480.458,622.154L453.479,637C426.501,651.847,372.543,681.541,345.565,712.959C318.586,744.376,318.586,777.518,318.586,810.66C318.586,843.802,318.586,876.944,318.586,898.798C318.586,920.653,318.586,931.219,318.586,936.503L318.586,941.786" id="L-E-F-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M573.8,633.973L586.599,646.85C599.398,659.727,624.996,685.481,637.866,703.724C650.737,721.968,650.88,732.701,650.952,738.068L651.023,743.435" id="L-E-G-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M620.445,842.937L609.486,854.128C598.528,865.32,576.612,887.703,565.654,904.178C554.695,920.653,554.695,931.219,554.695,936.503L554.695,941.786" id="L-G-H-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M681.743,842.937L692.535,854.128C703.326,865.32,724.909,887.703,735.701,904.178C746.492,920.653,746.492,931.219,746.492,936.503L746.492,941.786" id="L-G-I-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M79.332,986.086L79.332,990.253C79.332,994.419,79.332,1002.753,124.507,1012.545C169.682,1022.338,260.032,1033.591,305.206,1039.217L350.381,1044.843" id="L-D-J-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M318.586,986.086L318.586,990.253C318.586,994.419,318.586,1002.753,328.813,1010.774C339.04,1018.796,359.495,1026.506,369.722,1030.361L379.949,1034.217" id="L-F-J-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M554.695,986.086L554.695,990.253C554.695,994.419,554.695,1002.753,544.468,1010.774C534.241,1018.796,513.786,1026.506,503.559,1030.361L493.332,1034.217" id="L-H-J-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path><path d="M746.492,986.086L746.492,990.253C746.492,994.419,746.492,1002.753,709.225,1012.272C671.957,1021.79,597.422,1032.495,560.154,1037.847L522.887,1043.2" id="L-I-J-0" style="fill:none;" marker-end="url(#mermaid-1776012253195_flowchart-pointEnd)" stroke="currentColor"></path></g><g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g transform="translate(79.33203125, 711.234375)"><g transform="translate(-13.56640625, -12)"><foreignObject width="27.1328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Yes</div></foreignObject></g></g><g transform="translate(532.5390625, 473.6953125)"><g transform="translate(-10.7421875, -12)"><foreignObject width="21.484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">No</div></foreignObject></g></g><g transform="translate(318.5859375, 810.66015625)"><g transform="translate(-13.56640625, -12)"><foreignObject width="27.1328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Yes</div></foreignObject></g></g><g transform="translate(650.59375, 711.234375)"><g transform="translate(-10.7421875, -12)"><foreignObject width="21.484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">No</div></foreignObject></g></g><g transform="translate(554.6953125, 910.0859375)"><g transform="translate(-13.56640625, -12)"><foreignObject width="27.1328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Yes</div></foreignObject></g></g><g transform="translate(746.4921875, 910.0859375)"><g transform="translate(-10.7421875, -12)"><foreignObject width="21.484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">No</div></foreignObject></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g></g><g><g id="flowchart-A-10" data-node="true" data-id="A" transform="translate(412.912109375, 19.5)"><rect style="" rx="0" ry="0" x="-81.98046875" y="-19.5" width="163.9609375" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-74.48046875, -12)"><rect></rect><foreignObject width="148.9609375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Symptom Observed</div></foreignObject></g></g><g id="flowchart-B-11" data-node="true" data-id="B" transform="translate(412.912109375, 170.30859375)"><polygon points="81.30859375,0 162.6171875,-81.30859375 81.30859375,-162.6171875 0,-81.30859375" transform="translate(-81.30859375,81.30859375)" style="" fill="none" stroke="currentColor"></polygon><g style="" transform="translate(-54.30859375, -12)"><rect></rect><foreignObject width="108.6171875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Check Metrics</div></foreignObject></g></g><g id="flowchart-C-13" data-node="true" data-id="C" transform="translate(412.912109375, 369.15625)"><polygon points="67.5390625,0 135.078125,-67.5390625 67.5390625,-135.078125 0,-67.5390625" transform="translate(-67.5390625,67.5390625)" style="" fill="none" stroke="currentColor"></polygon><g style="" transform="translate(-40.5390625, -12)"><rect></rect><foreignObject width="81.078125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">CPU High?</div></foreignObject></g></g><g id="flowchart-D-15" data-node="true" data-id="D" transform="translate(79.33203125, 966.5859375)"><rect style="" rx="0" ry="0" x="-79.33203125" y="-19.5" width="158.6640625" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-71.83203125, -12)"><rect></rect><foreignObject width="143.6640625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Check Process List</div></foreignObject></g></g><g id="flowchart-E-17" data-node="true" data-id="E" transform="translate(532.5390625, 592.46484375)"><polygon points="81.76953125,0 163.5390625,-81.76953125 81.76953125,-163.5390625 0,-81.76953125" transform="translate(-81.76953125,81.76953125)" style="" fill="none" stroke="currentColor"></polygon><g style="" transform="translate(-54.76953125, -12)"><rect></rect><foreignObject width="109.5390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Memory High?</div></foreignObject></g></g><g id="flowchart-F-19" data-node="true" data-id="F" transform="translate(318.5859375, 966.5859375)"><rect style="" rx="0" ry="0" x="-109.921875" y="-19.5" width="219.84375" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-102.421875, -12)"><rect></rect><foreignObject width="204.84375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Check Memory Consumers</div></foreignObject></g></g><g id="flowchart-G-21" data-node="true" data-id="G" transform="translate(650.59375, 810.66015625)"><polygon points="62.42578125,0 124.8515625,-62.42578125 62.42578125,-124.8515625 0,-62.42578125" transform="translate(-62.42578125,62.42578125)" style="" fill="none" stroke="currentColor"></polygon><g style="" transform="translate(-35.42578125, -12)"><rect></rect><foreignObject width="70.8515625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Disk Full?</div></foreignObject></g></g><g id="flowchart-H-23" data-node="true" data-id="H" transform="translate(554.6953125, 966.5859375)"><rect style="" rx="0" ry="0" x="-76.1875" y="-19.5" width="152.375" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-68.6875, -12)"><rect></rect><foreignObject width="137.375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Check Disk Usage</div></foreignObject></g></g><g id="flowchart-I-25" data-node="true" data-id="I" transform="translate(746.4921875, 966.5859375)"><rect style="" rx="0" ry="0" x="-65.609375" y="-19.5" width="131.21875" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-58.109375, -12)"><rect></rect><foreignObject width="116.21875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Check Network</div></foreignObject></g></g><g id="flowchart-J-27" data-node="true" data-id="J" transform="translate(436.640625, 1055.5859375)"><rect style="" rx="0" ry="0" x="-81" y="-19.5" width="162" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-73.5, -12)"><rect></rect><foreignObject width="147" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Identify Root Cause</div></foreignObject></g></g></g></g></g></svg>

### Remediation Runbooks

These provide specific steps to fix known issues. When an alert fires, the corresponding remediation runbook tells the operator exactly what to do.

### Deployment Runbooks

These guide operators through deployment procedures, rollbacks, and release verification. They are especially important for systems that cannot use fully automated deployments.

### Maintenance Runbooks

These cover routine operational tasks like certificate rotation, database maintenance, backup verification, and capacity planning procedures.

## Essential Components of Every Runbook

Every effective runbook contains these core sections. Consistency across runbooks helps operators find information quickly during high-pressure situations.

### Metadata Header

Start every runbook with essential metadata that helps operators quickly determine if they have the right document.

The following metadata header example shows the critical information every runbook needs at the top.

```yaml
YAML---
title: Database Primary Failover
id: RB-DB-001
version: 2.3.0
last_updated: 2026-01-28
last_tested: 2026-01-15
owner: Database Team
slack_channel: "#database-incidents"
pagerduty_service: database-primary
estimated_duration: 15-30 minutes
risk_level: high
requires_approval: true
---
```

### Trigger Conditions

Clearly define when this runbook should be used. Include alert names, error messages, and observable symptoms.

The trigger conditions section helps operators quickly determine if this runbook matches their situation.

```markdown
Markdown## When to Use This Runbook

### Triggering Alerts
- \`DatabasePrimaryUnreachable\` - PagerDuty
- \`ReplicationLagCritical\` - Prometheus
- \`ConnectionPoolExhausted\` - Application logs

### Observable Symptoms
- Application returns 500 errors on write operations
- Read replicas show increasing replication lag
- Connection timeouts in application logs

### When NOT to Use
- If only read replicas are affected, see RB-DB-002
- If the issue is network-related, see RB-NET-001
- If this is a planned maintenance, see RB-DB-010
```

### Prerequisites

List everything the operator needs before starting. Access requirements, tools, and preliminary checks all belong here.

This prerequisite checklist ensures operators have everything needed before beginning the procedure.

```markdown
Markdown## Prerequisites

### Required Access
- [ ] SSH access to database servers (verify: \`ssh db-primary-01.prod\`)
- [ ] Database admin credentials (stored in Vault at \`secret/database/admin\`)
- [ ] Access to failover dashboard at https://internal.example.com/db-failover

### Required Tools
- [ ] psql client installed
- [ ] kubectl configured for production cluster
- [ ] Vault CLI authenticated

### Pre-Flight Checks
- [ ] Confirm incident channel is open: #database-incidents
- [ ] Notify incident commander: @oncall-ic
- [ ] Verify current replication status before proceeding
```

### Step-by-Step Procedure

This is the core of your runbook. Each step must be specific, executable, and verifiable.

The following example demonstrates how to structure individual steps with commands, expected output, and error handling.

```markdown
Markdown## Procedure

### Step 1: Assess Current State

Check the replication status on the primary database. This determines if failover is necessary.

Run this command to check replication health:

\`\`\`bash
## Connect to primary and check replication status
psql -h db-primary-01.prod.internal -U admin -d postgres -c \
  "SELECT client_addr, state, sent_lsn, write_lsn,
   flush_lsn, replay_lsn,
   pg_wal_lsn_diff(sent_lsn, replay_lsn) AS replication_lag_bytes
   FROM pg_stat_replication;"
\`\`\`bash

**Expected Output (Healthy):**
\`\`\`text
 client_addr  |   state   | replication_lag_bytes
--------------+-----------+----------------------
 10.0.1.52    | streaming |                 1024
 10.0.1.53    | streaming |                  512
\`\`\`bash

**Expected Output (Problem):**
\`\`\`text
 client_addr  |   state    | replication_lag_bytes
--------------+------------+----------------------
 10.0.1.52    | catchup    |            104857600
 10.0.1.53    | startup    |                    0
\`\`\`bash

**If replication_lag_bytes exceeds 100MB:** Proceed to Step 2.
**If all replicas show state='streaming' with low lag:** Investigate other causes before failover.

### Step 2: Initiate Controlled Failover

Stop writes to the primary to allow replicas to catch up.

Run this command to prevent new connections to the primary:

\`\`\`bash
## Block new connections to primary
psql -h db-primary-01.prod.internal -U admin -d postgres -c \
  "ALTER SYSTEM SET max_connections = 0;"

## Reload configuration
psql -h db-primary-01.prod.internal -U admin -d postgres -c \
  "SELECT pg_reload_conf();"
\`\`\`bash

**Expected Output:**
\`\`\`text
ALTER SYSTEM
 pg_reload_conf
----------------
 t
\`\`\`bash

Wait 30 seconds for existing transactions to complete.

### Step 3: Promote Standby to Primary

Execute the promotion command on the standby server designated for failover.

SSH into the standby and run the promotion command:

\`\`\`bash
## Connect to standby server
ssh admin@db-standby-01.prod.internal

## Promote standby to primary
sudo -u postgres pg_ctl promote -D /var/lib/postgresql/14/main
\`\`\`bash

**Expected Output:**
\`\`\`text
waiting for server to promote.... done
server promoted
\`\`\`bash

**If you see "server is not in standby mode":**
The server may have already been promoted. Verify with:

\`\`\`bash
psql -c "SELECT pg_is_in_recovery();"
\`\`\`bash

Returns \`f\` for primary, \`t\` for standby.
\`\`\`text

### Verification Steps

After completing the procedure, verify success with specific checks.

These verification steps confirm the procedure completed successfully and the system is functioning correctly.

\`\`\`markdown
## Verification

### Immediate Verification (within 5 minutes)

1. **Verify new primary accepts writes:**

\`\`\`bash
psql -h db-primary-02.prod.internal -U admin -d postgres -c \
  "CREATE TABLE failover_test_$(date +%s) (id int);
   DROP TABLE failover_test_$(date +%s);"
\`\`\`bash

Expected: Query completes without error.

2. **Verify application connectivity:**

\`\`\`bash
curl -s https://api.example.com/health | jq '.database'
\`\`\`bash

Expected: \`"status": "connected"\`

3. **Verify monitoring shows healthy state:**

Check Grafana dashboard: https://grafana.example.com/d/database-health

### Extended Verification (within 30 minutes)

- [ ] Replication established to remaining standbys
- [ ] Application error rate returned to baseline
- [ ] No customer reports of data issues
\`\`\`text

### Escalation Paths

Define when and how to escalate if the runbook does not resolve the issue.

The escalation section ensures operators know when to seek additional help.

\`\`\`markdown
## Escalation

### Escalate Immediately If:
- Failover does not complete within 30 minutes
- Data inconsistency detected between old and new primary
- Application cannot connect after successful failover
- Multiple standbys fail to reconnect

### Escalation Contacts:

| Condition | Contact | Method |
|-----------|---------|--------|
| Technical escalation | Database Team Lead | PagerDuty: database-leads |
| Business impact | VP Engineering | Slack: @vp-eng |
| Security concern | Security Team | PagerDuty: security-oncall |

### Information to Include When Escalating:
- Timestamp when procedure started
- Current step number
- Error messages encountered
- Actions already attempted
```

### Rollback Procedure

Every runbook that makes changes needs a rollback plan.

The rollback section provides steps to undo changes if the procedure causes additional problems.

```markdown
Markdown## Rollback

If failover causes additional issues, use this procedure to restore the previous primary.

**Warning:** Rollback may result in data loss for writes made to the new primary.

### Rollback Steps:

1. Stop the newly promoted primary:

\`\`\`bash
ssh admin@db-primary-02.prod.internal
sudo systemctl stop postgresql
\`\`\`bash

2. Restore connectivity to original primary:

\`\`\`bash
ssh admin@db-primary-01.prod.internal
psql -U admin -d postgres -c "ALTER SYSTEM RESET max_connections;"
psql -U admin -d postgres -c "SELECT pg_reload_conf();"
\`\`\`bash

3. Verify original primary accepts connections:

\`\`\`bash
psql -h db-primary-01.prod.internal -U admin -c "SELECT 1;"
\`\`\`bash

4. Update DNS or load balancer to point to original primary.
\`\`\`text

## Writing Clear and Actionable Steps

The quality of your runbook depends on how you write individual steps. Here are patterns that work.

### Use Imperative Voice

Tell the operator what to do, not what they might consider doing.

This example shows the difference between unclear and clear instruction writing.

\`\`\`markdown
# Unclear

You may want to check the logs for any errors that might indicate the root cause.

# Clear
Check the application logs for errors. Run:
\`\`\`bash
kubectl logs -l app=api-server --tail=100 --since=15m
\`\`\`bash
\`\`\`text

### Include Expected Outputs

Every command should show what success and failure look like.

Including expected outputs helps operators verify they are on the right track.

\`\`\`bash
# Check service health
systemctl status nginx
```

**Expected output (healthy):**

```
Textnginx.service - A high performance web server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: active (running) since Mon 2026-01-28 10:00:00 UTC
```

**Expected output (problem):**

```
Textnginx.service - A high performance web server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: failed (Result: exit-code) since Mon 2026-01-28 10:00:00 UTC
```

### Handle Edge Cases

Real incidents rarely follow the happy path. Document what to do when things go wrong.

Edge case handling prevents operators from getting stuck when unexpected situations occur.

```markdown
Markdown### If the service fails to start:

Check the nginx error log:

\`\`\`bash
tail -50 /var/log/nginx/error.log
\`\`\`bash

**Common errors and solutions:**

| Error | Cause | Solution |
|-------|-------|----------|
| "Address already in use" | Port 80 occupied | \`sudo lsof -i :80\` and stop conflicting process |
| "could not open error log file" | Permission issue | \`sudo chown -R www-data:www-data /var/log/nginx\` |
| "unknown directive" | Config syntax error | \`nginx -t\` to identify line number |
\`\`\`text

### Make Commands Copy-Paste Ready

Operators should be able to copy commands directly. Avoid placeholders that require mental substitution during an incident.

Commands should be ready to execute without modification during high-pressure incidents.

\`\`\`markdown
# Instead of this:
ssh $USER@$SERVER

# Write this:
ssh admin@api-server-01.prod.internal

# Or if variables are necessary, define them explicitly:
\`\`\`bash
## Set environment variables first
export ENV="prod"
export REGION="us-east-1"

## Then use them in commands
kubectl --context=${REGION}-${ENV} get pods -l app=api
\`\`\`bash
\`\`\`text

## Creating Runbooks for Common Scenarios

Here are templates for runbooks you likely need.

### High CPU Usage Runbook Template

This diagnostic runbook helps operators identify the cause of high CPU usage.

\`\`\`markdown
# High CPU Usage Investigation

## Metadata
- **ID:** RB-SYS-001
- **Last Updated:** 2026-01-28
- **Owner:** Platform Team

## Trigger
- Alert: \`HighCPUUsage\` (CPU > 80% for 5 minutes)
- Observable: System slowness, increased latency

## Procedure

### Step 1: Identify High CPU Processes

Connect to the affected host and identify CPU-heavy processes:

\`\`\`bash
ssh admin@${HOSTNAME}
top -bn1 -o %CPU | head -20
\`\`\`bash

**Expected output:** List of processes sorted by CPU usage.

### Step 2: Check for Known CPU-Intensive Operations

Verify if any expected operations are running:

\`\`\`bash
## Check for running backups
pgrep -a backup

## Check for batch jobs
systemctl status batch-processor
\`\`\`bash

### Step 3: Analyze Process Behavior

For the top CPU-consuming process, gather details:

\`\`\`bash
## Get process details
ps aux | grep ${PID}

## Check open files
lsof -p ${PID} | head -50

## Check process threads
ps -T -p ${PID}
\`\`\`bash

### Step 4: Determine Action

Based on findings:

| Finding | Action |
|---------|--------|
| Backup running | Wait for completion or reschedule |
| Runaway process | Restart the service (see step 5) |
| Legitimate load | Scale horizontally |
| Unknown process | Escalate to security |

### Step 5: Restart Service (if needed)

\`\`\`bash
sudo systemctl restart ${SERVICE_NAME}
\`\`\`bash

Verify service health:

\`\`\`bash
systemctl status ${SERVICE_NAME}
\`\`\`bash
\`\`\`text

### Service Deployment Runbook Template

This deployment runbook guides operators through a controlled service deployment.

\`\`\`markdown
# Service Deployment Runbook

## Metadata
- **ID:** RB-DEP-001
- **Last Updated:** 2026-01-28
- **Owner:** DevOps Team
- **Risk Level:** Medium

## Prerequisites

- [ ] Change approved in change management system
- [ ] Deployment window confirmed
- [ ] Rollback plan verified
- [ ] Monitoring dashboards ready

## Pre-Deployment Checks

### Step 1: Verify Current State

Record current version and health:

\`\`\`bash
kubectl get deployment api-server -o jsonpath='{.spec.template.spec.containers[0].image}'
\`\`\`bash

Check current pod health:

\`\`\`bash
kubectl get pods -l app=api-server
\`\`\`bash

**All pods should show Running and Ready.**

### Step 2: Verify New Image

Confirm the new image exists and is scannable:

\`\`\`bash
## Check image exists
docker manifest inspect registry.example.com/api-server:${NEW_VERSION}

## Check vulnerability scan passed
curl -s https://harbor.example.com/api/v2.0/projects/api/repositories/api-server/artifacts/${NEW_VERSION}/scan | jq '.severity'
\`\`\`bash

## Deployment Procedure

### Step 3: Update Deployment

Apply the new deployment configuration:

\`\`\`bash
kubectl set image deployment/api-server \
  api-server=registry.example.com/api-server:${NEW_VERSION} \
  --record
\`\`\`bash

### Step 4: Monitor Rollout

Watch the rollout progress:

\`\`\`bash
kubectl rollout status deployment/api-server --timeout=300s
\`\`\`bash

**Expected output:**
\`\`\`text
deployment "api-server" successfully rolled out
\`\`\`bash

### Step 5: Verify New Version

Confirm pods are running the new version:

\`\`\`bash
kubectl get pods -l app=api-server -o jsonpath='{.items[*].spec.containers[0].image}'
\`\`\`bash

## Post-Deployment Verification

### Step 6: Health Checks

\`\`\`bash
## Check endpoint health
curl -s https://api.example.com/health | jq '.'

## Check error rate
curl -s "https://prometheus.example.com/api/v1/query?query=rate(http_requests_total{status=~'5..'}[5m])" | jq '.data.result[0].value[1]'
\`\`\`bash

**Error rate should be below 0.01 (1%).**

## Rollback

If issues are detected:

\`\`\`bash
kubectl rollout undo deployment/api-server
kubectl rollout status deployment/api-server --timeout=300s
\`\`\`bash
\`\`\`text

### Certificate Rotation Runbook Template

This maintenance runbook guides operators through TLS certificate rotation.

\`\`\`markdown
# TLS Certificate Rotation

## Metadata
- **ID:** RB-SEC-001
- **Last Updated:** 2026-01-28
- **Owner:** Security Team
- **Risk Level:** High
- **Requires Approval:** Yes

## Trigger
- Alert: \`CertificateExpiringSoon\` (< 30 days to expiration)
- Scheduled: Quarterly rotation

## Prerequisites

- [ ] New certificate obtained from CA
- [ ] Certificate chain validated
- [ ] Change window approved
- [ ] Rollback certificate available

## Pre-Rotation Checks

### Step 1: Verify New Certificate

Validate the new certificate:

\`\`\`bash
## Check certificate dates
openssl x509 -in new-cert.pem -noout -dates

## Verify certificate chain
openssl verify -CAfile ca-bundle.pem new-cert.pem

## Check certificate matches private key
openssl x509 -noout -modulus -in new-cert.pem | md5sum
openssl rsa -noout -modulus -in new-key.pem | md5sum
\`\`\`bash

**Both md5sums must match.**

## Rotation Procedure

### Step 2: Backup Current Certificate

\`\`\`bash
kubectl get secret tls-certificate -o yaml > tls-certificate-backup-$(date +%Y%m%d).yaml
\`\`\`bash

### Step 3: Update Kubernetes Secret

\`\`\`bash
kubectl create secret tls tls-certificate \
  --cert=new-cert.pem \
  --key=new-key.pem \
  --dry-run=client -o yaml | kubectl apply -f -
\`\`\`bash

### Step 4: Reload Ingress Controller

\`\`\`bash
kubectl rollout restart deployment/ingress-nginx-controller -n ingress-nginx
kubectl rollout status deployment/ingress-nginx-controller -n ingress-nginx
\`\`\`bash

## Verification

### Step 5: Verify Certificate in Use

\`\`\`bash
echo | openssl s_client -connect api.example.com:443 -servername api.example.com 2>/dev/null | openssl x509 -noout -dates
\`\`\`bash

**Not After date should match new certificate.**

## Rollback

If issues occur:

\`\`\`bash
kubectl apply -f tls-certificate-backup-$(date +%Y%m%d).yaml
kubectl rollout restart deployment/ingress-nginx-controller -n ingress-nginx
\`\`\`bash
\`\`\`text

## Automating Runbook Execution

While runbooks start as documentation, many can be partially or fully automated. The key is progressive automation.

\`\`\`mermaid
flowchart LR
    A[Manual Runbook] --> B[Documented Commands]
    B --> C[Script Collection]
    C --> D[Orchestrated Workflow]
    D --> E[Self-Healing Automation]

    style A fill:#ffcccc
    style B fill:#ffe6cc
    style C fill:#ffffcc
    style D fill:#ccffcc
    style E fill:#ccccff
```

### Level 1: Documented Commands

Start with runbooks that contain copy-paste commands. This is better than having no documentation.

### Level 2: Script Collection

Package related commands into scripts that operators can run.

This script collects diagnostic information for the database team.

```bash
Bash#!/bin/bash
# db-diagnostics.sh - Collect database diagnostic information

set -e

echo "=== Database Diagnostics ==="
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

echo "=== Replication Status ==="
psql -h $DB_HOST -U admin -d postgres -c \
  "SELECT client_addr, state, sent_lsn, replay_lsn FROM pg_stat_replication;"

echo ""
echo "=== Connection Statistics ==="
psql -h $DB_HOST -U admin -d postgres -c \
  "SELECT state, count(*) FROM pg_stat_activity GROUP BY state;"

echo ""
echo "=== Long Running Queries ==="
psql -h $DB_HOST -U admin -d postgres -c \
  "SELECT pid, now() - pg_stat_activity.query_start AS duration, query
   FROM pg_stat_activity
   WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes'
   AND state != 'idle';"

echo ""
echo "=== Disk Usage ==="
psql -h $DB_HOST -U admin -d postgres -c \
  "SELECT pg_size_pretty(pg_database_size(current_database())) as db_size;"
```

### Level 3: Orchestrated Workflow

Connect scripts into workflows with proper error handling and notifications.

This Python script orchestrates the database failover workflow with proper error handling and notifications.

```python
Python#!/usr/bin/env python3
"""
Database Failover Orchestrator

This script automates the database failover process with proper
error handling, notifications, and audit logging.
"""

import subprocess
import logging
import sys
from datetime import datetime
from typing import Tuple

# Configure logging to capture all operations for audit purposes
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'/var/log/failover/failover-{datetime.now().strftime("%Y%m%d-%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DatabaseFailover:
    """
    Manages database failover operations with proper validation
    and rollback capabilities.
    """

    def __init__(self, primary_host: str, standby_host: str):
        """
        Initialize the failover handler with primary and standby hosts.

        Args:
            primary_host: Current primary database hostname
            standby_host: Standby database to promote
        """
        self.primary_host = primary_host
        self.standby_host = standby_host
        self.rollback_steps = []

    def check_prerequisites(self) -> bool:
        """
        Verify all prerequisites are met before starting failover.
        Returns True if all checks pass, False otherwise.
        """
        logger.info("Checking prerequisites...")

        # Verify connectivity to both hosts
        checks = [
            self._check_host_connectivity(self.primary_host),
            self._check_host_connectivity(self.standby_host),
            self._check_replication_status(),
        ]

        return all(checks)

    def _check_host_connectivity(self, host: str) -> bool:
        """
        Verify SSH connectivity to a database host.
        """
        try:
            result = subprocess.run(
                ['ssh', '-o', 'ConnectTimeout=5', f'admin@{host}', 'echo ok'],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                logger.info(f"Connectivity to {host}: OK")
                return True
            else:
                logger.error(f"Cannot connect to {host}: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            logger.error(f"Connection to {host} timed out")
            return False

    def _check_replication_status(self) -> bool:
        """
        Verify replication is functioning before failover.
        """
        logger.info("Checking replication status...")
        # Implementation details omitted for brevity
        return True

    def execute_failover(self) -> Tuple[bool, str]:
        """
        Execute the complete failover procedure.

        Returns:
            Tuple of (success: bool, message: str)
        """
        if not self.check_prerequisites():
            return False, "Prerequisites check failed"

        try:
            # Step 1: Block new connections
            logger.info("Step 1: Blocking new connections to primary")
            self._block_connections()
            self.rollback_steps.append(self._unblock_connections)

            # Step 2: Wait for transactions to complete
            logger.info("Step 2: Waiting for transactions to complete")
            self._wait_for_transactions()

            # Step 3: Promote standby
            logger.info("Step 3: Promoting standby to primary")
            self._promote_standby()

            # Step 4: Update DNS
            logger.info("Step 4: Updating DNS records")
            self._update_dns()

            # Step 5: Verify
            logger.info("Step 5: Verifying failover success")
            if self._verify_failover():
                logger.info("Failover completed successfully")
                return True, "Failover completed successfully"
            else:
                raise Exception("Failover verification failed")

        except Exception as e:
            logger.error(f"Failover failed: {e}")
            self._execute_rollback()
            return False, f"Failover failed: {e}"

    def _execute_rollback(self):
        """
        Execute rollback steps in reverse order.
        """
        logger.warning("Executing rollback...")
        for step in reversed(self.rollback_steps):
            try:
                step()
            except Exception as e:
                logger.error(f"Rollback step failed: {e}")

    # Additional helper methods would be implemented here
    def _block_connections(self): pass
    def _unblock_connections(self): pass
    def _wait_for_transactions(self): pass
    def _promote_standby(self): pass
    def _update_dns(self): pass
    def _verify_failover(self) -> bool: return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: failover.py <primary_host> <standby_host>")
        sys.exit(1)

    failover = DatabaseFailover(sys.argv[1], sys.argv[2])
    success, message = failover.execute_failover()

    if success:
        print(f"SUCCESS: {message}")
        sys.exit(0)
    else:
        print(f"FAILED: {message}")
        sys.exit(1)
```

### Level 4: Self-Healing Automation

The final level integrates automated remediation with your monitoring system.

This Kubernetes operator watches for specific conditions and automatically executes remediation.

```yaml
YAML# Example: Kubernetes operator for automatic remediation
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: auto-remediation-rules
spec:
  groups:
    - name: auto-remediation
      rules:
        # This rule triggers automatic pod restart when memory exceeds threshold
        - alert: HighMemoryUsage
          expr: |
            container_memory_usage_bytes / container_spec_memory_limit_bytes > 0.9
          for: 5m
          labels:
            severity: warning
            # This label triggers the remediation controller
            auto_remediate: "restart-pod"
          annotations:
            summary: "Container memory usage above 90%"
            runbook_url: "https://runbooks.example.com/RB-K8S-001"
```

## Runbook Lifecycle Management

Creating runbooks is only the beginning. Keeping them accurate requires ongoing effort.

<svg id="mermaid-1776012253288" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="max-width: 321.2090148925781px;" viewBox="-8 -8 321.2090148925781 1080.953125" role="graphics-document document" aria-roledescription="flowchart-v2"><g><marker id="mermaid-1776012253288_flowchart-pointEnd" viewBox="0 0 10 10" refX="6" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253288_flowchart-pointStart" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253288_flowchart-circleEnd" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-1776012253288_flowchart-circleStart" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-1776012253288_flowchart-crossEnd" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-1776012253288_flowchart-crossStart" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><g><g></g><g><path d="M173.986,39L173.986,43.167C173.986,47.333,173.986,55.667,173.986,63.117C173.986,70.567,173.986,77.133,173.986,80.417L173.986,83.7" id="L-A-B-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M143.46,128L136.938,132.167C130.415,136.333,117.37,144.667,110.847,152.117C104.324,159.567,104.324,166.133,104.324,169.417L104.324,172.7" id="L-B-C-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M104.324,217L104.324,221.167C104.324,225.333,104.324,233.667,104.324,241.117C104.324,248.567,104.324,255.133,104.324,258.417L104.324,261.7" id="L-C-D-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M104.324,306L104.324,310.167C104.324,314.333,104.324,322.667,104.324,330.117C104.324,337.567,104.324,344.133,104.324,347.417L104.324,350.7" id="L-D-E-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M104.324,395L104.324,399.167C104.324,403.333,104.324,411.667,104.39,419.2C104.456,426.734,104.588,433.467,104.654,436.834L104.72,440.201" id="L-E-F-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M79.681,547.864L72.853,558.138C66.025,568.412,52.369,588.96,45.541,608.651C38.713,628.341,38.713,647.174,38.713,666.008C38.713,684.841,38.713,703.674,38.713,735.295C38.713,766.915,38.713,811.323,38.713,855.73C38.713,900.138,38.713,944.546,52.224,972.567C65.735,1000.588,92.757,1012.222,106.267,1018.04L119.778,1023.857" id="L-F-G-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M216.623,1025.953L231.387,1019.786C246.152,1013.62,275.68,1001.286,290.445,972.916C305.209,944.546,305.209,900.138,305.209,855.73C305.209,811.323,305.209,766.915,305.209,735.295C305.209,703.674,305.209,684.841,305.209,666.008C305.209,647.174,305.209,628.341,305.209,602.132C305.209,575.923,305.209,542.339,305.209,510.754C305.209,479.169,305.209,449.585,305.209,427.376C305.209,405.167,305.209,390.333,305.209,375.5C305.209,360.667,305.209,345.833,305.209,331C305.209,316.167,305.209,301.333,305.209,286.5C305.209,271.667,305.209,256.833,305.209,242C305.209,227.167,305.209,212.333,305.209,197.5C305.209,182.667,305.209,167.833,293.759,156.534C282.309,145.234,259.408,137.468,247.958,133.585L236.508,129.702" id="L-G-B-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M129.968,547.864L136.629,558.138C143.29,568.412,156.613,588.96,163.274,604.517C169.936,620.074,169.936,630.641,169.936,635.924L169.936,641.208" id="L-F-H-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M152.596,685.508L147.113,691.674C141.629,697.841,130.662,710.174,128.929,726.158C127.195,742.141,134.695,761.774,138.444,771.59L142.194,781.407" id="L-H-I-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M170.436,952.453L170.352,958.536C170.269,964.62,170.102,976.786,170.019,988.153C169.936,999.52,169.936,1010.086,169.936,1015.37L169.936,1020.653" id="L-I-G-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path><path d="M196.786,786.358L200.684,775.716C204.582,765.074,212.379,743.791,211.381,727.643C210.383,711.495,200.59,700.482,195.693,694.975L190.797,689.468" id="L-I-H-0" style="fill:none;" marker-end="url(#mermaid-1776012253288_flowchart-pointEnd)" stroke="currentColor"></path></g><g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g><g transform="translate(0, 0)"></g></g><g transform="translate(38.712890625, 722.5078125)"><g transform="translate(-10.7421875, -12)"><foreignObject width="21.484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">No</div></foreignObject></g></g><g><g transform="translate(0, 0)"></g></g><g transform="translate(169.935546875, 609.5078125)"><g transform="translate(-13.56640625, -12)"><foreignObject width="27.1328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Yes</div></foreignObject></g></g><g><g transform="translate(0, 0)"></g></g><g transform="translate(169.935546875, 988.953125)"><g transform="translate(-13.56640625, -12)"><foreignObject width="27.1328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Yes</div></foreignObject></g></g><g transform="translate(220.17578125, 722.5078125)"><g transform="translate(-10.7421875, -12)"><foreignObject width="21.484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">No</div></foreignObject></g></g></g><g><g id="flowchart-A-34" data-node="true" data-id="A" transform="translate(173.986328125, 19.5)"><rect style="" rx="0" ry="0" x="-67.92578125" y="-19.5" width="135.8515625" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-60.42578125, -12)"><rect></rect><foreignObject width="120.8515625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Create Runbook</div></foreignObject></g></g><g id="flowchart-B-35" data-node="true" data-id="B" transform="translate(173.986328125, 108.5)"><rect style="" rx="0" ry="0" x="-62.953125" y="-19.5" width="125.90625" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-55.453125, -12)"><rect></rect><foreignObject width="110.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Test in Staging</div></foreignObject></g></g><g id="flowchart-C-37" data-node="true" data-id="C" transform="translate(104.32421875, 197.5)"><rect style="" rx="0" ry="0" x="-84.30078125" y="-19.5" width="168.6015625" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-76.80078125, -12)"><rect></rect><foreignObject width="153.6015625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Review and Approve</div></foreignObject></g></g><g id="flowchart-D-39" data-node="true" data-id="D" transform="translate(104.32421875, 286.5)"><rect style="" rx="0" ry="0" x="-104.32421875" y="-19.5" width="208.6484375" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-96.82421875, -12)"><rect></rect><foreignObject width="193.6484375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Deploy to Production Wiki</div></foreignObject></g></g><g id="flowchart-E-41" data-node="true" data-id="E" transform="translate(104.32421875, 375.5)"><rect style="" rx="0" ry="0" x="-85.69140625" y="-19.5" width="171.3828125" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-78.19140625, -12)"><rect></rect><foreignObject width="156.3828125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Use During Incidents</div></foreignObject></g></g><g id="flowchart-F-43" data-node="true" data-id="F" transform="translate(104.32421875, 508.75390625)"><polygon points="63.75390625,0 127.5078125,-63.75390625 63.75390625,-127.5078125 0,-63.75390625" transform="translate(-63.75390625,63.75390625)" style="" fill="none" stroke="currentColor"></polygon><g style="" transform="translate(-36.75390625, -12)"><rect></rect><foreignObject width="73.5078125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Effective?</div></foreignObject></g></g><g id="flowchart-G-45" data-node="true" data-id="G" transform="translate(169.935546875, 1045.453125)"><rect style="" rx="0" ry="0" x="-70.1875" y="-19.5" width="140.375" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-62.6875, -12)"><rect></rect><foreignObject width="125.375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Update Runbook</div></foreignObject></g></g><g id="flowchart-H-49" data-node="true" data-id="H" transform="translate(169.935546875, 666.0078125)"><rect style="" rx="0" ry="0" x="-71.5546875" y="-19.5" width="143.109375" height="39" fill="none" stroke="currentColor"></rect><g style="" transform="translate(-64.0546875, -12)"><rect></rect><foreignObject width="128.109375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Schedule Review</div></foreignObject></g></g><g id="flowchart-I-51" data-node="true" data-id="I" transform="translate(169.935546875, 855.73046875)"><polygon points="96.22265625,0 192.4453125,-96.22265625 96.22265625,-192.4453125 0,-96.22265625" transform="translate(-96.22265625,96.22265625)" style="" fill="none" stroke="currentColor"></polygon><g style="" transform="translate(-69.22265625, -12)"><rect></rect><foreignObject width="138.4453125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Changes Needed?</div></foreignObject></g></g></g></g></g></svg>

### Testing Runbooks

Untested runbooks are unreliable. Build testing into your workflow.

**Game Days:** Schedule monthly sessions where the team executes runbooks against intentionally broken staging environments.

**New Engineer Validation:** Have new team members follow runbooks during onboarding. Fresh eyes catch unclear instructions.

**Chaos Engineering:** When you inject failures in chaos experiments, the corresponding runbook should resolve them.

### Maintaining Currency

Systems change, but documentation often does not. Use these strategies to keep runbooks current.

**Change-Triggered Reviews:** When infrastructure changes, flag affected runbooks for review.

This CI/CD configuration example automatically flags runbooks when related infrastructure changes.

```yaml
YAML# .github/workflows/runbook-review.yml
name: Flag Runbook Reviews

on:
  push:
    paths:
      - 'terraform/**'
      - 'kubernetes/**'

jobs:
  check-runbooks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for affected runbooks
        run: |
          # Map infrastructure paths to runbook IDs
          CHANGED_PATHS=$(git diff --name-only HEAD~1)

          if echo "$CHANGED_PATHS" | grep -q "terraform/database"; then
            echo "Database infrastructure changed"
            echo "Review needed: RB-DB-001, RB-DB-002, RB-DB-003"
            # Create review ticket or send notification
          fi

          if echo "$CHANGED_PATHS" | grep -q "kubernetes/ingress"; then
            echo "Ingress configuration changed"
            echo "Review needed: RB-NET-001, RB-SEC-001"
          fi
```

**Post-Incident Reviews:** After every incident where a runbook was used, ask:

- Did the runbook help resolve the incident?
- Were any steps unclear or outdated?
- Did we discover steps that should be added?

**Scheduled Reviews:** Even without changes, review runbooks quarterly. Add ownership and review dates to your metadata.

## Runbook Repository Organization

As your runbook collection grows, organization becomes critical.

### Naming Conventions

Use consistent naming that sorts logically and indicates purpose.

```
Text{service}-{action}-{scope}.md

Examples:
database-failover-primary.md
database-recovery-replica.md
kubernetes-restart-deployment.md
kubernetes-scale-nodes.md
network-troubleshoot-connectivity.md
security-rotate-certificates.md
```

### Directory Structure

Organize runbooks by service or function.

```
Textrunbooks/
  database/
    RB-DB-001-primary-failover.md
    RB-DB-002-replica-recovery.md
    RB-DB-003-backup-restore.md
  kubernetes/
    RB-K8S-001-pod-restart.md
    RB-K8S-002-node-drain.md
    RB-K8S-003-cluster-upgrade.md
  network/
    RB-NET-001-connectivity.md
    RB-NET-002-dns-issues.md
  security/
    RB-SEC-001-certificate-rotation.md
    RB-SEC-002-credential-rotation.md
  _templates/
    diagnostic-template.md
    remediation-template.md
    deployment-template.md
```

### Searchability

Make runbooks findable by including symptoms and error messages.

This keywords section helps operators find the right runbook when searching for error messages.

```markdown
Markdown## Keywords and Search Terms

### Alert Names
- DatabasePrimaryUnreachable
- ReplicationLagCritical
- ConnectionPoolExhausted

### Error Messages
- "FATAL: the database system is not yet accepting connections"
- "could not connect to server: Connection refused"
- "psql: error: connection to server failed"
- "remaining connection slots are reserved"

### Symptoms
- Write operations failing
- Increased latency on read operations
- Application 500 errors
- Connection timeouts
```

## Getting Started

You do not need perfect runbooks on day one. Start with impact.

1. **List your top 5 incidents** from the past quarter
2. **Create a runbook** for each incident type
3. **Test each runbook** the next time that incident occurs
4. **Iterate** based on what worked and what did not

A simple runbook that works is better than a comprehensive one that does not exist.

The goal is not documentation for its own sake. The goal is faster incident resolution with less stress. Build runbooks that serve that purpose, and your on-call engineers will thank you at 3 AM.

## Conclusion

Effective runbooks are a cornerstone of operational excellence. They reduce mean time to resolution, decrease stress during incidents, and enable knowledge sharing across your team. By following the structure and practices outlined in this guide, you can create runbooks that your team will actually use.

Remember these key principles:

- **Be specific:** Every step should tell the operator exactly what to do
- **Include verification:** Show what success and failure look like
- **Plan for failure:** Include rollback procedures and edge case handling
- **Keep them current:** Test regularly and update after every use
- **Automate progressively:** Move from documentation to scripts to self-healing

Start small, iterate based on real-world usage, and build a runbook library that makes incidents manageable rather than chaotic.

@nawazdhandala • Feb 02, 2026 •

Nawaz is building OneUptime with a passion for engineering reliable systems and improving observability.

[GitHub](https://github.com/nawazdhandala)

### Improve this Blog Post

All our blog posts are open source. Found a typo, want to add more detail, or have a better explanation? Anyone can contribute and make this post better for everyone.

[Edit this Post on GitHub](https://github.com/oneuptime/blog/tree/master/posts/2026-02-02-effective-runbooks) [Contributing Guidelines](https://github.com/oneuptime/blog)