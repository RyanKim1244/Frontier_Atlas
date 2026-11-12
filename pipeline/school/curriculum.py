# School mathematics (from the first year of school): concepts from pipeline/school/concepts.md, written in clusters.
# A concept is published only once its page passes review (school/concepts/final_*.json). (id, title, short, area, fields, stage, prerequisites)
C = [
 # --- cluster 1: early number and counting ---
 ("counting-number-names", "Counting and number names", "Counting", "arithmetic", ["number-theory"], "school", []),
 ("comparing-ordering-numbers", "Comparing and ordering numbers", "Comparing numbers", "arithmetic", ["number-theory"], "school", ["counting-number-names"]),
 ("composing-decomposing-numbers", "Composing and decomposing numbers (number bonds)", "Number bonds", "arithmetic", ["number-theory"], "school", ["counting-number-names"]),
 ("place-value", "Place value and the base-ten numeral system", "Place value", "arithmetic", ["number-theory"], "school", ["counting-number-names", "composing-decomposing-numbers"]),
 ("number-line", "The number line", "Number line", "arithmetic", ["number-theory"], "school", ["comparing-ordering-numbers"]),
 ("odd-even-numbers", "Odd and even numbers", "Odd and even", "arithmetic", ["number-theory"], "school", ["counting-number-names"]),
 ("patterns-sequences", "Patterns and number sequences", "Patterns", "arithmetic", ["number-theory"], "school", ["counting-number-names"]),
 ("addition-subtraction", "Addition and subtraction of whole numbers", "Adding & subtracting", "arithmetic", ["number-theory"], "school", ["composing-decomposing-numbers", "place-value"]),
 ("column-addition-subtraction", "Column addition and subtraction algorithms", "Column methods", "arithmetic", ["number-theory"], "school", ["addition-subtraction", "place-value"]),
 ("equality-equal-sign", "Equality, the equal sign and unknowns", "Equal sign", "arithmetic", ["algebra"], "school", ["addition-subtraction"]),
 ("properties-of-operations", "Properties of operations: commutative, associative, identity, inverse", "Properties of operations", "arithmetic", ["algebra"], "school", ["addition-subtraction"]),
 ("multiplication", "Multiplication of whole numbers", "Multiplication", "arithmetic", ["number-theory"], "school", ["addition-subtraction", "patterns-sequences"]),
 ("division", "Division of whole numbers", "Division", "arithmetic", ["number-theory"], "school", ["multiplication"]),
 ("distributive-property", "The distributive property", "Distributivity", "arithmetic", ["algebra"], "school", ["multiplication", "properties-of-operations"]),
]
NEW_AREAS = [{"id": "arithmetic", "name": "Numbers and arithmetic", "blurb": "Counting, place value and the four operations: where mathematics starts.", "fields": ["number-theory"]}]
STAGE_DETAIL = {  # finer school stage, shown to writers (the site's stage filter stays 'school')
 "counting-number-names": "early primary (ages 4-7)", "comparing-ordering-numbers": "early primary", "composing-decomposing-numbers": "early primary",
 "place-value": "early to late primary", "number-line": "early primary", "odd-even-numbers": "early primary", "patterns-sequences": "early primary",
 "addition-subtraction": "early primary", "column-addition-subtraction": "early to late primary (ages 7-10)", "equality-equal-sign": "early primary",
 "properties-of-operations": "early primary", "multiplication": "early primary (ages 7-9)", "division": "late primary (ages 8-10)", "distributive-property": "late primary",
}
