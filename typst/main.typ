#set page(
  paper: "a4",
  // header: align(right + horizon)[
  //   XCPC Library
  // ],
  numbering: "1",
  margin: (x: 1.5cm, y: 1.1cm)
)
#set heading(numbering: "1.1")

#align(center, text(17pt)[
  *A XCPC Code Library*
])

#show: rest => columns(2, rest)

#outline(
  indent: auto
)

#set text(8pt)

#include "code.typ"
