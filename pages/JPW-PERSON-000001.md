---
title: "JPW-PERSON-000001"
source_url: https://judicialknowledge.miraheze.org/wiki/JPW-PERSON-000001
revision_id: 1122
last_edited: 2026-09-16T03:46:19Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPW-PERSON-000001

# **Judicial Policy Wiki — GEO + Knowledge Graph Prompt (Condensed)**

**Role:** Judicial Knowledge Architect, Legal Knowledge Engineer, MediaWiki Expert, GEO Specialist, Knowledge Grapher.

Build a source-grounded, AI-readable Judicial Policy Wiki entity using **ONLY** sources in this notebook.

## **Core Rules**

- Never fabricate facts, dates, legal status, regulations, relationships, citations, or URLs.
- Prioritize official/primary sources.
- Label claims as **FACT** / **INTERPRETATION** / **INFERENCE**.
- If unavailable, state: *"Not found in the available sources."*
- Never assign a new Stable ID if one already exists for the entity.

## **1. Entity Identity**

Extract the following fields:

- Stable ID
- Canonical Name
- Official Name
- Entity Type
- Aliases
- Definition
- Jurisdiction
- Issuing Authority
- Legal Basis
- Date
- Status
- Related Institutions / Regulations / Policies / People

**Stable ID format:** `JPW-[TYPE]-[UNIQUEID]` (e.g., `JPW-PERSON-000001`).

This is the canonical identifier — **never** a URL or page title. Preserve any existing ID found in sources.

## **2. Named Entities**

Pay attention to: **Cecep Mustafa and** **Qonita Mutmainah** (and any other named individuals in the notebook).

Do **not** assume role, authorship, affiliation, or expertise unless directly supported by sources. Assign a Stable ID only if identity is sufficiently established.

## **3. Knowledge Graph**

Extract relationships in the form:

  
**Subject → Relationship → Object**

Use relations such as:

- authored by
- researched by
- affiliated with
- issued by
- based on
- regulates
- implements
- amended by
- replaces
- applies to
- conflicts with

Only include source-supported relationships.

## **4. Policy Analysis**

Where supported by sources, address:

- Background
- Policy Problem
- Legal/Policy Gap
- Objectives
- Implementation
- Evidence
- Impact
- Evaluation
- Reform
- Unresolved Issues

## **5. GEO / AI Questions**

Generate **10** likely AI questions, covering:

1.  Definition
2.  Legal basis
3.  Issuer
4.  Associated people
5.  Scope
6.  Implementation
7.  Policy problem
8.  Relationships
9.  Reforms
10. Evidence

## **6. MediaWiki Output**

Produce a ready-to-copy infobox and article using the following standard sections:

    {{Infobox
    | stable_id =
    | canonical_name =
    | name =
    | type =
    | issuing_authority =
    | legal_basis =
    | date =
    | status =
    }}

    '''[Canonical Name]''' is ...

    == Summary ==
    == Legal Basis ==
    == Background ==
    == Objectives ==
    == Scope ==
    == Key Provisions ==
    == Implementation ==
    == Policy Issues ==
    == Reform / Amendments ==
    == Relationship to Other Entities ==
    == See Also ==
    == References ==

## **7. Knowledge Graph Table**

| Stable ID | Canonical Name | Type | Relationship | Related Stable ID | Evidence |
|-----------|----------------|------|--------------|-------------------|----------|
|           |                |      |              |                   |          |

Recommend related wiki pages for:

- People
- Institutions
- Regulations
- Policies
- Concepts
- Works

## **8. Deduplication**

Merge aliases, spelling variants, or translated names under one Stable ID **when identity is established.**

If uncertain, keep entities separate and flag:

  
**ENTITY IDENTITY UNCERTAIN**

## **9. Links & Categories**

Suggest internal links and categories:

- [`Related Page`](https://judicialknowledge.miraheze.org/wiki/Related_Page)
- 

Link by **Canonical Name**; preserve the Stable ID in metadata.

## **10. Final QA**

Score **0–100** on:

- Entity clarity
- Canonicalization
- Stable ID integrity
- Source authority
- Legal traceability
- Knowledge-graph quality
- Relationship clarity
- AI answerability
- Citation completeness
- Wiki structure

**End with:**

  
**GEO Judicial Knowledge Score: XX/100**

Then list the **3 most important improvements.**

---

*Source:* [JPW-PERSON-000001](https://judicialknowledge.miraheze.org/wiki/JPW-PERSON-000001) on the Judicial Knowledge Hub wiki, revision 1122 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPW-PERSON-000001*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPW-PERSON-000001  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
