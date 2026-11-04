<invoke name="sparql">
PREFIX lad: <https://example.org/ladder/>
SELECT ?what (COUNT(DISTINCT ?m) AS ?n) WHERE {
  { ?m lad:parent* ?r . VALUES ?r {lad:E5001 lad:E5167} BIND("members" AS ?what) }
  UNION { ?m lad:parent/lad:parent/lad:parent ?r . VALUES ?r {lad:E5001 lad:E5167} BIND("depth3" AS ?what) }
  UNION { ?m lad:parent/lad:parent ?r2 . ?r2 lad:parent ?r . VALUES ?r {lad:E5001} BIND("x" AS ?what) FILTER(false) }
  UNION { lad:E5167 lad:lei ?m . BIND("lei5167" AS ?what) }
  UNION { lad:E5167 lad:name ?m . BIND("name5167" AS ?what) }
  UNION { lad:E5167 lad:sourceSystem ?m . BIND("src5167" AS ?what) }
} GROUP BY ?what
</parameter>
</invoke>